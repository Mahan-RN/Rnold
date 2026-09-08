from typing import Annotated
from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import User


DbSession = Annotated[Session, Depends(get_db)]


def get_current_user(request: Request, db: DbSession) -> User:
    github_id = request.session.get("github_id")
    if github_id is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "not authenticated")

    user = db.get(User, github_id)
    if user is None:
        request.session.pop("github_id")
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "not authenticated")

    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
