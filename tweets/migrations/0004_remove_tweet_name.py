# Generated by Django 5.0 on 2023-12-22 06:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tweets", "0003_alter_tweet_created_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tweet",
            name="name",
        ),
    ]