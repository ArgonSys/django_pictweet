from django import forms

from tweets.models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ("text", "image")
        widgets = {
            "text": forms.Textarea(attrs={"placeholder": "text"}),
            "image": forms.TextInput(attrs={"placeholder": "Image Url"}),
        }
