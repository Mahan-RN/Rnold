from collections.abc import Sequence

from sqlalchemy.orm import Session

from src.exceptions.repository_exceptions import ConflictError, NotFoundError
from src.exceptions.topic_exceptions import TopicConflictError, TopicNotFoundError
from src.models import Topic
from src.repository import topic_respository


def get_one(id: int, session: Session) -> Topic:
    try:
        result = topic_respository.get_one(id, session)
    except NotFoundError as e:
        raise TopicNotFoundError from e

    return result


def get_all(session: Session) -> Sequence[Topic]:
    return topic_respository.get_all(session)


def insert_one(
    *, name: str, description: str, sort_order: int, session: Session
) -> Topic:
    try:
        result = topic_respository.insert_one(
            name=name,
            description=description,
            sort_order=sort_order,
            session=session,
        )
    except ConflictError as e:
        raise TopicConflictError from e

    return result


def update_one(
    *,
    id: int,
    name: str | None = None,
    description: str | None = None,
    sort_order: int | None = None,
    session: Session,
) -> Topic:
    try:
        result = topic_respository.update_one(
            id=id,
            name=name,
            description=description,
            sort_order=sort_order,
            session=session,
        )
    except NotFoundError as e:
        raise TopicNotFoundError from e
    except ConflictError as e:
        raise TopicConflictError from e

    return result


def delete_one(id: int, session: Session) -> None:
    try:
        topic_respository.delete_one(id, session)
    except NotFoundError as e:
        raise TopicNotFoundError from e
