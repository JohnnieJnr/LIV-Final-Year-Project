from django.db import models
from accounts.models import Account
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


# Create your models here.
class Posts(models.Model):
        # Field to store the textual content of the post
    content = models.TextField()

     # Field to store an optional image associated with the post
    # 'blank=True, null=True' makes the field optional
    # 'upload_to' specifies the directory structure where images will be saved
    # 'validators' ensure that only files with allowed extensions are uploaded
    image = models.ImageField(blank=True, null=True, upload_to='Post/%Y/%m/%d/',
                              validators=[
                                  FileExtensionValidator(
                                      allowed_extensions=['jpeg ', 'png', 'jpg', 'webm'])])
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='posts')

        # Automatically set the timestamp when the post is created
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated at', auto_now=True)

    # String representation of the post, returning its content when printed
    def __str__(self):
        return self.content

    # Custom validation logic for the model (called during save)
    def clean(self):
        if self.image:
            max_size = 1 * 1024 * 1024 * 1024
            if self.image.size > max_size:
                raise ValidationError("Image file too large ( > 1GB )")
