from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView as LoginBaseView
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate

from .models import User
from .forms import LoginForm, SignupForm
from tweets.utils import sanitize_image_all

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


class UsersView(View):
    template_name = "users/show.html"

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs["id"])
        tweets = user.tweet_set.all()
        tweets = sanitize_image_all(tweets)
        return render(request, self.template_name, {"user": user, "tweets": tweets})
