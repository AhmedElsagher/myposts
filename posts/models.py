from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_PRIVATE = 'PRIVATE'
    STATUS_PUBLIC = 'PUBLIC'
    STATUS_SEMI = 'SEMI'
    STATUS_CHOICES = (
        (STATUS_PRIVATE, 'PRIVATE'),
        (STATUS_PUBLIC , 'PUBLIC'),
        (STATUS_SEMI , 'SEMI'))

    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    post_details = models.TextField()
    shared_with_users  = models.ManyToManyField('auth.User')
    status = models.CharField(choices=STATUS_CHOICES, default='PUBLIC',max_length=120)
    class Meta:
        ordering =  ('created_date',)
    def share(user):
        " A convenience function to share with users "
        self.shared_with_users.add(user)
