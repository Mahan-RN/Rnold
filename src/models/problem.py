from enum import IntEnum, auto
from src.database import Base
from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .test_case import TestCase


class Difficulty(IntEnum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()


class Problem(Base):
    __tablename__ = "problems"

    id: Mapped[int] = mapped_column(primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"))
    sort_order: Mapped[int | None]
    title: Mapped[str] = mapped_column(Text, unique=True)
    description: Mapped[str] = mapped_column(Text)
    difficulty: Mapped[int]
    starter_code: Mapped[str] = mapped_column(Text)
    test_cases: Mapped[list["TestCase"]] = relationship(
        back_populates="problem", cascade="all, delete-orphan", passive_deletes=True
    )

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
