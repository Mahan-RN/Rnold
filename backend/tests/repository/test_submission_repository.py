import pytest

from datetime import datetime
from sqlalchemy.orm import Session

from src.models import Difficulty, Problem, Role, Topic, User
from src.repository import submission_repository
from src.exceptions.repository_exceptions import NotFoundError


class TestSubmissionRepository:
    def setup_method(self):
        self.admin1 = User(
            github_id=123,
            github_email="user@email.com",
            username="user1",
            role=Role.ADMIN,
        )
        self.topic_1 = Topic(
            "Arithmetic Operations", "Simple mathematical operations", 10
        )
        self.problem_1 = Problem(
            topic_id=1,
            sort_order=1,
            title="summation",
            description="some string",
            difficulty=Difficulty.EASY,
            starter_code="some starter code",
        )

    def test_get_one_no_match(self, db_session: Session):
        with pytest.raises(NotFoundError):
            submission_repository.get_one(1, db_session)

    def test_insert_one(self, db_session: Session):
        db_session.add(self.admin1)
        db_session.add(self.topic_1)
        db_session.add(self.problem_1)
        db_session.flush()
        result = submission_repository.insert_one(
            user_id=self.admin1.github_id,
            problem_id=self.problem_1.id,
            status=1,
            runtime_ms=5,
            code="hello",
            session=db_session,
        )
        assert result.id == 1
        assert result.user_id == 123
        assert result.problem_id == 1
        assert result.status == 1
        assert isinstance(result.created_at, datetime)
        assert result.runtime_ms == 5
        assert result.code == "hello"
        assert result.user == self.admin1
        assert result.problem == self.problem_1

    def test_get_one_match(self, db_session: Session):
        db_session.add(self.admin1)
        db_session.add(self.topic_1)
        db_session.add(self.problem_1)
        db_session.flush()
        submission = submission_repository.insert_one(
            user_id=self.admin1.github_id,
            problem_id=self.problem_1.id,
            status=1,
            runtime_ms=5,
            code="hello",
            session=db_session,
        )
        result = submission_repository.get_one(1, db_session)
        assert result == submission

    def test_get_all(self, db_session: Session):
        db_session.add(self.admin1)
        db_session.add(self.topic_1)
        db_session.add(self.problem_1)
        db_session.flush()
        submission1 = submission_repository.insert_one(
            user_id=self.admin1.github_id,
            problem_id=self.problem_1.id,
            status=1,
            runtime_ms=5,
            code="hello",
            session=db_session,
        )
        submission2 = submission_repository.insert_one(
            user_id=self.admin1.github_id,
            problem_id=self.problem_1.id,
            status=1,
            runtime_ms=5,
            code="hello",
            session=db_session,
        )
        results = submission_repository.get_all(db_session)
        assert len(results) == 2
        assert results[0] == submission1
        assert results[1] == submission2

    def test_get_per_problem_per_user(self, db_session: Session):
        db_session.add(self.admin1)
        db_session.add(self.topic_1)
        db_session.add(self.problem_1)
        # Setup second user and second problem
        user2 = User(
            github_id=456,
            github_email="user@email.com",
            username="user1",
            role=Role.USER,
        )
        problem_2 = Problem(
            topic_id=1,
            sort_order=1,
            title="subtraction",
            description="some string",
            difficulty=Difficulty.EASY,
            starter_code="some starter code",
        )
        db_session.add(user2)
        db_session.add(problem_2)
        db_session.flush()
        # First user, first problem
        submission1 = submission_repository.insert_one(
            user_id=self.admin1.github_id,
            problem_id=self.problem_1.id,
            status=1,
            runtime_ms=5,
            code="hello",
            session=db_session,
        )
        # First user, second problem
        submission2 = submission_repository.insert_one(
            user_id=self.admin1.github_id,
            problem_id=problem_2.id,
            status=1,
            runtime_ms=5,
            code="hello",
            session=db_session,
        )
        # Second user, first problem
        submission3 = submission_repository.insert_one(
            user_id=user2.github_id,
            problem_id=self.problem_1.id,
            status=1,
            runtime_ms=5,
            code="hello",
            session=db_session,
        )
        # Second user, second problem
        submission4 = submission_repository.insert_one(
            user_id=user2.github_id,
            problem_id=problem_2.id,
            status=1,
            runtime_ms=5,
            code="hello",
            session=db_session,
        )
        # Now test
        result1 = submission_repository.get_per_problem_per_user(
            self.admin1.github_id, self.problem_1.id, db_session
        )
        assert len(result1) == 1
        assert result1[0] == submission1
        result2 = submission_repository.get_per_problem_per_user(
            self.admin1.github_id, problem_2.id, db_session
        )
        assert len(result2) == 1
        assert result2[0] == submission2
        result3 = submission_repository.get_per_problem_per_user(
            user2.github_id, self.problem_1.id, db_session
        )
        assert len(result3) == 1
        assert result3[0] == submission3
        result4 = submission_repository.get_per_problem_per_user(
            user2.github_id, problem_2.id, db_session
        )
        assert len(result4) == 1
        assert result4[0] == submission4

    def test_delete_one_no_match(self, db_session: Session):
        db_session.add(self.admin1)
        db_session.add(self.topic_1)
        db_session.add(self.problem_1)
        db_session.flush()
        insert_result = submission_repository.insert_one(
            user_id=self.admin1.github_id,
            problem_id=self.problem_1.id,
            status=1,
            runtime_ms=5,
            code="hello",
            session=db_session,
        )
        with pytest.raises(NotFoundError):
            submission_repository.delete_one(111, db_session)
        get_result = submission_repository.get_one(insert_result.id, db_session)
        assert get_result == insert_result

    def test_delete_one_match(self, db_session: Session):
        db_session.add(self.admin1)
        db_session.add(self.topic_1)
        db_session.add(self.problem_1)
        db_session.flush()
        insert_result = submission_repository.insert_one(
            user_id=self.admin1.github_id,
            problem_id=self.problem_1.id,
            status=1,
            runtime_ms=5,
            code="hello",
            session=db_session,
        )
        submission_repository.delete_one(insert_result.id, db_session)
        with pytest.raises(NotFoundError):
            submission_repository.get_one(insert_result.id, db_session)
