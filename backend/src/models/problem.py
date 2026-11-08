from enum import IntEnum, auto
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.models import Submission, TestCase, Topic


class Difficulty(IntEnum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()


class Problem(Base):
    __tablename__ = "problems"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"))
    sort_order: Mapped[int]
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    difficulty: Mapped[int]
    starter_code: Mapped[str]
    test_cases: Mapped[list["TestCase"]] = relationship(
        back_populates="problem",
        cascade="all, delete-orphan",
        passive_deletes=True,
        init=False,
        default_factory=list,
    )
    submissions: Mapped[list["Submission"]] = relationship(
        back_populates="problem",
        cascade="all, delete-orphan",
        passive_deletes=True,
        init=False,
        default_factory=list,
    )
    topic: Mapped["Topic"] = relationship(back_populates="problems", init=False)

    def __repr__(self) -> str:
        return f"""
        Problem(
        id: {self.id},
        topic_id: {self.topic_id},
        sort_order: {self.sort_order},
        title: '{self.title}',
        description: '{self.description}',
        difficulty: {self.difficulty},
        starter_code: '{self.starter_code}'
        )
        """
