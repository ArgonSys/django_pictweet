from django.shortcuts import render
from django.contrib.auth.views import LoginView as LoginBaseView
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate

from .forms import LoginForm, SignupForm


class SignupView(CreateView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return response


class LoginView(LoginBaseView):
    redirect_authenticated_user = True
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = "/"
