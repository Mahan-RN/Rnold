from collections.abc import Sequence

from sqlalchemy.orm import Session

from src.exceptions.problem_exceptions import ProblemConflictError, ProblemNotFoundError
from src.exceptions.repository_exceptions import ConflictError, NotFoundError
from src.models import Problem, TestCase
from src.repository import problem_repository


def get_one(id: int, session: Session) -> Problem:
    try:
        problem = problem_repository.get_one(id, session)
    except NotFoundError as e:
        raise ProblemNotFoundError from e

    return problem


def get_test_cases(problem_id: int, session: Session) -> Sequence[TestCase]:
    try:
        result = problem_repository.get_test_cases(problem_id, session)
    except NotFoundError as e:
        raise ProblemNotFoundError from e

    return result


def get_all(session: Session) -> Sequence[Problem]:
    return problem_repository.get_all(session)


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
    try:
        problem = problem_repository.insert_one(
            topic_id=topic_id,
            sort_order=sort_order,
            title=title,
            description=description,
            difficulty=difficulty,
            starter_code=starter_code,
            session=session,
        )
    except ConflictError as e:
        raise ProblemConflictError from e

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
) -> Problem:
    try:
        result = problem_repository.update_one(
            id=id,
            topic_id=topic_id,
            sort_order=sort_order,
            title=title,
            description=description,
            difficulty=difficulty,
            starter_code=starter_code,
            session=session,
        )
    except NotFoundError as e:
        raise ProblemNotFoundError from e
    except ConflictError as e:
        raise ProblemConflictError from e

    return result


def delete_one(id: int, session: Session) -> None:
    try:
        problem_repository.delete_one(id, session)
    except NotFoundError as e:
        raise ProblemNotFoundError from e
