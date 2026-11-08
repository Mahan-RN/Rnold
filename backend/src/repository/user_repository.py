from collections.abc import Sequence

from sqlalchemy import exc, select
from sqlalchemy.orm import Session

from src.exceptions.repository_exceptions import ConflictError, NotFoundError
from src.models import Role, User


def get_one(github_id: int, session: Session) -> User:
    user = session.get(User, github_id)
    if user is None:
        raise NotFoundError(f"User with GitHUb ID {github_id} not found")

    return user


def get_all(session: Session) -> Sequence[User]:
    stmt = select(User).order_by(User.username)
    return session.scalars(stmt).all()


def insert_one(
    github_id: int,
    github_email: str,
    username: str,
    session: Session,
    role: Role = Role.USER,
) -> User:
    user = User(github_id, github_email, username, role)
    session.add(user)
    try:
        session.flush()
    except exc.IntegrityError as e:
        session.rollback()
        raise ConflictError("Faield to insert user") from e

    return user


def update_one(
    github_id: int,
    session: Session,
    username: str | None = None,
    role: Role | None = None,
) -> User:
    user = get_one(github_id, session)

    if username is not None:
        user.username = username
    if role is not None:
        user.role = role

    try:
        session.flush()
    except exc.IntegrityError as e:
        session.rollback()
        raise ConflictError("Failed to update user") from e

    return user


def delete_one(github_id: int, session: Session) -> None:
    user = get_one(github_id, session)
    session.delete(user)
    session.flush()
