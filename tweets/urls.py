from django.urls import path
from tweets.views import tweets_index

urlpatterns = [
    path("", tweets_index, name="tweets_index"),
]
