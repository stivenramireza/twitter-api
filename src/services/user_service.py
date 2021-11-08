import json

from typing import List

from fastapi import HTTPException

from src.models.user_model import User
from src.repositories import user_repository


def get_all_users() -> List[User]:
    users = user_repository.get_users()
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users


def register_user(user: User) -> User:
    with open("./files/users.json", "r+", encoding="utf-8") as f:
        users = json.loads(f.read())
        user = dict(user)
        user["user_id"] = str(user["user_id"])
        user["birth_date"] = str(user["birth_date"])
        users.append(user)
        f.seek(0)
        f.write(json.dumps(users))
        return user
