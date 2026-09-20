from collections.abc import Sequence
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import Topic


def get_one(id: int, session: Session) -> Topic | None:
    result = session.get(Topic, id)
    return result


def get_all(session: Session) -> Sequence[Topic]:
    stmt = select(Topic).order_by(Topic.sort_order)
    return session.scalars(stmt).all()


def insert_one(
    *, name: str, description: str, sort_order: int, session: Session
) -> Topic:
    topic = Topic(name, description, sort_order)
    session.add(Topic)
    session.flush()
    return topic


def update_one(
    *,
    id: int,
    name: str | None = None,
    description: str | None = None,
    sort_order: int | None = None,
    session: Session,
) -> Topic | None:
    topic = session.get(Topic, id)
    if topic is None:
        return None
    else:
        if name is not None:
            topic.name = name
        if description is not None:
            topic.description = description
        if sort_order is not None:
            topic.sort_order = sort_order
        session.flush()
        return topic


def delete_one(id: int, session: Session) -> None:
    result: Topic | None = session.get(Topic, id)
    if result is not None:
        session.delete(result)
        session.flush()
