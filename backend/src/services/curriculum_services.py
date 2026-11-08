from collections.abc import Sequence

from sqlalchemy.orm import Session

from src.models import Topic
from src.repository import curriculum_repository


def get_curriculum(session: Session) -> Sequence[Topic]:
    return curriculum_repository.get_curriculum(session)
