from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from src.models import Topic


def get_curriculum(session: Session) -> Sequence[Topic]:
    stmt = (
        select(Topic).order_by(Topic.sort_order).options(selectinload(Topic.problems))
    )
    return session.scalars(stmt).all()
