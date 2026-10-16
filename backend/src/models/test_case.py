from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

if TYPE_CHECKING:
    from .problem import Problem


class TestCase(Base):
    __tablename__ = "test_cases"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    problem_id: Mapped[int] = mapped_column(ForeignKey("problems.id"))
    sort_order: Mapped[int]
    code: Mapped[str] = mapped_column(Text)
    expected_output: Mapped[str] = mapped_column(Text)
    problem: Mapped["Problem"] = relationship(back_populates="test_cases", init=False)
    is_hidden: Mapped[bool] = mapped_column(default=True)

    def __repr__(self) -> str:
        return f"""
        TestCase(
        id: {self.id},
        problem_id: {self.problem_id},
        code: '{self.code}',
        expected_output: '{self.expected_output}',
        is_hidden: {self.is_hidden}
        )
        """
