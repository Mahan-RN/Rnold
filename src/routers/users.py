from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import User, Role
from src.schemas.user import GetUser
from src.dependency import CurrentUser

router = APIRouter(prefix="/users", tags=["users"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get(
    "",
    response_model=list[GetUser],
    responses={403: {"description": "access requires admin status"}},
)
def get_users(db: DbSession, current_user: CurrentUser) -> Sequence[User]:
    if current_user.role == Role.USER:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "access requires admin status")
    else:
        stmt = select(User).order_by(User.username)
        return db.scalars(stmt).all()


@router.get(
    "/{user_github_id}",
    response_model=GetUser,
    responses={404: {"description": "User not found"}},
)
def get_user(user_github_id: str, db: DbSession) -> User:
    user: User | None = db.get(User, user_github_id)
    if user is not None:
        return user
    else:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"User with GitHub ID {user_github_id} does not exist",
        )
