from django.db import models

from accounts.models import Account


# Create your models here.
class Eduresources(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=128, blank=True)

    class Resource_type(models.TextChoices):
        Video = 'V', 'Video'
        Article = 'A', 'Article'
        BLOG = 'B', 'Blog'
    resource_type = models.CharField(max_length=1, choices=Resource_type.choices, default=Resource_type.Article)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated at', auto_now=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Accessed_BY')
