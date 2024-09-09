from django.db import models
from accounts.models import Account
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


# Create your models here.
class Posts(models.Model):
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='Post/%Y/%m/%d/',
                              validators=[
                                  FileExtensionValidator(
                                      allowed_extensions=['jpeg ', 'png', 'jpg', 'webm'])])
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated at', auto_now=True)

    def clean(self):
        if self.image:
            max_size = 1 * 1024 * 1024 * 1024
            if self.picture.size > max_size:
                raise ValidationError("Image file too large ( > 1GB )")
