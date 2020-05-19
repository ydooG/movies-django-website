from django.db import models
from accounts.models import CustomUser


class Chat(models.Model):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(CustomUser, related_name='chats', related_query_name='chats')

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField(max_length=4096)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pub_date) + "|" + self.author.username + ": " + self.text

