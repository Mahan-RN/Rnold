from sqlalchemy.orm import Session
from src.models import Topic, Difficulty
from src.repository import problem_repository, curriculum_repository


class TestCurriculumRepository:
    def setup_method(self):
        self.topic_1 = Topic(
            "Arithmetic Operations", "Simple mathematical operations", 10
        )
        self.topic_2 = Topic("Data Structures", "Vectors and Matrices", 20)
        self.problem_1_topic_1 = {
            "sort_order": 10,
            "topic_id": 1,
            "title": "Summation",
            "description": "sum x and y",
            "difficulty": Difficulty.EASY,
            "starter_code": "some code",
        }
        self.problem_2_topic_1 = {
            "sort_order": 20,
            "topic_id": 1,
            "title": "Subtraction",
            "description": "subtract x and y",
            "difficulty": Difficulty.MEDIUM,
            "starter_code": "some more code",
        }
        self.problem_1_topic_2 = {
            "sort_order": 10,
            "topic_id": 2,
            "title": "Orthogonality",
            "description": "is this matrix orthogonal?",
            "difficulty": Difficulty.HARD,
            "starter_code": "some code",
        }
        self.problem_2_topic_2 = {
            "sort_order": 20,
            "topic_id": 2,
            "title": "Invertibility",
            "description": "is this matrix invertible?",
            "difficulty": Difficulty.HARD,
            "starter_code": "some more code",
        }

    def test_get_curriculum(self, db_session: Session):
        db_session.add(self.topic_1)
        db_session.add(self.topic_2)
        db_session.flush()
        problem_repository.insert_one(**self.problem_1_topic_1, session=db_session)
        problem_repository.insert_one(**self.problem_2_topic_1, session=db_session)
        problem_repository.insert_one(**self.problem_1_topic_2, session=db_session)
        problem_repository.insert_one(**self.problem_2_topic_2, session=db_session)
        db_session.refresh(self.topic_1)
        db_session.refresh(self.topic_2)
        curriculum = curriculum_repository.get_curriculum(db_session)
        assert len(curriculum) == 2
        topic_1 = curriculum[0]
        topic_2 = curriculum[1]
        assert topic_1.name == "Arithmetic Operations"
        assert topic_2.name == "Data Structures"
        assert len(topic_1.problems) == 2
        assert len(topic_2.problems) == 2
        assert topic_1.problems[0].title == "Summation"
        assert topic_1.problems[1].title == "Subtraction"
        assert topic_2.problems[0].title == "Orthogonality"
        assert topic_2.problems[1].title == "Invertibility"
