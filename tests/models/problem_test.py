import pytest
from src.models.problem import Problem


class TestProblem:

    problem1: Problem
    problem2: Problem

    @pytest.fixture(autouse=True)
    def before_each(self):
        self.problem1 = Problem(
            id=123,
            title="Arrays",
            desc="this is an array problem",
            diff=4,
            starter_code="x = 2+2",
        )

    def test_constructor(self) -> None:
        assert self.problem1.id == 123
        assert self.problem1.title == "Arrays"
        assert self.problem1.desc == "this is an array problem"
        assert self.problem1.diff == 4
        assert self.problem1.starter_code == "x = 2+2"
