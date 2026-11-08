from collections.abc import Sequence
from src.models import TestCase
from src.repository import test_case_repository
from src.exceptions.test_case_exceptions import (
    TestCaseNotFoundError,
    TestCaseConflictError,
)
from src.exceptions.repository_exceptions import NotFoundError, ConflictError
from sqlalchemy.orm import Session


def get_one(id: int, session: Session) -> TestCase:
    try:
        result = test_case_repository.get_one(id, session)
    except NotFoundError as e:
        raise TestCaseNotFoundError from e

    return result


def get_all(session: Session) -> Sequence[TestCase]:
    return test_case_repository.get_all(session)


def insert_one(
    *,
    problem_id: int,
    sort_order: int,
    code: str,
    session: Session,
) -> TestCase:
    try:
        result = test_case_repository.insert_one(
            problem_id=problem_id,
            sort_order=sort_order,
            code=code,
            session=session,
        )
    except ConflictError as e:
        raise TestCaseConflictError from e

    return result


def update_one(
    *,
    id: int,
    session: Session,
    problem_id: int | None = None,
    sort_order: int | None = None,
    code: str | None = None,
) -> TestCase:
    try:
        result = test_case_repository.update_one(
            id=id,
            session=session,
            problem_id=problem_id,
            sort_order=sort_order,
            code=code,
        )
    except NotFoundError as e:
        raise TestCaseNotFoundError from e
    except ConflictError as e:
        raise TestCaseConflictError from e

    return result


def delete_one(id: int, session: Session) -> None:
    try:
        test_case_repository.delete_one(id, session)
    except NotFoundError as e:
        raise TestCaseNotFoundError from e
