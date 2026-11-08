from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Topic
from src.dependency import CurrentAdmin

from src.services import topic_services
from src.exceptions.topic_exceptions import TopicNotFoundError, TopicConflictError
from src.schemas.topic import TopicResponse, UpdateTopicRequest, CreateTopicRequest

router = APIRouter(prefix="/topics", tags=["topics"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get("", response_model=list[TopicResponse])
def get_topics(session: DbSession) -> Sequence[Topic]:
    return topic_services.get_all(session)


@router.get(
    "/{topic_id}",
    response_model=TopicResponse,
    responses={404: {"description": "Topic ID not found"}},
)
def get_topic(topic_id: int, session: DbSession) -> Topic:
    try:
        return topic_services.get_one(topic_id, session)
    except TopicNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))


@router.patch(
    "/{topic_id}",
    response_model=TopicResponse,
    responses={
        404: {"description": "Topic ID not found"},
        409: {"description": "Topic name already exists"},
    },
)
def update_topic(
    topic_id: int, request: UpdateTopicRequest, session: DbSession, admin: CurrentAdmin
) -> Topic:
    try:
        result = topic_services.update_one(
            id=topic_id, **request.model_dump(), session=session
        )
        session.commit()
        return result
    except TopicNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))
    except TopicConflictError as e:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(e))


@router.post(
    "",
    response_model=TopicResponse,
    responses={409: {"description": "Topic name already exists"}},
)
def add_topic(
    request: CreateTopicRequest, session: DbSession, admin: CurrentAdmin
) -> Topic:
    try:
        result = topic_services.insert_one(**request.model_dump(), session=session)
        session.commit()
        return result
    except TopicConflictError as e:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(e))


@router.delete(
    "/{topic_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"description": "Topic ID not found"}},
)
def delete_topic(topic_id: int, session: DbSession, admin: CurrentAdmin) -> Response:
    try:
        topic_services.delete_one(topic_id, session)
        session.commit()
        return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
    except TopicNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))
