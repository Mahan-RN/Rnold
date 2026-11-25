from collections.abc import Sequence

from sqlalchemy import exc, select
from sqlalchemy.orm import Session

from src.exceptions.repository_exceptions import ConflictError, NotFoundError
from src.models import Submission


def get_one(id: int, session: Session) -> Submission:
    submission = session.get(Submission, id)
    if submission is None:
        raise NotFoundError(f"Submission with ID {id} not found")

    return submission


def get_all(session: Session) -> Sequence[Submission]:
    stmt = select(Submission).order_by(Submission.created_at.desc())
    return session.scalars(stmt).all()


def get_per_problem_per_user(
    user_id: int, problem_id: int, session: Session
) -> Sequence[Submission]:
    stmt = (
        select(Submission)
        .where(Submission.user_id == user_id, Submission.problem_id == problem_id)
        .order_by(Submission.created_at.desc())
    )
    return session.scalars(stmt).all()


def get_completed_problems_per_user(user_id: int, session: Session) -> Sequence[int]:
    stmt = (
        select(Submission.problem_id)
        .where(Submission.user_id == user_id, Submission.accepted == True)
        .distinct()
    )

    return session.scalars(stmt).all()


def get_problem_status_per_user(
    user_id: int, problem_id: int, session: Session
) -> bool:
    stmt = select(Submission.accepted).where(
        Submission.user_id == user_id,
        Submission.problem_id == problem_id,
        Submission.accepted == True,
    )
    results = session.scalars(stmt).all()
    return len(results) > 0


def insert_one(
    *,
    user_id: int,
    problem_id: int,
    accepted: bool,
    session: Session,
) -> Submission:
    submission = Submission(
        user_id=user_id,
        problem_id=problem_id,
        accepted=accepted,
    )
    session.add(submission)
    try:
        session.flush()
    except exc.IntegrityError as e:
        session.rollback()
        raise ConflictError("Failed to insert submission") from e
    return submission


def delete_one(id: int, session: Session) -> None:
    submission = get_one(id, session)

    session.delete(submission)
    session.flush()
