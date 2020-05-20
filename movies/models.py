from django.core.validators import FileExtensionValidator
from django.db import models

from accounts.models import CustomUser
from transliterate import translit


def get_episode_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'movies/{instance.movie.name}/season_{instance.season}' \
           f'/episode_{instance.number}.{extension}'


def get_movie_image_path(instance, filename):
    extension = filename.split('.')[-1]
    name = translit(instance.name, "ru", reversed=True).replace(' ', '_')
    return f'movies/{name}/logo.{extension}'


class Movie(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name='Название',
    )

    description = models.TextField(
        verbose_name='Описание',
    )

    movie_picture = models.ImageField(
        upload_to=get_movie_image_path,
        validators=[FileExtensionValidator(allowed_extensions=CustomUser.VALID_IMAGE_EXTENSIONS)],
        help_text='Лучше грузить фотографии в альбомном стиле',
        verbose_name='Картинка',
    )

    def __str__(self):
        return self.name


class Episode(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    number = models.PositiveSmallIntegerField()
    season = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=128)
    video_obj = models.FileField(upload_to=get_episode_path)
