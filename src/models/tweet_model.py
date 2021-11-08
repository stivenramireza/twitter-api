from uuid import UUID
from datetime import datetime

from pydantic import BaseModel
from pydantic import Field

from src.models.user_model import User


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ..., min_length=1, max_length=256, example="This is a tweet example"
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
    by: User = Field(...)
