from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Tweet
from .forms import TweetForm, SearchForm
from .utils import sanitize_image, sanitize_image_all

from comments.forms import CommentForm


def tweets_index(request):
    tweets = sanitize_image_all(Tweet.objects.prefetch_related("created_by"))
    form = SearchForm
    if request.method == "POST":
        keyword = request.POST["keyword"]
        print(f"keyword: {keyword}")
        if keyword:
            tweets = tweets.filter(text__icontains=keyword)
            form = SearchForm(request.POST)
    template = "tweets/index.html"
    context = {"tweets": tweets, "template": template, "form": form}
    return render(request, "tweets/index.html", context)


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
    tweet = sanitize_image(get_object_or_404(Tweet, pk=id))
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.created_by = request.user
            comment.created_in = tweet
            comment.save()
            return redirect("tweets:show", pk=id)
    else:
        form = CommentForm
    template = "tweets/show.html"
    comments = tweet.comment_set.prefetch_related("created_by")
    context = {"tweet": tweet, "template": template, "comments": comments, "form": form}
    return render(request, "tweets/show.html", context)
