import random
import string
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import MyAccountManager


# Create your models here.

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    # required Fields
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def generate_random_username(self, length=8):
        """Generate a random username."""
        while True:
            username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
            if not Account.objects.filter(username=username).exists():
                break
        return username

    def save(self, *args, **kwargs):
        """Override save method to automatically generate a username if none is provided."""
        if not self.username:
            self.username = self.generate_random_username()
        super(Account, self).save(*args, **kwargs)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name', 'phone']

    objects = MyAccountManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, add_label):
        return True

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
