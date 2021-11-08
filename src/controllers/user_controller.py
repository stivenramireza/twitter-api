from typing import List, Dict

from fastapi import APIRouter
from fastapi import status

from src.models.user_model import User, UserRegister
from src.services import user_service
from src.utils.logger import logger


router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a USER",
)
def signup(user: UserRegister) -> Dict[str, any]:
    """
    Signup

    This path operation registers a user in the app

    Parameters:
    - Request body parameter
        - user: UserRegister

    Returns a JSON with the basic user information
    - user_id: UUID
    - email: EmailStr
    - first_name: str
    - last_name: str
    - birth_date: datetime
    """
    registered_user = user_service.register_user(user)
    return registered_user


@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
)
def login() -> Dict[str, any]:
    pass


@router.get(
    path="/",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
)
def show_all_users() -> Dict[str, any]:
    users = user_service.get_all_users()
    return users


@router.get(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user",
)
def show_user() -> Dict[str, any]:
    pass


@router.put(
    path="/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"],
)
def update_user() -> Dict[str, any]:
    pass


@router.delete(
    path="/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
)
def delete_user() -> Dict[str, any]:
    pass
