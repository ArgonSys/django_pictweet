from django.shortcuts import render
from django.contrib.auth.views import LoginView as LoginBaseView
from django.views.generic import CreateView

from .forms import LoginForm, SignupForm


class SignupView(CreateView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = "/"

class LoginView(LoginBaseView):
    redirect_authenticated_user = True
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = "/"
