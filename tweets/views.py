from django.shortcuts import render, redirect

from tweets.models import Tweet

def tweets_index(request):
    tweets = Tweet.objects.all()
    return render(request, "tweets_index.html", {"tweets": tweets})
