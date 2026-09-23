from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Problem, TestCase
from src.dependency import CurrentAdmin

from src.services import problem_services
from src.exceptions.problem_exceptions import ProblemNotFoundError, DuplicateTitleError
from src.schemas.problem import (
    ProblemsResponse,
    CreateProblemRequest,
    PatchProblemRequest,
)
from src.schemas.test_case import TestCaseResponse

router = APIRouter(prefix="/problems", tags=["problems"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get("", response_model=list[ProblemsResponse])
def get_problems(session: DbSession) -> Sequence[Problem]:
    return problem_services.get_all(session)


@router.get("/{problem_id}", responses={404: {"description": "Problem not found"}})
def get_problem(problem_id: int, session: DbSession) -> Problem:
    try:
        problem = problem_services.get_one(problem_id, session)
        return problem
    except ProblemNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get(
    "/{problem_id}/test-cases",
    response_model=list[TestCaseResponse],
    responses={404: {"description": "Problem not found"}},
)
def get_test_cases(problem_id: int, session: DbSession) -> Sequence[TestCase]:
    try:
        result = problem_services.get_test_cases(problem_id, session)
        return result
    except ProblemNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("", responses={403: {"description": "Title already exists"}})
def add_problem(
    request: CreateProblemRequest, session: DbSession, admin: CurrentAdmin
) -> Problem:
    try:
        result = problem_services.insert_one(**request.model_dump(), session=session)
        session.commit()
        return result
    except DuplicateTitleError as e:
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(e))


@router.patch("/{problem_id}", responses={404: {"description": "Problem not found"}})
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
        return result
    except ProblemNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{problem_id}", responses={404: {"description": "Problem not found"}})
def delete_problem(
    problem_id: int, session: DbSession, admin: CurrentAdmin
) -> Response:
    try:
        problem_services.delete_one(problem_id, session)
        session.commit()
        return Response(status.HTTP_204_NO_CONTENT)
    except ProblemNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))
