from django.db import models
from accounts.models import Account
from Post.models import Posts


# Create your models here.

class Comments(models.Model):
    content = models.TextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='post_comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated at', auto_now=True)
