from django.shortcuts import render, redirect


def top(request):
    return redirect("tweets_index")
