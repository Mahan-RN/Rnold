from collections.abc import Sequence

from sqlalchemy import exc, select
from sqlalchemy.orm import Session

from src.exceptions.repository_exceptions import ConflictError, NotFoundError
from src.models import Topic


def get_one(id: int, session: Session) -> Topic:
    result = session.get(Topic, id)
    if result is None:
        raise NotFoundError(f"Topic with ID {id} not found")

    return result


def get_by_name(name: str, session: Session) -> Topic:
    stmt = select(Topic).where(Topic.name == name)
    topic = session.scalars(stmt).one_or_none()
    if topic is None:
        raise NotFoundError(f"Topic with ID {id} not found")

    return topic


def get_all(session: Session) -> Sequence[Topic]:
    stmt = select(Topic).order_by(Topic.sort_order)
    return session.scalars(stmt).all()


def insert_one(
    *, name: str, description: str, sort_order: int, session: Session
) -> Topic:
    topic = Topic(name, description, sort_order)
    session.add(topic)
    try:
        session.flush()
    except exc.IntegrityError as e:
        session.rollback()
        raise ConflictError("Failed to insert topic") from e

    return topic


def update_one(
    *,
    id: int,
    name: str | None = None,
    description: str | None = None,
    sort_order: int | None = None,
    session: Session,
) -> Topic:
    topic = get_one(id, session)

    if name is not None:
        topic.name = name
    if description is not None:
        topic.description = description
    if sort_order is not None:
        topic.sort_order = sort_order
    try:
        session.flush()
    except exc.IntegrityError as e:
        session.rollback()
        raise ConflictError("Failed to update topic") from e

    return topic


def delete_one(id: int, session: Session) -> None:
    result = get_one(id, session)

    session.delete(result)
    session.flush()
