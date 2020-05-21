from django.db import models
from accounts.models import CustomUser


class Chat(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    members = models.ManyToManyField(
        CustomUser,
        related_name='chats',
        related_query_name='chats',
        verbose_name='Участники беседы',
        )

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Автор')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Беседа')
    text = models.TextField(max_length=4096, verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return str(self.pub_date) + "|" + self.author.username + ": " + self.text

