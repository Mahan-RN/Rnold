from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import Problem


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    sort_order: Mapped[int | None] = mapped_column(unique=True)
    problems: Mapped[list["Problem"]] = relationship(
        back_populates="topic",
        cascade="all, delete-orphan",
        passive_deletes=True,
        init=False,
        default_factory=list,
        order_by="Problem.sort_order",
    )

    def __repr__(self) -> str:
        return f"""
        Topic(
        id: {self.id},
        name: '{self.name}',
        description: '{self.description}',
        sort_order: {self.sort_order}
        )"""
