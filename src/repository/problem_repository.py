from collections.abc import Sequence
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import Problem, Topic


def get_one(id: int, session: Session) -> Problem | None:
    return session.get(Problem, id)


def get_all(session: Session) -> Sequence[Problem]:
    stmt = (
        select(Problem)
        .join(Topic, Problem.topic_id == Topic.id)
        .order_by(Topic.sort_order, Problem.sort_order)
    )
    return session.scalars(stmt).all()


def insert_one(
    *,
    topic_id: int,
    sort_order: int,
    title: str,
    description: str,
    difficulty: int,
    starter_code: str,
    session: Session,
) -> Problem:
    problem = Problem(
        topic_id=topic_id,
        sort_order=sort_order,
        title=title,
        description=description,
        difficulty=difficulty,
        starter_code=starter_code,
    )
    session.add(problem)
    session.flush()
    return problem


def update_one(
    *,
    id: int,
    topic_id: int | None = None,
    sort_order: int | None = None,
    title: str | None = None,
    description: str | None = None,
    difficulty: int | None = None,
    starter_code: str | None = None,
    session: Session,
) -> Problem | None:
    problem = session.get(Problem, id)
    if problem is None:
        return None
    if topic_id is not None:
        problem.topic_id = topic_id
    if sort_order is not None:
        problem.sort_order = sort_order
    if title is not None:
        problem.title = title
    if description is not None:
        problem.description = description
    if difficulty is not None:
        problem.difficulty = difficulty
    if starter_code is not None:
        problem.starter_code = starter_code
    session.flush()
    return problem


def delete_one(id: int, session: Session) -> None:
    problem: Problem | None = session.get(Problem, id)
    if problem is not None:
        session.delete(problem)
        session.flush()
