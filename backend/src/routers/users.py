from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import User
from src.dependency import CurrentUser, CurrentAdmin, logout
from src.services import user_services
from src.exceptions.user_exceptions import UserNotFoundError, LastAdminDeletionError
from src.schemas.user import UpdateUsernameRequest, GetUser, UpdateRoleRequest

router = APIRouter(prefix="/users", tags=["users"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get(
    "",
    response_model=list[GetUser],
    responses={403: {"description": "Access requires admin status"}},
)
def get_users(db: DbSession, current_admin: CurrentAdmin) -> Sequence[User]:
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
        db.commit()
        logout(request)
    except UserNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))
    except LastAdminDeletionError as e:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail=str(e))
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch(
    "/me", response_model=GetUser, responses={404: {"description": "User not found"}}
)
def update_username(
    request: UpdateUsernameRequest, db: DbSession, current_user: CurrentUser
) -> User:
    try:
        user_services.update_one(
            github_id=current_user.github_id,
            session=db,
            role=None,
            username=request.username,
        )
        db.commit()
        updated_user = user_services.get_one(current_user.github_id, db)
        return updated_user
    except UserNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))


@router.patch(
    "/{github_id}/role",
    responses={404: {"description": "User not found"}},
    response_model=GetUser,
)
def update_user_role(
    github_id: int, request: UpdateRoleRequest, db: DbSession, admin: CurrentAdmin
) -> User:
    try:
        user_services.update_one(
            github_id=github_id, session=db, role=request.role, username=None
        )
        db.commit()
        updated_user = user_services.get_one(github_id, db)
        return updated_user
    except UserNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))
