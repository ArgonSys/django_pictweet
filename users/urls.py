from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


app_name = "users"

urlpatterns = [
    path("login", LoginView.as_view(
        redirect_authenticated_user=True,
        template_name="users/login.html"
    ), name="login"),
]
