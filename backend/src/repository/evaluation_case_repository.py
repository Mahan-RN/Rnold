from collections.abc import Sequence

from sqlalchemy import exc, select
from sqlalchemy.orm import Session

from src.exceptions.repository_exceptions import ConflictError, NotFoundError
from src.models import EvaluationCase


def get_one(id: int, session: Session) -> EvaluationCase:
    result = session.get(EvaluationCase, id)
    if result is None:
        raise NotFoundError(f"Test Case with ID {id} not found")

    return result


def get_by_unique_constraint(
    problem_id: int, sort_order: int, session: Session
) -> EvaluationCase:
    stmt = select(EvaluationCase).where(
        EvaluationCase.problem_id == problem_id
        and EvaluationCase.sort_order == sort_order
    )
    evaluation_case = session.scalars(stmt).one_or_none()
    if evaluation_case is None:
        raise NotFoundError(
            f"Test Case with problem ID {problem_id} and sort order {sort_order} not found"
        )

    return evaluation_case


def get_all(session: Session) -> Sequence[EvaluationCase]:
    stmt = select(EvaluationCase).order_by(EvaluationCase.sort_order)
    return session.scalars(stmt).all()


def insert_one(
    *,
    problem_id: int,
    sort_order: int,
    code: str,
    session: Session,
) -> EvaluationCase:
    test_case = EvaluationCase(
        problem_id=problem_id,
        sort_order=sort_order,
        code=code,
    )
    session.add(test_case)
    try:
        session.flush()
    except exc.IntegrityError as e:
        session.rollback()
        raise ConflictError("Failed to insert test case") from e

    return test_case


def update_one(
    *,
    id: int,
    session: Session,
    problem_id: int | None = None,
    sort_order: int | None = None,
    code: str | None = None,
) -> EvaluationCase:
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
