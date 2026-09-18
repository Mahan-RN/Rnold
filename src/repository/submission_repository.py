from src.models import Submission
from collections.abc import Sequence
from sqlalchemy.orm import Session
from sqlalchemy import select


def get_one(id: int, session: Session) -> Submission | None:
    return session.get(Submission, id)


def get_all(session: Session) -> Sequence[Submission]:
    stmt = select(Submission).order_by(Submission.created_at.desc())
    return session.scalars(stmt).all()


def insert_one(
    *,
    user_id: int,
    problem_id: int,
    status: int,
    runtime_ms: int,
    code: str,
    session: Session,
) -> Submission:
    submission = Submission(
        user_id=user_id,
        problem_id=problem_id,
        status=status,
        runtime_ms=runtime_ms,
        code=code,
    )
    session.add(submission)
    session.flush()
    return submission


def delete_one(id: int, session: Session) -> None:
    submission: Submission | None = session.get(Submission, id)
    if submission is not None:
        session.delete(submission)
        session.flush()
