from django.shortcuts import render

from accounts.forms import UserRegistrationForm


def root(request):
    return render(request, 'accounts/root.html')


def register(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})
