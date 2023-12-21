from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from .forms import LoginForm, SignupForm

app_name = "users"

urlpatterns = [
    path("signup/", CreateView.as_view(
        template_name="users/signup.html",
        form_class=SignupForm,
        success_url="/",
    ), name="signup"),
    path("login/", LoginView.as_view(
        redirect_authenticated_user=True,
        template_name="users/login.html",
        form_class=LoginForm,
        success_url="/",
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

]
