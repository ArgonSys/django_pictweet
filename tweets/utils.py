def sanitize_image_all(tweets):
    for tweet in tweets:
        tweet = sanitize_image(tweet)
    return tweets


def sanitize_image(tweet):
    tweet.image = tweet.image or ""
    return tweet
