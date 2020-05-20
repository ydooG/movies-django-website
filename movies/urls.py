from django.urls import path

from . import views
app_name = 'movies'

urlpatterns = [
    path('<int:page>', views.MoviesListView.as_view(), name='movies_list'),
    path('add_movie/', views.MovieCreateView.as_view(), name='add_movie'),
]
