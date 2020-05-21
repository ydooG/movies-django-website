from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from movies.forms import MovieCreateForm, EpisodeCreateForm
from movies.models import Movie, Episode


class MoviesListView(ListView):
    template_name = 'movies/movies_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        movies = Movie.objects.all()
        paginator = Paginator(movies, 3)
        page_num = self.kwargs['page']
        page = paginator.page(page_num)
        return page


class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = 'movies/movie_create.html'
    model = Movie
    success_url = reverse_lazy('accounts:root')
    form_class = MovieCreateForm


class MovieDetailView(DetailView):
    template_name = 'movies/movie.html'
    model = Movie
    context_object_name = 'movie'

    def get_object(self, queryset=None):
        return get_object_or_404(Movie, id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curr_movie = self.get_object()
        season_length = Episode.objects.filter(movie=curr_movie).values('season').distinct().count()
        seasons = [i for i in range(1, season_length+1)]
        context['episodes'] = curr_movie.episodes.all()
        context['seasons'] = seasons
        return context


class EpisodeCreateView(LoginRequiredMixin, CreateView):
    form_class = EpisodeCreateForm
    template_name = 'movies/episode_create.html'
    success_url = reverse_lazy('movies:movies_list', args={1})

    def get_initial(self):
        curr_movie = get_object_or_404(Movie, id=self.kwargs['id'])
        return {'movie': curr_movie}


class EpisodeDetailView(DetailView):
    template_name = 'movies/episode.html'
    model = Episode
    context_object_name = 'episode'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Episode,
            movie_id=self.kwargs['movie_id'],
            number=self.kwargs['number'],
            season=self.kwargs['season'],
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curr_episode = kwargs['object']
        if curr_episode.has_next():
            context['next'] = curr_episode.number + 1
        if curr_episode.has_previous():
            context['previous'] = curr_episode.number - 1
        return context

