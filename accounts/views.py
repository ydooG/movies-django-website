from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from accounts.forms import UserRegistrationForm, UserLoginForm
from accounts.models import CustomUser


def root(request):
    return render(request, 'accounts/root.html')


class UserRegistrationView(CreateView):

    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:root')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:root')
    authentication_form = AuthenticationForm


class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])

