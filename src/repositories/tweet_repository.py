import json

from typing import List, Dict


def get_tweets() -> List[Dict[str, any]]:
    with open("./files/tweets.json", "r+", encoding="utf-8") as f:
        tweets = json.loads(f.read())
        return tweets
