from collections.abc import Sequence

from sqlalchemy.orm import Session

from src.exceptions.repository_exceptions import ConflictError, NotFoundError
from src.exceptions.user_exceptions import (
    LastAdminDeletionError,
    UserConflictError,
    UserNotFoundError,
)
from src.models import Role, User
from src.repository import user_repository


def get_one(github_id: int, session: Session) -> User:
    try:
        user = user_repository.get_one(github_id, session)
    except NotFoundError as e:
        raise UserNotFoundError from e

    return user


def get_all(session: Session) -> Sequence[User]:
    return user_repository.get_all(session)


def insert_one(
    *,
    github_id: int,
    github_email: str,
    username: str,
    role: Role = Role.USER,
    session: Session,
) -> User:
    try:
        result = user_repository.insert_one(
            github_id=github_id,
            github_email=github_email,
            username=username,
            role=role,
            session=session,
        )
    except ConflictError as e:
        raise UserConflictError from e

    return result


def update_one(
    github_id: int,
    session: Session,
    role: Role | None = None,
    username: str | None = None,
) -> User:
    try:
        result = user_repository.update_one(github_id, session, username, role)
    except NotFoundError as e:
        raise UserNotFoundError from e
    except ConflictError as e:
        raise UserConflictError from e

    return result


def delete_one(github_id: int, session: Session) -> None:
    try:
        user = user_repository.get_one(github_id, session)
    except NotFoundError as e:
        raise UserNotFoundError from e

    if user.role == Role.USER:
        try:
            user_repository.delete_one(user.github_id, session)
        except NotFoundError as e:
            raise UserNotFoundError from e
    else:
        users = list(user_repository.get_all(session))
        admins = list(filter(lambda user: user.role == Role.ADMIN, users))
        if len(admins) > 1:
            try:
                user_repository.delete_one(user.github_id, session)
            except NotFoundError as e:
                raise UserNotFoundError from e
        else:
            raise LastAdminDeletionError("Last admin cannot be deleted")
