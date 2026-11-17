import json
from pathlib import Path

from pydantic import TypeAdapter
from sqlalchemy.orm import Session

from src.exceptions.topic_exceptions import TopicNotFoundError
from src.exceptions.topic_parser_exceptions import InvalidTopicTemplateFormatError
from src.schemas.topic import CreateTopicRequest
from src.services import topic_services


def load_topic_data(session: Session, path: Path) -> None:
    parsed_topics = _read_json(path)
    _write_parser_output_to_db(parsed_topics, session)

    session.commit()


def _read_json(path: Path) -> list[CreateTopicRequest]:
    with open(path, "r") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise InvalidTopicTemplateFormatError(
            "Topics file must be a list of JSON entries"
        )

    try:
        return TypeAdapter(list[CreateTopicRequest]).validate_python(data)
    except ValueError as e:
        raise InvalidTopicTemplateFormatError("Invalid topics file format") from e


def _write_parser_output_to_db(
    parser_output: list[CreateTopicRequest], session: Session
) -> None:
    for topic in parser_output:
        try:
            existing_topic = topic_services.get_by_name(topic.name, session)
            topic_services.update_one(
                id=existing_topic.id,
                name=topic.name,
                description=topic.description,
                sort_order=topic.sort_order,
                session=session,
            )
        except TopicNotFoundError:
            topic_services.insert_one(
                name=topic.name,
                description=topic.description,
                sort_order=topic.sort_order,
                session=session,
            )
