from django.urls import path
from tweets.views import tweets_index, tweets_new, tweets_delete, tweets_edit


app_name = "tweets"

urlpatterns = [
    path("", tweets_index, name="index"),
    path("new", tweets_new, name="new"),
    path("<int:id>/delete", tweets_delete, name="delete"),
    path("<int:id>/edit", tweets_edit, name="edit"),
]
