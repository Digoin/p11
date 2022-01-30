from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm
from django.contrib.auth import get_user_model

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('main_site:home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
