from django.urls import path
from posts import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/(?P<min_date>.+)/$', views.PostList.as_view()),
    path('download-stats/', views.stats),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
