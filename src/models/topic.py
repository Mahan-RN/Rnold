from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    slug: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    order: Mapped[int] = mapped_column(unique=True)

    def __repr__(self) -> str:
        return f"Topic({self.name}, {self.slug})"
