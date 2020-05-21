from django.contrib import admin
from movies.models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('movie', 'season', 'number')
    search_fields = ('movie__name',)
    ordering = ('movie', 'season', 'number')
    list_filter = ('movie',)

