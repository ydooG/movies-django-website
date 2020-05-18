from django.db import models


def get_episode_path(instance, filename):
    return f'movies/{instance.movie.name}/season_{instance.season}/episode_{instance.number}'


def get_movie_image_path(instance, filename):
    return f'movies/{instance.movie.name}/logo'


class Movie(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    movie_picture = models.ImageField(upload_to=get_movie_image_path)

    def __str__(self):
        return self.name


class Episode(models.Model):
    video_obj = models.FileField(upload_to=get_episode_path)
    number = models.PositiveSmallIntegerField()
    season = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=128)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
