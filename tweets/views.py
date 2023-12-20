from django.shortcuts import render, redirect

from tweets.models import Tweet
from tweets.forms import TweetForm

def tweets_index(request):
    context = {"tweets": __sanitize_image(Tweet.objects.all())}
    return render(request, "tweets_index.html", context)


def tweets_new(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("tweets:index")
    else:
        form = TweetForm
    return render(request, "tweets_new.html", {"form": form})


def __sanitize_image(tweets):
    for tweet in tweets:
        tweet.image = tweet.image or ""
    return tweets
