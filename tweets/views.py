from django.shortcuts import render, redirect


def tweets_index(request):
    return render(request, "tweets_index.html")
