from collections.abc import Sequence
from src.models import TestCase
from sqlalchemy.orm import Session
from sqlalchemy import select


def get_one(id: int, session: Session) -> TestCase | None:
    return session.get(TestCase, id)


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
    session.flush()
    return test_case


def update_one(
    *,
    id: int,
    session: Session,
    problem_id: int | None = None,
    sort_order: int | None = None,
    code: str | None = None,
) -> TestCase | None:
    test_case = session.get(TestCase, id)
    if test_case is None:
        return None
    else:
        if problem_id is not None:
            test_case.problem_id = problem_id
        if sort_order is not None:
            test_case.sort_order = sort_order
        if code is not None:
            test_case.code = code
        session.flush()
        return test_case


def delete_one(id: int, session: Session) -> None:
    test_case = session.get(TestCase, id)
    if test_case is not None:
        session.delete(test_case)
        session.flush()
