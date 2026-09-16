from sqlalchemy.orm import Session
from src.models import Topic, Difficulty
from src.repository import problem_repository


class TestProblemRepository:
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
        result = problem_repository.get_one(1, db_session)
        assert result is None

    def test_get_all_empty(self, db_session: Session):
        result = problem_repository.get_all(db_session)
        assert len(result) == 0

    def test_insert_one(self, db_session: Session):
        db_session.add(self.topic_1)
        db_session.flush()
        problem = problem_repository.insert_one(**self.problem_1, session=db_session)
        assert problem.id == 1
        assert problem.topic_id == self.topic_1.id
        assert problem.sort_order == 10
        assert problem.title == "Summation"
        assert problem.description == "sum x and y"
        assert problem.difficulty == Difficulty.EASY
        assert problem.starter_code == "some code"
        assert len(problem.test_cases) == 0
        assert len(problem.submissions) == 0
        assert problem.topic == self.topic_1

    def test_insert_one_multiple(self, db_session):
        db_session.add(self.topic_1)
        db_session.flush()
        problem = problem_repository.insert_one(**self.problem_1, session=db_session)
        assert problem.id == 1
        assert problem.topic_id == self.topic_1.id
        assert problem.sort_order == 10
        assert problem.title == "Summation"
        assert problem.description == "sum x and y"
        assert problem.difficulty == Difficulty.EASY
        assert problem.starter_code == "some code"
        assert len(problem.test_cases) == 0
        assert len(problem.submissions) == 0
        assert problem.topic == self.topic_1

    def test_update_one_no_match(self, db_session: Session):
        db_session.add(self.topic_1)
        db_session.flush()
        result = problem_repository.update_one(id=1, session=db_session)
        assert result is None

    def test_update_one_match(self, db_session: Session):
        db_session.add(self.topic_1)
        db_session.flush()
        problem_repository.insert_one(**self.problem_1, session=db_session)
        result = problem_repository.update_one(id=1, sort_order=20, session=db_session)
        assert result.id == 1
        assert result.topic_id == self.topic_1.id
        assert result.sort_order == 20
        assert result.title == "Summation"
        assert result.description == "sum x and y"
        assert result.difficulty == Difficulty.EASY
        assert result.starter_code == "some code"
        assert len(result.test_cases) == 0
        assert len(result.submissions) == 0
        assert result.topic == self.topic_1

    def test_delete_one_no_match(self, db_session: Session):
        result = problem_repository.delete_one(1, db_session)
        assert result is None

    def test_delete_one_match(self, db_session: Session):
        db_session.add(self.topic_1)
        db_session.flush()
        problem = problem_repository.insert_one(**self.problem_1, session=db_session)
        result = problem_repository.get_one(problem.id, db_session)
        assert result == problem
        problem_repository.delete_one(problem.id, db_session)
        result_after_delete = problem_repository.get_one(problem.id, db_session)
        assert result_after_delete is None
