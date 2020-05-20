from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from transliterate import translit


def get_photo_path(instance, filename):
    extension = filename.split('.')[-1]
    username = translit(instance.username, 'ru', reversed=True).replace(' ', '_')
    return f'profiles/{username}/photo.{extension}'


class CustomUser(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = [
        [MALE, 'Кун'],
        [FEMALE, 'Тян']
    ]

    VALID_IMAGE_EXTENSIONS = [
        "jpg",
        "jpeg",
        "png",
        "gif",
    ]

    username = models.CharField(
        max_length=128,
        unique=True,
        validators=[MinLengthValidator(5)],
    )

    email = models.EmailField(
        max_length=128,
        unique=True,
    )

    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )

    profile_photo = models.ImageField(
        upload_to=get_photo_path,
    )

