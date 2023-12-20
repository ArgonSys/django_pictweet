from django.shortcuts import render, redirect

from tweets.models import Tweet

def tweets_index(request):
    context = {"tweets": __sanitize_image(Tweet.objects.all())}
    return render(request, "tweets_index.html", context)


def tweets_new(request):
    return render(request, "tweets_new.html")


def __sanitize_image(tweets):
    for tweet in tweets:
        tweet.image = tweet.image or ""
    return tweets
