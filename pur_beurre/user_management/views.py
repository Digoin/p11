from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, views

from .forms import SignUpForm, LoginForm


User = get_user_model()

class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

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
