from collections.abc import Sequence
from src.models import User, Role
from src.schemas.user import PostUser, PutUser
from src.repository import user_repository
from src.exceptions.user_exceptions import UserNotFoundError, LastAdminDeletionError
from sqlalchemy.orm import Session


def get_one(github_id: int, session: Session) -> User | None:
    user = user_repository.get_one(github_id, session)
    if user is None:
        raise UserNotFoundError(f"User with github ID {github_id} not found")
    else:
        return user


def get_all(session: Session) -> Sequence[User]:
    return user_repository.get_all(session)


def insert_one(user: PostUser, session: Session) -> User:
    return user_repository.insert_one(
        user.github_id, user.github_email, user.username, session, user.role
    )


def update_one(user: PutUser, session: Session) -> User | None:
    result = user_repository.update_one(user.github_id, session, username=user.username)
    if result is None:
        raise UserNotFoundError(f"User with github ID {user.github_id} not found")
    else:
        return result


def delete_one(github_id: int, session: Session) -> None:
    user = user_repository.get_one(github_id, session)
    if user is None:
        raise UserNotFoundError(f"User with github ID {github_id} not found")
    elif user.role == Role.USER:
        user_repository.delete_one(user.github_id, session)
    else:
        users = list(user_repository.get_all(session))
        admins = list(filter(lambda user: user.role == Role.ADMIN, users))
        if len(admins) > 1:
            user_repository.delete_one(user.github_id, session)
        else:
            raise LastAdminDeletionError("Last admin cannot be deleted")
