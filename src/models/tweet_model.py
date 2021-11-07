from uuid import UUID
from datetime import datetime

from pydantic import BaseModel

from src.models import user_model


class Tweet(BaseModel):
    tweet_id = UUID = Field(...)
    content: str = Field(..., min_length=1, max_length=256)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())
    by: user_model.User = Field(...)
