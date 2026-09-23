from sqlalchemy.orm import Session
from src.repository import problem_repository
from src.models import Problem, TestCase
from src.exceptions.problem_exceptions import ProblemNotFoundError, DuplicateTitleError
from collections.abc import Sequence


def get_one(id: int, session: Session) -> Problem:
    problem = problem_repository.get_one(id, session)
    if problem is None:
        raise ProblemNotFoundError(f"Problem with ID {id} not found")
    else:
        return problem


def get_test_cases(problem_id: int, session: Session) -> Sequence[TestCase]:
    result = problem_repository.get_test_cases(problem_id, session)
    if result is None:
        raise ProblemNotFoundError(f"Problem with ID {problem_id} not found")
    else:
        return result


def get_all(session: Session) -> Sequence[Problem]:
    return problem_repository.get_all(session)


def insert_one(
    *,
    topic_id: int,
    sort_order: int,
    title: str,
    description: str,
    difficulty: int,
    starter_code: str,
    session: Session,
) -> Problem:
    result = session.query(Problem).filter(Problem.title == title).all()
    if len(result) != 0:
        raise DuplicateTitleError(f"Problem with title {title} already exists")
    else:
        return problem_repository.insert_one(
            topic_id=topic_id,
            sort_order=sort_order,
            title=title,
            description=description,
            difficulty=difficulty,
            starter_code=starter_code,
            session=session,
        )


def update_one(
    *,
    id: int,
    topic_id: int | None = None,
    sort_order: int | None = None,
    title: str | None = None,
    description: str | None = None,
    difficulty: int | None = None,
    starter_code: str | None = None,
    session: Session,
) -> Problem:
    result = problem_repository.update_one(
        id=id,
        topic_id=topic_id,
        sort_order=sort_order,
        title=title,
        description=description,
        difficulty=difficulty,
        starter_code=starter_code,
        session=session,
    )
    if result is None:
        raise ProblemNotFoundError(f"Problem with ID {id} not found")
    else:
        return result


def delete_one(id: int, session: Session) -> None:
    result = problem_repository.get_one(id, session)
    if result is None:
        raise ProblemNotFoundError(f"Problem with ID {id} not found")
    else:
        problem_repository.delete_one(id, session)
