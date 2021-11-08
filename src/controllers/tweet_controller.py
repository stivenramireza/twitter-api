from typing import List, Dict

from fastapi import APIRouter
from fastapi import status

from src.models.tweet_model import Tweet
from src.services import tweet_service


router = APIRouter(prefix="/tweets", tags=["Tweets"])


@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
)
def show_all_tweets() -> Dict[str, any]:
    tweets = tweet_service.get_all_tweets()
    return tweets


@router.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
)
def post(tweet: Tweet) -> Dict[str, any]:
    posted_tweet = tweet_service.post_tweet(tweet)
    return posted_tweet


@router.get(
    path="/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
)
def show_tweet() -> None:
    pass


@router.put(
    path="/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
)
def update_tweet() -> None:
    pass


@router.delete(
    path="/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
)
def delete_tweet() -> None:
    pass
