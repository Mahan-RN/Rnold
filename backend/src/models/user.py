from datetime import datetime
from enum import IntEnum, auto
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from .submission import Submission


class Role(IntEnum):
    USER = auto()
    ADMIN = auto()


class User(Base):
    __tablename__ = "users"

    github_id: Mapped[int] = mapped_column(primary_key=True)
    github_email: Mapped[str]
    username: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), init=False
    )
    last_login: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), init=False
    )
    submissions: Mapped[list["Submission"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
        init=False,
        default_factory=list,
    )
    role: Mapped[int] = mapped_column(default=Role.USER)

    def __repr__(self) -> str:
        return f"""
            User(
            github_id: {self.github_id},
            github_email: '{self.github_email}',
            username: '{self.username}',
            created_at: '{self.created_at}',
            last_login: '{self.last_login}',
            role: {self.role}
            )
            """
