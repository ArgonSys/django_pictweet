from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

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


@require_POST
def tweets_delete(request, id):
    tweet = get_object_or_404(Tweet, pk=id)
    tweet.delete()
    return redirect("tweets:index")


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




def __sanitize_image(tweets):
    for tweet in tweets:
        tweet.image = tweet.image or ""
    return tweets
