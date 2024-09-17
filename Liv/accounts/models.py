from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import MyAccountManager


# Create your models here.

# Custom user model for managing user accounts
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

    # The field used to log in users (in this case, email instead of username)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name', 'phone']

    objects = MyAccountManager()

  # Permissions methods
    # This method checks if the user has a specific permission (admins or superusers can bypass)
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, add_label):
        return True
    
 # String representation of the user object (displays last name and first name)
    def __str__(self):
        return self.last_name + ' ' + self.first_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
