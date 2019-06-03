from rest_framework import serializers
from posts.models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = ('id', 'created_date', 'post_details', 'status',"owner")

# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'posts')
