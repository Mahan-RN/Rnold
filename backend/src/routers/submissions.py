from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from src.database import get_db
from src.dependency import CurrentAdmin, CurrentUser
from src.exceptions.submission_exceptions import SubmissionNotFoundError
from src.models import Submission
from src.schemas.submission import CreateSubmissionRequest, SubmissionResponse
from src.services import submission_services

router = APIRouter(prefix="/submissions", tags=["submissions"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get("", response_model=list[SubmissionResponse])
def get_submissions(session: DbSession, admin: CurrentAdmin) -> Sequence[Submission]:
    return submission_services.get_all(session)


@router.get("/{problem_id}/me", response_model=list[SubmissionResponse])
def get_user_submissions_per_problem(
    problem_id: int, session: DbSession, user: CurrentUser
) -> Sequence[Submission]:
    user_id = user.github_id
    result = submission_services.get_per_problem_per_user(user_id, problem_id, session)
    return result


@router.get(
    "/{submission_id}", responses={404: {"description": "Submission not found"}}
)
def get_submission(
    submission_id: int, session: DbSession, admin: CurrentAdmin
) -> Submission:
    try:
        submission = submission_services.get_one(submission_id, session)
        return submission
    except SubmissionNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("", response_model=SubmissionResponse)
def add_submission(
    request: CreateSubmissionRequest, session: DbSession, user: CurrentUser
) -> Submission:
    result = submission_services.insert_one(**request.model_dump(), session=session)
    session.commit()
    return result


@router.delete(
    "/{submission_id}", responses={404: {"description": "Submission not found"}}
)
def delete_submission(
    submission_id: int, session: DbSession, admin: CurrentAdmin
) -> Response:
    try:
        submission_services.delete_one(submission_id, session)
        session.commit()
        return Response(status.HTTP_204_NO_CONTENT)
    except SubmissionNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))
