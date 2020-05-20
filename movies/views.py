from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from movies.forms import MovieCreateForm
from movies.models import Movie


class MoviesListView(ListView):
    template_name = 'movies/movies_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        movies = Movie.objects.all()
        paginator = Paginator(movies, 3)
        page_num = self.kwargs['page']
        page = paginator.page(page_num)
        print(page.has_next())
        return page


class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = 'movies/movie_create.html'
    model = Movie
    success_url = reverse_lazy('accounts:root')
    form_class = MovieCreateForm

