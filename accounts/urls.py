from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', views.root, name='root'),
    path('register/', views.register, name='register'),
    #path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView, name='logout'),
    #path('profile/<slug:username>', views, name='profile')
]
