from src.database import Base
from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import IntEnum, auto
from datetime import datetime
from sqlalchemy import DateTime, func
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User


class Status(IntEnum):
    ACCEPTED = auto()
    WRONG_ANSWER = auto()
    ERROR = auto()


class Submission(Base):
    __tablename__ = "submissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    problem_id: Mapped[int] = mapped_column(ForeignKey("problems.id"))
    status: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    runtime_ms: Mapped[int]
    code: Mapped[str] = mapped_column(Text)
    user: Mapped["User"] = relationship(back_populates="submissions")

    def __repr__(self) -> str:
        return f"""
        Submission(
        id: {self.id},
        user_id: {self.user_id},
        problem_id: {self.problem_id},
        status: {self.status},
        created_at: '{self.created_at}',
        runtime_ms: {self.runtime_ms},
        code: '{self.code}'
        )
        """
