from django.db import models
from django.contrib.auth.models import AbstractUser


def get_photo_path(instance, filename):
    return f'profiles/{instance.username}/photo'


class CustomUser(AbstractUser):
    profile_photo = models.FileField(upload_to=get_photo_path)
