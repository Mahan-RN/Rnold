from collections.abc import Sequence

from sqlalchemy.orm import Session

from src.exceptions.repository_exceptions import ConflictError, NotFoundError
from src.exceptions.submission_exceptions import (
    SubmissionConflictError,
    SubmissionNotFoundError,
)
from src.models import Submission
from src.repository import submission_repository


def get_one(id: int, session: Session) -> Submission:
    try:
        result = submission_repository.get_one(id, session)
    except NotFoundError as e:
        raise SubmissionNotFoundError from e

    return result


def get_per_problem_per_user(
    user_id: int, problem_id: int, session: Session
) -> Sequence[Submission]:
    result = submission_repository.get_per_problem_per_user(
        user_id, problem_id, session
    )
    return result


def get_all(session: Session) -> Sequence[Submission]:
    return submission_repository.get_all(session)


def insert_one(
    *,
    user_id: int,
    problem_id: int,
    status: int,
    session: Session,
) -> Submission:
    try:
        submission = submission_repository.insert_one(
            user_id=user_id,
            problem_id=problem_id,
            status=status,
            session=session,
        )
    except ConflictError as e:
        raise SubmissionConflictError from e

    return submission


def delete_one(id: int, session: Session) -> None:
    try:
        submission_repository.delete_one(id, session)
    except NotFoundError as e:
        raise SubmissionNotFoundError from e
