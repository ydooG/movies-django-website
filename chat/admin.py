from django.contrib import admin
from .models import Chat, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'author', 'text', 'pub_date')
    search_fields = ('text', 'author')
    ordering = ('author', 'pub_date', 'chat')
    list_filter = ('chat', 'author')


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
