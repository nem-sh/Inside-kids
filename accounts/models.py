from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail

# Create your models here.


class User(AbstractUser):
    pass


class Kid(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default='default_image.jpg')
    image_small = ImageSpecField(
        source='image',
        processors=[ResizeToFit(150, 150)],
        format='JPEG',
        options={'quality': 60}
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='kid')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
