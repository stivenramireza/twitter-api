import json

from typing import List

from fastapi import HTTPException

from src.models.tweet_model import Tweet
from src.models.user_model import UserRegister
from src.repositories import tweet_repository


def get_all_tweets() -> List[Tweet]:
    tweets = tweet_repository.get_tweets()
    if not tweets:
        raise HTTPException(status_code=404, detail="Tweets not found")
    return tweets


def post_tweet(tweet: Tweet) -> Tweet:
    with open("./files/tweets.json", "r+", encoding="utf-8") as f:
        tweets = json.loads(f.read())
        tweet = dict(tweet)
        tweet["tweet_id"] = str(tweet["tweet_id"])
        tweet["created_at"] = str(tweet["created_at"])
        tweet["updated_at"] = str(tweet["updated_at"])
        tweet["by"] = dict(tweet["by"])
        tweet["by"]["user_id"] = str(tweet["by"]["user_id"])
        tweet["by"]["birth_date"] = str(tweet["by"]["birth_date"])
        tweets.append(tweet)
        f.seek(0)
        f.write(json.dumps(tweets))
        return tweet
