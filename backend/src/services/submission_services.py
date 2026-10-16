from src.models import Submission
from src.repository import submission_repository
from src.exceptions.submission_exceptions import SubmissionNotFoundError
from collections.abc import Sequence
from sqlalchemy.orm import Session


def get_one(id: int, session: Session) -> Submission:
    result = submission_repository.get_one(id, session)
    if result is None:
        raise SubmissionNotFoundError(f"Submission with ID {id} not found")
    else:
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
    runtime_ms: int,
    code: str,
    session: Session,
) -> Submission:
    return submission_repository.insert_one(
        user_id=user_id,
        problem_id=problem_id,
        status=status,
        runtime_ms=runtime_ms,
        code=code,
        session=session,
    )


def delete_one(id: int, session: Session) -> None:
    result = submission_repository.get_one(id, session)
    if result is None:
        raise SubmissionNotFoundError(f"Submission with ID {id} not found")
    else:
        submission_repository.delete_one(id, session)
