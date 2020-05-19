

from django.db import models
from django.utils.timezone import now

from movies.models import Movie
from accounts.models import CustomUser


class Discussion(models.Model):
    movie = models.OneToOneField(to=Movie, on_delete=models.DO_NOTHING, related_name='discussion')


class Theme(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    discussion = models.ForeignKey(to=Discussion, on_delete=models.CASCADE, related_name='themes')


class Post(models.Model):
    author = models.ForeignKey(to=CustomUser, null=True, on_delete=models.SET_NULL, related_name='posts')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication Date')
    text = models.TextField(max_length=4096)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    author = models.ForeignKey(to=CustomUser, null=True, on_delete=models.SET_NULL, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=4096)




