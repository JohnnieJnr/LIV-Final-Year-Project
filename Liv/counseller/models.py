from django.db import models


# Create your models here.
class Counsellor(models.Model):
    name = models.CharField(max_length=100)
    languages_spoken = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

