from sqlalchemy.orm import Session
from src.models import Topic
from src.repository import curriculum_repository
from collections.abc import Sequence


def get_curriculum(session: Session) -> Sequence[Topic]:
    return curriculum_repository.get_curriculum(session)
