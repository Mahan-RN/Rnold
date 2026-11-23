from datetime import datetime
from enum import IntEnum, auto
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.models.problem import Problem
    from src.models.user import User


class Status(IntEnum):
    ACCEPTED = auto()
    WRONG_ANSWER = auto()
    ERROR = auto()


class Submission(Base):
    __tablename__ = "submissions"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.github_id", ondelete="CASCADE")
    )
    problem_id: Mapped[int] = mapped_column(
        ForeignKey("problems.id", ondelete="CASCADE")
    )
    status: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), init=False
    )
    user: Mapped["User"] = relationship(back_populates="submissions", init=False)
    problem: Mapped["Problem"] = relationship(back_populates="submissions", init=False)

    __table_args__ = (Index("idx_user_problem", "user_id", "problem_id"),)

    def __repr__(self) -> str:
        return f"""
        Submission(
        id: {self.id},
        user_id: {self.user_id},
        problem_id: {self.problem_id},
        status: {self.status},
        created_at: '{self.created_at}'
        )
        """
