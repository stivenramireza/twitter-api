from typing import List, Dict

from fastapi import APIRouter
from fastapi import status

from src.main import app
from src.models.user_model import User


router = APIRouter(tags=["Users"])


@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a USER",
)
def signup() -> Dict[str, any]:
    pass


@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
)
def login() -> Dict[str, any]:
    pass


@router.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
)
def show_all_users() -> Dict[str, any]:
    pass


@router.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user",
)
def show_user() -> Dict[str, any]:
    pass


@router.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"],
)
def update_user() -> Dict[str, any]:
    pass


@router.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
)
def delete_user() -> Dict[str, any]:
    pass
