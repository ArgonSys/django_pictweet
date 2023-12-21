from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from tweets.models import Tweet
from tweets.forms import TweetForm


def tweets_index(request):
    tweets = Tweet.objects.all()
    tweets = __sanitize_image_all(tweets)
    return render(request, "tweets_index.html", {"tweets": tweets})


@login_required
def tweets_new(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("tweets:index")
    else:
        form = TweetForm
    return render(request, "tweets_new.html", {"form": form})


@login_required
@require_POST
def tweets_delete(request, id):
    tweet = get_object_or_404(Tweet, pk=id)
    tweet.delete()
    return redirect("tweets:index")


@login_required
def tweets_edit(request, id):
    tweet = get_object_or_404(Tweet, pk=id)
    if request.method == "POST":
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid:
            form.save()
            return redirect("tweets:index")
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweets_edit.html", {"form": form})


def tweets_show(request, id):
    tweet = get_object_or_404(Tweet, pk=id)
    tweet = __sanitize_image(tweet)
    return render(request, "tweets_show.html", {"tweet": tweet})


###  general methods ###

def __sanitize_image_all(tweets):
    for tweet in tweets:
        tweet = __sanitize_image(tweet)
    return tweets


def __sanitize_image(tweet):
    tweet.image = tweet.image or ""
    return tweet
