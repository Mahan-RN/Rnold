from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from src.database import get_db
from src.dependency import CurrentAdmin
from src.exceptions.evaluation_case_exceptions import EvaluationCaseNotFoundError
from src.models import EvaluationCase
from src.schemas.test_case import (
    CreateTestCaseRequest,
    PatchTestCaseRequest,
    TestCaseResponse,
)
from src.services import evaluation_case_services

router = APIRouter(prefix="/test-cases", tags=["test-cases"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get(
    "/{test_case_id}",
    response_model=TestCaseResponse,
    responses={404: {"description": "Test case not found"}},
)
def get_test_case(test_case_id: int, session: DbSession) -> EvaluationCase:
    try:
        result = evaluation_case_services.get_one(test_case_id, session)
        return result
    except EvaluationCaseNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("", response_model=TestCaseResponse)
def add_test_case(
    request: CreateTestCaseRequest, session: DbSession, admin: CurrentAdmin
) -> EvaluationCase:
    result = evaluation_case_services.insert_one(
        **request.model_dump(), session=session
    )
    session.commit()
    return result


@router.patch(
    "/{test_case_id}",
    response_model=TestCaseResponse,
    responses={404: {"description": "Test case not found"}},
)
def update_test_case(
    test_case_id: int,
    request: PatchTestCaseRequest,
    session: DbSession,
    admin: CurrentAdmin,
) -> EvaluationCase:
    try:
        result = evaluation_case_services.update_one(
            **request.model_dump(), id=test_case_id, session=session
        )
        session.commit()
        return result
    except EvaluationCaseNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete(
    "/{test_case_id}", responses={404: {"description": "Test case not found"}}
)
def delete_test_case(
    test_case_id: int, session: DbSession, admin: CurrentAdmin
) -> Response:
    try:
        evaluation_case_services.delete_one(test_case_id, session)
        session.commit()
        return Response(status.HTTP_204_NO_CONTENT)
    except EvaluationCaseNotFoundError as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=str(e))
