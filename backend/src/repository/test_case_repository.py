from collections.abc import Sequence

from sqlalchemy import exc, select
from sqlalchemy.orm import Session

from src.exceptions.repository_exceptions import ConflictError, NotFoundError
from src.models import TestCase


def get_one(id: int, session: Session) -> TestCase:
    result = session.get(TestCase, id)
    if result is None:
        raise NotFoundError(f"Test Case with ID {id} not found")

    return result


def get_all(session: Session) -> Sequence[TestCase]:
    stmt = select(TestCase).order_by(TestCase.sort_order)
    return session.scalars(stmt).all()


def insert_one(
    *,
    problem_id: int,
    sort_order: int,
    code: str,
    session: Session,
) -> TestCase:
    test_case = TestCase(
        problem_id=problem_id,
        sort_order=sort_order,
        code=code,
    )
    session.add(test_case)
    try:
        session.flush()
    except exc.IntegrityError as e:
        session.rollback()
        raise ConflictError("Failed to insert submission") from e

    return test_case


def update_one(
    *,
    id: int,
    session: Session,
    problem_id: int | None = None,
    sort_order: int | None = None,
    code: str | None = None,
) -> TestCase:
    test_case = get_one(id, session)

    if problem_id is not None:
        test_case.problem_id = problem_id
    if sort_order is not None:
        test_case.sort_order = sort_order
    if code is not None:
        test_case.code = code

    try:
        session.flush()
    except exc.IntegrityError as e:
        session.rollback()
        raise ConflictError("Failed to update test case") from e

    return test_case


def delete_one(id: int, session: Session) -> None:
    test_case = get_one(id, session)

    session.delete(test_case)
    session.flush()
