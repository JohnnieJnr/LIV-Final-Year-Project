from django.db import models
from accounts.models import Account


# Create your models here.
class Events(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='created_by')
    event_name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateField()
    event_location = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated at', auto_now=True)


