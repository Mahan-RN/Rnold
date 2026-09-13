from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import User, Role
from src.schemas.user import GetUser
from src.dependency import CurrentUser, logout
from src.services import user_services
from src.exceptions.user_exceptions import UserNotFoundError, LastAdminDeletionError

router = APIRouter(prefix="/users", tags=["users"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get(
    "",
    response_model=list[GetUser],
    responses={403: {"description": "Access requires admin status"}},
)
def get_users(db: DbSession, current_user: CurrentUser) -> Sequence[User]:
    if current_user.role == Role.USER:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Access requires admin status")
    else:
        return user_services.get_all(db)


@router.get(
    "/me",
    response_model=GetUser,
    responses={404: {"description": "User not found"}},
)
def get_user(db: DbSession, current_user: CurrentUser) -> User:
    try:
        user = user_services.get_one(current_user.github_id, db)
        return user
    except UserNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete(
    "/me",
    responses={
        404: {"description": "User not found"},
        403: {"description": "Last admin cannot be deleted"},
    },
)
def delete_user(db: DbSession, current_user: CurrentUser, request: Request) -> Response:
    try:
        user_services.delete_one(current_user.github_id, db)
        logout(request)
    except UserNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))
    except LastAdminDeletionError as e:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail=str(e))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
