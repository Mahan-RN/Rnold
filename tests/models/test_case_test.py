import pytest
from src.models.test_case import TestCase


class TestTestCase:
    test_case1: TestCase

    @pytest.fixture(autouse=True)
    def before_each(self):
        self.test_case1 = TestCase(
            id=123,
            problem_id=1234,
            input="y=3",
            expected_output="Passed",
            is_hidden=False,
        )

    def test_constructor(self):
        assert self.test_case1.id == 123
        assert self.test_case1.problem_id == 1234
        assert self.test_case1.input == "y=3"
        assert self.test_case1.expected_output == "Passed"
        assert not self.test_case1.is_hidden
