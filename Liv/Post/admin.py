from django.contrib import admin
from.models import  Posts
from accounts.models import Account
from Comment.models import Comments

# Register your models here.
admin.site.register(Posts)
admin.site.register(Account)
admin.site.register(Comments)
