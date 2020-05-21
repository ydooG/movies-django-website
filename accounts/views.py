from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, FormView

from accounts.forms import UserRegistrationForm, UserPhotoLoadForm
from accounts.models import CustomUser


def root(request):
    if request.method == 'GET':
        return render(request, 'accounts/root.html')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', ])


class UserRegistrationView(CreateView):

    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:root')

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:root')
    authentication_form = AuthenticationForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo'] = self.request.user.profile_photo
        return context


class AddUserPhotoView(LoginRequiredMixin, FormView):
    template_name = 'accounts/photo_load.html'
    form_class = UserPhotoLoadForm
    success_url = reverse_lazy('accounts:root')

    def form_valid(self, form):
        curr_user = self.request.user
        if curr_user.profile_photo:
            curr_user.profile_photo.delete()
        curr_user.profile_photo = self.request.FILES['photo']
        curr_user.save()
        return HttpResponseRedirect(self.success_url)
