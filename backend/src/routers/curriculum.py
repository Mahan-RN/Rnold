from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Topic

from src.services import curriculum_services
from src.schemas.curriculum import CurriculumResponse

router = APIRouter(prefix="/curriculum", tags=["curriculum"])

DbSession = Annotated[Session, Depends(get_db)]


@router.get("", response_model=list[CurriculumResponse])
def get_curriculum(session: DbSession) -> Sequence[Topic]:
    return curriculum_services.get_curriculum(session)
