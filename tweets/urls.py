from django.urls import path
from tweets.views import tweets_index, tweets_new

urlpatterns = [
    path("", tweets_index, name="tweets_index"),
    path("new", tweets_new, name="tweets_index"),
]
