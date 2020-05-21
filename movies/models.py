from django.core.validators import FileExtensionValidator
from django.db import models

from accounts.models import CustomUser
from transliterate import translit


def get_episode_path(instance, filename):
    extension = filename.split('.')[-1]
    name = translit(instance.movie.name, "ru", reversed=True).replace(' ', '_')
    return f'movies/{name}/season_{instance.season}' \
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
        help_text='Лучше не грузить фотографии в альбомной ориентации, околоквадратные - лучше всего',
        verbose_name='Картинка',
    )

    def __str__(self):
        return self.name


class Episode(models.Model):

    VALID_VIDEO_EXTENSIONS = [
        "webm",
        "mkv",
        "flv",
        "avi",
        "wmv",
        "mp4",
    ]

    class Meta:
        ordering = ['season', 'number']

    movie = models.ForeignKey(
        Movie,
        on_delete=models.SET_NULL,
        null=True,
        related_name='episodes',
        verbose_name='Аниме'
    )

    number = models.PositiveSmallIntegerField(
        verbose_name='Серия'
    )

    season = models.PositiveSmallIntegerField(
        verbose_name='Сезон'
    )

    title = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='Название серии (если есть)'
    )

    video_obj = models.FileField(
        upload_to=get_episode_path,
        validators=[FileExtensionValidator(allowed_extensions=VALID_VIDEO_EXTENSIONS)],
        verbose_name='Видео'
    )

    def has_next(self):
        episodes = self.movie.episodes.all()
        try:
            episodes.get(season=self.season, number=self.number+1)
        except Episode.DoesNotExist:
            return False
        return True

    def has_previous(self):
        episodes = self.movie.episodes.all()
        try:
            episodes.get(season=self.season, number=self.number-1)
        except Episode.DoesNotExist:
            return False
        return True
