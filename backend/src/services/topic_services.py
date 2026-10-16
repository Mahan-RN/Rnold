from collections.abc import Sequence
from sqlalchemy.orm import Session
from src.models import Topic
from src.repository import topic_respository
from src.exceptions.topic_exceptions import TopicNotFoundError, DuplicateTitleError


def get_one(id: int, session: Session) -> Topic:
    result = topic_respository.get_one(id, session)
    if result is None:
        raise TopicNotFoundError(f"Topic with ID {id} not found")
    else:
        return result


def get_all(session: Session) -> Sequence[Topic]:
    return topic_respository.get_all(session)


def insert_one(
    *, name: str, description: str, sort_order: int, session: Session
) -> Topic:
    result = session.query(Topic).filter(Topic.name == name).all()
    if len(result) != 0:
        raise DuplicateTitleError(f"Topic with name `{name}` already exists")
    else:
        return topic_respository.insert_one(
            name=name,
            description=description,
            sort_order=sort_order,
            session=session,
        )


def update_one(
    *,
    id: int,
    name: str | None = None,
    description: str | None = None,
    sort_order: int | None = None,
    session: Session,
) -> Topic:
    name_exists = session.query(Topic).filter(Topic.name == name, Topic.id != id).all()
    if name_exists:
        raise DuplicateTitleError(f"Topic with name `{name}` already exists")
    else:
        result = topic_respository.update_one(
            id=id,
            name=name,
            description=description,
            sort_order=sort_order,
            session=session,
        )
        if result is None:
            raise TopicNotFoundError(f"Topic with ID {id} not found")
        else:
            return result


def delete_one(id: int, session: Session) -> None:
    result = topic_respository.get_one(id, session)
    if result is None:
        raise TopicNotFoundError(f"Topic with ID {id} not found")
    else:
        topic_respository.delete_one(id, session)
