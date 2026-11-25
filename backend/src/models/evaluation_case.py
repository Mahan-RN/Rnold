from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from .problem import Problem


class EvaluationCase(Base):
    __tablename__ = "evaluation_cases"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    problem_id: Mapped[int] = mapped_column(
        ForeignKey("problems.id", ondelete="CASCADE")
    )
    code: Mapped[str]
    sort_order: Mapped[int]

    problem: Mapped["Problem"] = relationship(
        back_populates="evaluation_cases", init=False
    )

    __table_args__ = (
        UniqueConstraint("problem_id", "sort_order", name="problemID_sortOrder_unique"),
    )

    def __repr__(self) -> str:
        return f"""
        TestCase(
        id: {self.id},
        problem_id: {self.problem_id},
        code: '{self.code}',
        sort_order: '{self.sort_order}'
        )
        """
