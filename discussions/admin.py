from django.contrib import admin
from discussions.models import *


@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('movie',)
    search_fields = ('movie',)
    ordering = ('movie',)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('discussion', 'title',)
    search_fields = ('discussion__movie__name', 'title',)
    ordering = ('discussion',)
    list_filter = ('discussion', )
