from enum import Enum, auto
from src.database import Base
from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Difficulty(Enum):
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
