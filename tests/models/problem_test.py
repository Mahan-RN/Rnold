import pytest
from src.models.problem import Problem, Difficulty
from uuid import UUID


class TestProblem:
    @pytest.fixture(autouse=True)
    def before_each(self) -> None:
        self.problem1 = Problem(
            title="Arrays",
            desc="this is an array problem",
            diff=Difficulty.HARD,
            starter_code="x = 2+2",
        )

    def test_constructor(self) -> None:
        assert isinstance(self.problem1._id, UUID)
        assert self.problem1._id.version == 4
        assert self.problem1.title == "Arrays"
        assert self.problem1.desc == "this is an array problem"
        assert self.problem1.diff == Difficulty.HARD
        assert self.problem1.starter_code == "x = 2+2"
