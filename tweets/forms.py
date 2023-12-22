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


class SearchForm(forms.Form):
    keyword = forms.CharField(
        label="keyword",
        max_length=128,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "投稿を検索する",
            "class": "search-input",
        }))
