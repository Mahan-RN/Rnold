from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from src.database import get_db
from src.dependency import CurrentAdmin
from src.exceptions.problem_exceptions import ProblemConflictError, ProblemNotFoundError
from src.models import EvaluationCase, Problem
from src.schemas.problem import (
    CreateProblemRequest,
    PatchProblemRequest,
    ProblemResponse,
    ProblemsResponse,
)
from src.schemas.test_case import TestCaseResponse
from src.services import problem_services

router = APIRouter(prefix="/problems", tags=["problems"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get("", response_model=list[ProblemsResponse])
def get_problems(session: DbSession) -> Sequence[Problem]:
    return problem_services.get_all(session)


@router.get(
    "/{problem_id}",
    response_model=ProblemResponse,
    responses={404: {"description": "Problem not found"}},
)
def get_problem(problem_id: int, session: DbSession) -> Problem:
    try:
        problem = problem_services.get_one(problem_id, session)
    except ProblemNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))

    return problem


@router.get(
    "/{problem_id}/test-cases",
    response_model=list[TestCaseResponse],
    responses={404: {"description": "Problem not found"}},
)
def get_test_cases(problem_id: int, session: DbSession) -> Sequence[EvaluationCase]:
    try:
        result = problem_services.get_test_cases(problem_id, session)
    except ProblemNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))

    return result


@router.post(
    "",
    response_model=ProblemResponse,
    responses={409: {"description": "Conflict error"}},
)
def add_problem(
    request: CreateProblemRequest, session: DbSession, admin: CurrentAdmin
) -> Problem:
    try:
        result = problem_services.insert_one(**request.model_dump(), session=session)
        session.commit()
    except ProblemConflictError as e:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(e))

    return result


@router.patch(
    "/{problem_id}",
    response_model=ProblemResponse,
    responses={
        404: {"description": "Problem not found"},
        409: {"description": "Conflict error"},
    },
)
def update_problem(
    problem_id: int,
    request: PatchProblemRequest,
    session: DbSession,
    admin: CurrentAdmin,
) -> Problem:
    try:
        result = problem_services.update_one(
            id=problem_id, **request.model_dump(), session=session
        )
        session.commit()
    except ProblemNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))
    except ProblemConflictError as e:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(e))
    return result


@router.delete("/{problem_id}", responses={404: {"description": "Problem not found"}})
def delete_problem(
    problem_id: int, session: DbSession, admin: CurrentAdmin
) -> Response:
    try:
        problem_services.delete_one(problem_id, session)
        session.commit()
    except ProblemNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))

    return Response(status.HTTP_204_NO_CONTENT)
