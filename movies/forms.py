from django import forms

from movies.models import Movie, Episode
from django_select2 import forms as s2forms


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'movie_picture')


class EpisodeCreateForm(forms.ModelForm):
    movie = forms.ModelChoiceField(
        queryset=Movie.objects.all(),

    )

    class Meta:
        model = Episode
        fields = ('movie', 'number', 'season', 'title', 'video_obj')
