from rest_framework import mixins
from rest_framework import generics
from posts.models import Post
from posts.serializers import PostSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import permissions
from posts.permissions import IsOwnerOrReadOnly
from django.db.models import Q
import pandas as pd
from django.core.files.storage import FileSystemStorage
import csv
from django.http import HttpResponse

class PostList(generics.ListCreateAPIView):
    permission_classes = ( IsOwnerOrReadOnly,)
    queryset = Post.objects.filter(Q(status="PUBLIC"))
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        serializer.save()
    def get_queryset(self):
        print(self.kwargs)
        print(self.request.GET.keys())
        min_date = self.request.GET.get('min_date',None)
        if min_date is None:
            return Post.objects.all()
        print("here")

        # max_date = self.kwargs['max_date']
        return Post.objects.filter(created_date__gte=min_date)
    def list(self, request):
        queryset = self.get_queryset()
        query1=queryset.filter(Q(status="PUBLIC"))
        print(self.request.user.is_authenticated)
        if request.user.is_authenticated:
            query2=query1|queryset.filter(Q(shared_with_users=self.request.user))
            print(self.request.user)
            query1 = query2 | queryset.filter(owner=request.user)
        serializer = PostSerializer(query1, many=True)
        return Response(serializer.data)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ( IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



def stats(request):
    users=User.objects.all()
    users_name=[i.username for i in users]
    posts=[Post.objects.filter(owner=i) for i in users]
    posts_len=[len(i) for i in posts]
    my_dict={"users":users_name,"num_of_posts":posts_len}
    df=pd.DataFrame(my_dict)
    file_csv=df.to_csv("stats.csv",index=False)
    # with open('stats.csv', 'w', newline="") as myfile:  # python 2: open('stockitems_misuper.csv', 'wb')
    #     wr = csv.writer(myfile)
    #     wr.writerows(df)
    with open('stats.csv') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stats.csv'
        return response
    # print(file_csv)
    # print(type(file_csv))
    # file_system = FileSystemStorage()
    # filename = file_system.save(file_csv, myfile)
    # file_cntent = file_system.open(file_path)
    # response = HttpResponse(file_cntent, content_type='application/text')
    # response['Content-Disposition'] = "attachment; filename=%s" % \
    #                                   ( "stats.csv")
    return response


#
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
