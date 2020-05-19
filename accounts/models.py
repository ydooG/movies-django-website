from django.db import models
from django.contrib.auth.models import AbstractUser


def get_photo_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'profiles/{instance.username}/photo.{extension}'


class CustomUser(AbstractUser):
    profile_photo = models.ImageField(upload_to=get_photo_path)

