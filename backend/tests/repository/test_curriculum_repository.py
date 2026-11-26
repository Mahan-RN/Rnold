from sqlalchemy.orm import Session

from src.repository import curriculum_repository
from tests.factory_types import ProblemMaker, TopicMaker


class TestCurriculumRepository:
    def test_get_curriculum(
        self, db_session: Session, make_topic: TopicMaker, make_problem: ProblemMaker
    ) -> None:
        topic_1 = make_topic()
        topic_2 = make_topic(name="topic 2", description="description 2", sort_order=20)
        make_problem()
        make_problem(title="problem 2")
        make_problem(topic_id=2, title="problem 3")
        make_problem(topic_id=2, title="problem 4")
        db_session.refresh(topic_1)
        db_session.refresh(topic_2)
        curriculum = curriculum_repository.get_curriculum(db_session)
        assert len(curriculum) == 2
        topic_1 = curriculum[0]
        topic_2 = curriculum[1]
        assert topic_1.name == "topic 1"
        assert topic_2.name == "topic 2"
        assert len(topic_1.problems) == 2
        assert len(topic_2.problems) == 2
        assert topic_1.problems[0].title == "problem 1"
        assert topic_1.problems[1].title == "problem 2"
        assert topic_2.problems[0].title == "problem 3"
        assert topic_2.problems[1].title == "problem 4"
