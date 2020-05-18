from django.db import models
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
    # ToDo: change SET_NULL to SET_DEFAULT
    reply_to = models.OneToOneField(to='self', null=True, blank=True, on_delete=models.SET_NULL)
    text = models.TextField(max_length=4096)




