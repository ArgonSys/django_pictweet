from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Tweet
from .forms import TweetForm
from .utils import sanitize_image, sanitize_image_all


def tweets_index(request):
    tweets = Tweet.objects.all()
    tweets = sanitize_image_all(tweets)
    return render(request, "tweets/index.html", {"tweets": tweets})


@login_required
def tweets_new(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid:
            tweet = form.save(commit=False)
            tweet.created_by = request.user
            tweet.save()
            return redirect("tweets:index")
    else:
        form = TweetForm
    return render(request, "tweets/new.html", {"form": form})


@login_required
@require_POST
def tweets_delete(request, id):
    tweet = get_object_or_404(Tweet, pk=id)
    if tweet.created_by_id != request.user.id:
        return HttpResponseForbidden("このツイートの削除は許可されていません")

    tweet.delete()
    return redirect("tweets:index")


@login_required
def tweets_edit(request, id):
    tweet = get_object_or_404(Tweet, pk=id)
    if tweet.created_by_id != request.user.id:
        return HttpResponseForbidden("このツイートの編集は許可されていません")

    if request.method == "POST":
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid:
            form.save()
            return redirect("tweets:index")
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweets/edit.html", {"form": form})


def tweets_show(request, id):
    tweet = get_object_or_404(Tweet, pk=id)
    tweet = sanitize_image(tweet)
    return render(request, "tweets/show.html", {"tweet": tweet})
