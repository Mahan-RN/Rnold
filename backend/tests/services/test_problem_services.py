# from src.schemas.user import PostUser
from typing import TypedDict

import pytest
from sqlalchemy.orm import Session

from src.exceptions.problem_exceptions import ProblemConflictError, ProblemNotFoundError
from src.models import Difficulty
from src.services import problem_services
from tests.factory_types import EvaluationCaseMaker, ProblemMaker, TopicMaker


class ProblemData(TypedDict):
    sort_order: int
    topic_id: int
    title: str
    description: str
    difficulty: Difficulty
    starter_code: str


class TestProblemServices:
    def setup_method(self) -> None:

        self.problem_1: ProblemData = {
            "sort_order": 10,
            "topic_id": 1,
            "title": "problem 1",
            "description": "description 1",
            "difficulty": Difficulty.EASY,
            "starter_code": "some code",
        }
        self.problem_2: ProblemData = {
            "sort_order": 20,
            "topic_id": 1,
            "title": "problem 2",
            "description": "description 2",
            "difficulty": Difficulty.MEDIUM,
            "starter_code": "some more code",
        }

    def test_get_one_no_match(self, db_session: Session) -> None:
        with pytest.raises(ProblemNotFoundError):
            problem_services.get_one(1, db_session)

    def test_get_one_match(
        self, make_problem: ProblemMaker, db_session: Session
    ) -> None:
        make_problem()
        make_problem(title="problem 2")
        result = problem_services.get_one(1, db_session)

        assert result.id == 1
        assert result.title == "problem 1"

    def test_get_by_title_no_match(
        self, make_problem: ProblemMaker, db_session: Session
    ) -> None:
        make_problem()
        make_problem(title="problem 2")

        with pytest.raises(ProblemNotFoundError):
            problem_services.get_by_title("problem 3", db_session)

    def test_get_by_title_match(
        self, make_problem: ProblemMaker, db_session: Session
    ) -> None:
        make_problem()
        make_problem(title="problem 2")

        result = problem_services.get_by_title("problem 1", db_session)

        assert result.id == 1
        assert result.title == "problem 1"

    def test_get_all_empty(self, db_session: Session) -> None:
        result = problem_services.get_all(db_session)
        assert len(result) == 0

    def test_get_all(self, make_problem: ProblemMaker, db_session: Session) -> None:
        make_problem()
        make_problem(title="problem 2")
        result = problem_services.get_all(db_session)

        assert len(result) == 2

    def test_get_test_cases_no_match(
        self,
        make_problem: ProblemMaker,
        make_evaluation_case: EvaluationCaseMaker,
        db_session: Session,
    ) -> None:
        make_problem()
        make_evaluation_case()
        make_evaluation_case(sort_order=20)

        with pytest.raises(ProblemNotFoundError):
            problem_services.get_test_cases(10, db_session)

    def test_get_test_cases_match(
        self,
        make_problem: ProblemMaker,
        make_evaluation_case: EvaluationCaseMaker,
        db_session: Session,
    ) -> None:
        make_problem()
        make_evaluation_case()
        make_evaluation_case(sort_order=20)

        result = problem_services.get_test_cases(1, db_session)

        assert len(result) == 2
        assert result[0].sort_order == 10
        assert result[1].sort_order == 20

    def test_insert_one(self, make_topic: TopicMaker, db_session: Session) -> None:
        make_topic()
        result = problem_services.insert_one(**self.problem_1, session=db_session)
        assert result.id == 1
        assert result.topic_id == 1
        assert result.sort_order == 10
        assert result.title == "problem 1"
        assert result.description == "description 1"
        assert result.difficulty == Difficulty.EASY
        assert result.starter_code == "some code"

    def test_insert_one_duplicate_title(
        self, make_topic: TopicMaker, db_session: Session
    ) -> None:
        make_topic()
        problem_services.insert_one(**self.problem_1, session=db_session)
        with pytest.raises(ProblemConflictError):
            self.problem_2["title"] = self.problem_1["title"]
            problem_services.insert_one(**self.problem_2, session=db_session)

    def test_update_one_no_match(
        self, make_topic: TopicMaker, make_problem: ProblemMaker, db_session: Session
    ) -> None:
        make_topic()
        make_problem()
        with pytest.raises(ProblemNotFoundError):
            problem_services.update_one(id=10, session=db_session)

    def test_update_one_duplicate_title(
        self, make_topic: TopicMaker, make_problem: ProblemMaker, db_session: Session
    ) -> None:
        make_topic()
        make_problem()
        make_problem(title="problem 2")
        with pytest.raises(ProblemConflictError):
            problem_services.update_one(id=1, title="problem 2", session=db_session)

    def test_update_one_match_sort_order(
        self, make_problem: ProblemMaker, make_topic: TopicMaker, db_session: Session
    ) -> None:
        make_topic()
        make_problem()
        result = problem_services.update_one(id=1, sort_order=20, session=db_session)
        assert result.id == 1
        assert result.topic_id == 1
        assert result.sort_order == 20
        assert result.title == "problem 1"
        assert result.description == "description 1"
        assert result.difficulty == Difficulty.EASY
        assert result.starter_code == "some code"
        assert len(result.evaluation_cases) == 0
        assert len(result.submissions) == 0

    def test_update_one_match_topic_id(
        self, make_problem: ProblemMaker, make_topic: TopicMaker, db_session: Session
    ) -> None:
        make_topic()
        make_topic(name="topic 2", sort_order=20)
        make_problem()
        result = problem_services.update_one(id=1, topic_id=2, session=db_session)
        assert result.id == 1
        assert result.topic_id == 2
        assert result.sort_order == 10
        assert result.title == "problem 1"
        assert result.description == "description 1"
        assert result.difficulty == Difficulty.EASY
        assert result.starter_code == "some code"
        assert len(result.evaluation_cases) == 0
        assert len(result.submissions) == 0

    def test_update_one_match_title(
        self, make_problem: ProblemMaker, make_topic: TopicMaker, db_session: Session
    ) -> None:
        make_topic()
        make_problem()
        result = problem_services.update_one(
            id=1, title="problem x", session=db_session
        )
        assert result.id == 1
        assert result.topic_id == 1
        assert result.sort_order == 10
        assert result.title == "problem x"
        assert result.description == "description 1"
        assert result.difficulty == Difficulty.EASY
        assert result.starter_code == "some code"
        assert len(result.evaluation_cases) == 0
        assert len(result.submissions) == 0

    def test_update_one_match_description(
        self, make_problem: ProblemMaker, make_topic: TopicMaker, db_session: Session
    ) -> None:
        make_topic()
        make_problem()
        result = problem_services.update_one(
            id=1, description="new description", session=db_session
        )
        assert result.id == 1
        assert result.topic_id == 1
        assert result.sort_order == 10
        assert result.title == "problem 1"
        assert result.description == "new description"
        assert result.difficulty == Difficulty.EASY
        assert result.starter_code == "some code"
        assert len(result.evaluation_cases) == 0
        assert len(result.submissions) == 0

    def test_update_one_match_starter_code(
        self, make_problem: ProblemMaker, make_topic: TopicMaker, db_session: Session
    ) -> None:
        make_topic()
        make_problem()
        result = problem_services.update_one(
            id=1, starter_code="new code", session=db_session
        )
        assert result.id == 1
        assert result.topic_id == 1
        assert result.sort_order == 10
        assert result.title == "problem 1"
        assert result.description == "description 1"
        assert result.difficulty == Difficulty.EASY
        assert result.starter_code == "new code"
        assert len(result.evaluation_cases) == 0
        assert len(result.submissions) == 0

    def test_update_one_match_difficulty(
        self, make_problem: ProblemMaker, make_topic: TopicMaker, db_session: Session
    ) -> None:
        make_topic()
        make_problem()
        result = problem_services.update_one(
            id=1, difficulty=Difficulty.HARD, session=db_session
        )
        assert result.id == 1
        assert result.topic_id == 1
        assert result.sort_order == 10
        assert result.title == "problem 1"
        assert result.description == "description 1"
        assert result.difficulty == Difficulty.HARD
        assert result.starter_code == "some code"
        assert len(result.evaluation_cases) == 0
        assert len(result.submissions) == 0

    def test_update_one_match_all(
        self, make_problem: ProblemMaker, make_topic: TopicMaker, db_session: Session
    ) -> None:
        make_topic()
        make_topic(name="topic 2", sort_order=20)
        make_problem()
        result = problem_services.update_one(
            id=1,
            topic_id=2,
            sort_order=20,
            title="problem x",
            description="new description",
            difficulty=Difficulty.HARD,
            starter_code="new code",
            session=db_session,
        )
        assert result.id == 1
        assert result.topic_id == 2
        assert result.sort_order == 20
        assert result.title == "problem x"
        assert result.description == "new description"
        assert result.difficulty == Difficulty.HARD
        assert result.starter_code == "new code"
        assert len(result.evaluation_cases) == 0
        assert len(result.submissions) == 0

    def test_delete_one_no_match(self, db_session: Session) -> None:
        with pytest.raises(ProblemNotFoundError):
            problem_services.delete_one(1, db_session)

    def test_delete_one_match(
        self, make_topic: TopicMaker, db_session: Session
    ) -> None:
        make_topic()
        before_delete = problem_services.insert_one(
            **self.problem_1, session=db_session
        )
        problem_services.delete_one(before_delete.id, db_session)
        with pytest.raises(ProblemNotFoundError):
            problem_services.get_one(before_delete.id, db_session)
