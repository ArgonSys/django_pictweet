from django.db import models
from django.conf import settings


class TweetManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("-created_at")


class Tweet(models.Model):
    text = models.TextField("本文")
    image = models.CharField("画像URL", max_length=512, blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="投稿者",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField("投稿日時", auto_now_add=True)
    updated_at = models.DateTimeField("投稿日時", auto_now=True)

    objects = TweetManager()

    class Meta:
        db_table = "tweets"

    def __str__(self):
        return f"{ self.pk } { self.text }"
