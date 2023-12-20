from django.db import models

class Tweet(models.Model):
    name = models.CharField("名前", max_length=128)
    text = models.CharField("本文", max_length=256)
    image = models.CharField("画像URL", max_length=512, blank=True, null=True)
    created_at = models.DateTimeField("投稿日時", auto_now_add=True)
    updated_at = models.DateTimeField("投稿日時", auto_now=True)

    class Meta:
        db_table = "tweets"

    def __str__(self):
        return f"{ self.pk } { self.text }"
