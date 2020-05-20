from django.urls import path

from . import views
app_name = 'movies'

urlpatterns = [
    path('<int:page>', views.MoviesListView.as_view(), name='movies_list'),
    path('add_movie/', views.MovieCreateView.as_view(), name='add_movie'),
    path('movie/<int:id>', views.MovieDetailView.as_view(), name='movie_details'),
    path('watch/<int:movie_id>/<int:season>/<int:number>', views.EpisodeDetailView.as_view(), name='watch_episode'),
    path('add_episode/', views.EpisodeCreateView.as_view(), name='add_episode'),
]
