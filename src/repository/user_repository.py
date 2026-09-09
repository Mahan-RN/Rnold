from collections.abc import Sequence
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models import User


def get_one(github_id: int, session: Session) -> User | None:
    return session.get(User, github_id)


def get_all(session: Session) -> Sequence[User]:
    stmt = select(User).order_by(User.username)
    return session.scalars(stmt).all()


def insert_one(
    github_id: int, github_email: str, username: str, session: Session
) -> User:
    user = User(github_id, github_email, username)
    session.add(user)
    session.flush()
    return user


def update_one(
    github_id: int, github_email: str | None, username: str | None, session: Session
) -> User:
    user = session.get(User, github_id)
    if user is None:
        raise Exception(f"User with github ID {github_id} not found")
    if github_email is not None:
        user.github_email = github_email
    if username is not None:
        user.username = username
    return user


def delete_one(github_id: int, session: Session) -> None:
    user = session.get(User, github_id)
    session.delete(user)
