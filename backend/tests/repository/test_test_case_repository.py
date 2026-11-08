from src.models import Problem, Difficulty
from src.repository import test_case_repository
from sqlalchemy.orm import Session


class TestTestCaseRepository:
    def setup_method(self):
        self.problem_1 = Problem(
            topic_id=1,
            sort_order=1,
            title="summation",
            description="some string",
            difficulty=Difficulty.EASY,
            starter_code="some starter code",
        )
        self.problem_2 = Problem(
            topic_id=1,
            sort_order=10,
            title="subtraction",
            description="some string",
            difficulty=Difficulty.EASY,
            starter_code="some starter code",
        )
        self.test_case_1_dict = {
            "problem_id": 1,
            "sort_order": 0,
            "code": "some code",
        }
        self.test_case_2_dict = {
            "problem_id": 2,
            "sort_order": 10,
            "code": "some other code",
        }

    def test_get_one_no_match(self, db_session: Session):
        result = test_case_repository.get_one(1, db_session)
        assert result is None

    def test_insert_one(self, db_session: Session):
        db_session.add(self.problem_1)
        db_session.flush()
        result = test_case_repository.insert_one(
            **self.test_case_1_dict, session=db_session
        )
        assert result is not None
        assert result.id == 1
        assert result.problem_id == 1
        assert result.sort_order == 0
        assert result.code == "some code"

    def test_get_all(self, db_session: Session):
        db_session.add(self.problem_1)
        db_session.add(self.problem_2)
        db_session.flush()
        test_case1 = test_case_repository.insert_one(
            **self.test_case_1_dict, session=db_session
        )
        test_case2 = test_case_repository.insert_one(
            **self.test_case_2_dict, session=db_session
        )
        test_cases = test_case_repository.get_all(db_session)
        assert len(test_cases) == 2
        assert test_cases[0] == test_case1
        assert test_cases[1] == test_case2

    def test_update_one_no_match(self, db_session: Session):
        result = test_case_repository.update_one(id=1, session=db_session)
        assert result is None

    def test_update_one_match_problem_id(self, db_session: Session):
        db_session.add(self.problem_1)
        db_session.add(self.problem_2)
        db_session.flush()
        before_result = test_case_repository.insert_one(
            **self.test_case_1_dict, session=db_session
        )
        assert before_result.problem_id == 1
        after_result = test_case_repository.update_one(
            id=1, session=db_session, problem_id=2
        )
        assert after_result.problem_id == 2
        assert after_result.id == 1
        assert after_result.sort_order == 0
        assert after_result.code == "some code"

    def test_update_one_match_sort_order(self, db_session: Session):
        db_session.add(self.problem_1)
        db_session.add(self.problem_2)
        db_session.flush()
        before_result = test_case_repository.insert_one(
            **self.test_case_1_dict, session=db_session
        )
        assert before_result.problem_id == 1
        after_result = test_case_repository.update_one(
            id=1, session=db_session, sort_order=10
        )
        assert after_result.sort_order == 10
        assert after_result.id == 1
        assert after_result.problem_id == 1
        assert after_result.code == "some code"

    def test_update_one_match_code(self, db_session: Session):
        db_session.add(self.problem_1)
        db_session.add(self.problem_2)
        db_session.flush()
        before_result = test_case_repository.insert_one(
            **self.test_case_1_dict, session=db_session
        )
        assert before_result.problem_id == 1
        after_result = test_case_repository.update_one(
            id=1, session=db_session, code="new code"
        )
        assert after_result.code == "new code"
        assert after_result.id == 1
        assert after_result.problem_id == 1
        assert after_result.sort_order == 0

    def test_update_one_all(self, db_session: Session):
        db_session.add(self.problem_1)
        db_session.add(self.problem_2)
        db_session.flush()
        before_result = test_case_repository.insert_one(
            **self.test_case_1_dict, session=db_session
        )
        assert before_result.problem_id == 1
        after_result = test_case_repository.update_one(
            id=1,
            session=db_session,
            problem_id=2,
            sort_order=10,
            code="new code",
        )
        assert after_result.id == 1
        assert after_result.problem_id == 2
        assert after_result.sort_order == 10
        assert after_result.code == "new code"

    def test_delete_one_no_match(self, db_session: Session):
        db_session.add(self.problem_1)
        db_session.flush()
        test_case_repository.insert_one(**self.test_case_1_dict, session=db_session)
        result = test_case_repository.delete_one(2, db_session)
        assert result is None
        test_case = test_case_repository.get_one(1, db_session)
        assert test_case is not None

    def test_delete_one_match(self, db_session: Session):
        db_session.add(self.problem_1)
        db_session.flush()
        test_case_repository.insert_one(**self.test_case_1_dict, session=db_session)
        result = test_case_repository.delete_one(1, db_session)
        assert result is None
        test_case = test_case_repository.get_one(1, db_session)
        assert test_case is None
