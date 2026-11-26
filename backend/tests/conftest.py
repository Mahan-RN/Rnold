from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from src.database import Base, get_db
from src.main import app
from src.models import Difficulty, Problem, Topic
from tests.factory_types import ProblemMaker, TopicMaker

test_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    bind=test_engine, autoflush=False, expire_on_commit=False
)


@pytest.fixture()
def db_session() -> Generator[Session]:
    Base.metadata.create_all(bind=test_engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=test_engine)


@pytest.fixture()
def client(db_session: Session) -> Generator[TestClient]:
    def override_get_db() -> Generator[Session]:
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    test_client = TestClient(app)
    yield test_client
    app.dependency_overrides.clear()


### Factories


@pytest.fixture()
def make_topic(db_session: Session) -> TopicMaker:
    def _make(
        name: str = "topic 1", description: str = "description 1", sort_order: int = 10
    ) -> Topic:
        topic = Topic(name, description, sort_order)
        db_session.add(topic)
        db_session.flush()
        return topic

    return _make


@pytest.fixture()
def make_problem(db_session: Session) -> ProblemMaker:
    def _make(
        topic_id: int = 1,
        sort_order: int = 10,
        title: str = "problem 1",
        description: str = "description 1",
        difficulty: Difficulty = Difficulty.EASY,
        starter_code: str = "some code",
    ) -> Problem:
        problem = Problem(
            topic_id, sort_order, title, description, difficulty, starter_code
        )
        db_session.add(problem)
        db_session.flush()
        return problem

    return _make
