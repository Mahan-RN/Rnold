from collections.abc import Sequence
from src.models import TestCase
from src.repository import test_case_repository
from src.exceptions.test_case_exceptions import TestCaseNotFoundError
from sqlalchemy.orm import Session


def get_one(id: int, session: Session) -> TestCase:
    result = test_case_repository.get_one(id, session)
    if result is None:
        raise TestCaseNotFoundError(f"Test case with ID {id} not found")
    else:
        return result


def get_all(session: Session) -> Sequence[TestCase]:
    return test_case_repository.get_all(session)


def insert_one(
    *,
    problem_id: int,
    sort_order: int,
    code: str,
    expected_output: str,
    is_hidden: bool = True,
    session: Session,
) -> TestCase:
    return test_case_repository.insert_one(
        problem_id=problem_id,
        sort_order=sort_order,
        code=code,
        expected_output=expected_output,
        is_hidden=is_hidden,
        session=session,
    )


def update_one(
    *,
    id: int,
    session: Session,
    problem_id: int | None = None,
    sort_order: int | None = None,
    code: str | None = None,
    expected_output: str | None = None,
    is_hidden: bool | None = None,
) -> TestCase:
    result = test_case_repository.update_one(
        id=id,
        session=session,
        problem_id=problem_id,
        sort_order=sort_order,
        code=code,
        expected_output=expected_output,
        is_hidden=is_hidden,
    )
    if result is None:
        raise TestCaseNotFoundError(f"Test case with ID {id} not found")
    else:
        return result


def delete_one(id: int, session: Session) -> None:
    result = test_case_repository.get_one(id, session)
    if result is None:
        raise TestCaseNotFoundError(f"Test case with ID {id} not found")
    else:
        test_case_repository.delete_one(id, session)
