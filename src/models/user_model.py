from uuid import UUID
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(..., example="stivenramireza@gmail.com")


class UserPassword(BaseModel):
    password: str = Field(..., min_length=8, example="stivenramireza")


class User(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50, example="Stiven")
    last_name: str = Field(..., min_length=1, max_length=50, example="Ramírez Arango")
    birth_date: Optional[date] = Field(default=None, example="1998-08-13")


class UserLogin(UserBase, UserPassword):
    pass


class UserRegister(User, UserPassword):
    pass
