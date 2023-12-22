from django.db import models
from users.models import User
from tweets.models import Tweet


class Comment(models.Model):
    text = models.CharField(max_length=128)
    created_by = models.ForeignKey(
        User,
        verbose_name="投稿者",
        on_delete=models.CASCADE
    )
    created_in = models.ForeignKey(
        Tweet,
        verbose_name="ツイート",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return f"{self.pk} {self.text}"
