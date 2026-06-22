from enum import Enum
from src.database import Base
from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column


class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class Problem(Base):
    __tablename__ = "problems"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    slug: Mapped[str] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)
    difficulty: Mapped[str] = mapped_column(Text)
    starter_code: Mapped[str] = mapped_column(Text)
