# from src.schemas.user import PostUser
from sqlalchemy.orm import Session

from src.services import problem_services, test_case_services
from src.models import Topic, Difficulty
from src.exceptions.problem_exceptions import ProblemNotFoundError, DuplicateTitleError
import pytest


class TestProblemServices:
    def setup_method(self):
        self.topic_1 = Topic(
            "Arithmetic Operations", "Simple mathematical operations", 10
        )
        self.problem_1 = {
            "sort_order": 10,
            "topic_id": 1,
            "title": "Summation",
            "description": "sum x and y",
            "difficulty": Difficulty.EASY,
            "starter_code": "some code",
        }
        self.problem_2 = {
            "sort_order": 20,
            "topic_id": 1,
            "title": "Subtraction",
            "description": "subtract x and y",
            "difficulty": Difficulty.MEDIUM,
            "starter_code": "some more code",
        }

    def test_get_one_no_match(self, db_session: Session):
        with pytest.raises(ProblemNotFoundError):
            problem_services.get_one(1, db_session)

    def test_insert_one(self, db_session: Session):
        db_session.add(self.topic_1)
        db_session.flush()
        result = problem_services.insert_one(**self.problem_1, session=db_session)
        assert result.id == 1
        assert result.topic_id == 1
        assert result.sort_order == 10
        assert result.title == "Summation"
        assert result.description == "sum x and y"
        assert result.difficulty == Difficulty.EASY
        assert result.starter_code == "some code"

    def test_insert_one_duplicate_title(self, db_session: Session):
        db_session.add(self.topic_1)
        db_session.flush()
        problem_services.insert_one(**self.problem_1, session=db_session)
        with pytest.raises(DuplicateTitleError):
            self.problem_2["title"] = self.problem_1["title"]
            problem_services.insert_one(**self.problem_2, session=db_session)

    def test_get_all_test_cases_no_match(self, db_session: Session):
        with pytest.raises(ProblemNotFoundError):
            problem_services.get_test_cases(1, db_session)

    def test_get_all_test_cases(self, db_session: Session):
        problem_services.insert_one(
            topic_id=1,
            sort_order=1,
            title="summation",
            description="some string",
            difficulty=Difficulty.EASY,
            starter_code="some starter code",
            session=db_session,
        )
        problem_services.insert_one(
            topic_id=1,
            sort_order=10,
            title="subtraction",
            description="some string",
            difficulty=Difficulty.EASY,
            starter_code="some starter code",
            session=db_session,
        )
        test_case_1_dict = {
            "problem_id": 1,
            "sort_order": 0,
            "code": "some code",
            "expected_output": "some output",
        }
        test_case_2_dict = {
            "problem_id": 2,
            "sort_order": 10,
            "code": "some other code",
            "expected_output": "some other output",
            "is_hidden": False,
        }
        test_case1 = test_case_services.insert_one(
            **test_case_1_dict, session=db_session
        )
        test_case2 = test_case_services.insert_one(
            **test_case_2_dict, session=db_session
        )
        problem_1_test_cases = problem_services.get_test_cases(
            problem_id=1, session=db_session
        )
        problem_2_test_cases = problem_services.get_test_cases(
            problem_id=2, session=db_session
        )
        assert len(problem_1_test_cases) == 1
        assert problem_1_test_cases[0] == test_case1
        assert len(problem_2_test_cases) == 1
        assert problem_2_test_cases[0] == test_case2

    def test_update_one_no_match(self, db_session: Session):
        with pytest.raises(ProblemNotFoundError):
            problem_services.update_one(**self.problem_1, id=1, session=db_session)

    def test_update_one_match(self, db_session: Session):
        db_session.add(self.topic_1)
        db_session.flush()
        before_update = problem_services.insert_one(
            **self.problem_1, session=db_session
        )
        assert before_update.description == "sum x and y"
        result = problem_services.update_one(
            id=before_update.id, description="new description", session=db_session
        )
        assert result.description == "new description"

    def test_delete_one_no_match(self, db_session: Session):
        with pytest.raises(ProblemNotFoundError):
            problem_services.delete_one(1, db_session)

    def test_delete_one_match(self, db_session: Session):
        db_session.add(self.topic_1)
        db_session.flush()
        before_delete = problem_services.insert_one(
            **self.problem_1, session=db_session
        )
        problem_services.delete_one(before_delete.id, db_session)
        with pytest.raises(ProblemNotFoundError):
            problem_services.get_one(before_delete.id, db_session)
