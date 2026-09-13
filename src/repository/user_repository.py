from collections.abc import Sequence
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models import User, Role


def get_one(github_id: int, session: Session) -> User | None:
    return session.get(User, github_id)


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
    session.flush()
    return user


def update_one(
    github_id: int,
    session: Session,
    github_email: str | None = None,
    username: str | None = None,
) -> User | None:
    user = session.get(User, github_id)
    if user is None:
        return None
    if github_email is not None:
        user.github_email = github_email
    if username is not None:
        user.username = username
    return user


def delete_one(github_id: int, session: Session) -> None:
    user: User | None = session.get(User, github_id)
    if user is not None:
        if user.role == Role.USER:
            session.delete(user)
            session.flush()
        else:
            results = session.query(User).where(User.role == Role.ADMIN).all()
            if len(results) > 1:
                session.delete(user)
                session.flush()
            else:
                return None
