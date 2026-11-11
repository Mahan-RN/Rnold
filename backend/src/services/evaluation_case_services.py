from collections.abc import Sequence

from sqlalchemy.orm import Session

from src.exceptions.evaluation_case_exceptions import (
    EvaluationCaseConflictError,
    EvaluationCaseNotFoundError,
)
from src.exceptions.repository_exceptions import ConflictError, NotFoundError
from src.models import EvaluationCase
from src.repository import evaluation_case_repository


def get_one(id: int, session: Session) -> EvaluationCase:
    try:
        result = evaluation_case_repository.get_one(id, session)
    except NotFoundError as e:
        raise EvaluationCaseNotFoundError from e

    return result


def get_all(session: Session) -> Sequence[EvaluationCase]:
    return evaluation_case_repository.get_all(session)


def insert_one(
    *,
    problem_id: int,
    sort_order: int,
    code: str,
    session: Session,
) -> EvaluationCase:
    try:
        result = evaluation_case_repository.insert_one(
            problem_id=problem_id,
            sort_order=sort_order,
            code=code,
            session=session,
        )
    except ConflictError as e:
        raise EvaluationCaseConflictError from e

    return result


def update_one(
    *,
    id: int,
    session: Session,
    problem_id: int | None = None,
    sort_order: int | None = None,
    code: str | None = None,
) -> EvaluationCase:
    try:
        result = evaluation_case_repository.update_one(
            id=id,
            session=session,
            problem_id=problem_id,
            sort_order=sort_order,
            code=code,
        )
    except NotFoundError as e:
        raise EvaluationCaseNotFoundError from e
    except ConflictError as e:
        raise EvaluationCaseConflictError from e

    return result


def delete_one(id: int, session: Session) -> None:
    try:
        evaluation_case_repository.delete_one(id, session)
    except NotFoundError as e:
        raise EvaluationCaseNotFoundError from e
