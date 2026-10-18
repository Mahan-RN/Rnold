from collections.abc import Sequence
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select
from src.models import Topic


def get_curriculum(session: Session) -> Sequence[Topic]:
    stmt = (
        select(Topic).order_by(Topic.sort_order).options(selectinload(Topic.problems))
    )
    return session.scalars(stmt).all()
