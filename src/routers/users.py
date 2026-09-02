from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import User
from src.schemas.user import GetUser

router = APIRouter(prefix="/users", tags=["users"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get("", response_model=list[GetUser])
def get_users(db: DbSession) -> Sequence[User]:
    stmt = select(User).order_by(User.username)
    return db.scalars(stmt).all()


@router.get("/{user_github_id}", response_model=GetUser)
def get_user(user_github_id: str, db: DbSession) -> User:
    user: User | None = db.get(User, user_github_id)
    if user is not None:
        return user
    else:
        raise HTTPException(
            status_code=404,
            detail=f"User with GitHub ID {user_github_id} does not exist",
        )
