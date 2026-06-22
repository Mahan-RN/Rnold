from enum import Enum
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class Problem(Base):
    __tablename__ = "problems"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    slug: Mapped[str] = mapped_column(unique=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    difficulty: Mapped[str] = mapped_column(nullable=False)
    starter_code: Mapped[str] = mapped_column(nullable=False)
