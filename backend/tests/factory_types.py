from typing import Protocol

from src.models import Difficulty, Problem, Role, Topic, User


class TopicMaker(Protocol):
    def __call__(
        self, name: str = ..., description: str = ..., sort_order: int = ...
    ) -> Topic: ...


class ProblemMaker(Protocol):
    def __call__(
        self,
        topic_id: int = ...,
        sort_order: int = ...,
        title: str = ...,
        description: str = ...,
        difficulty: Difficulty = ...,
        starter_code: str = ...,
    ) -> Problem: ...


class UserMaker(Protocol):
    def __call__(
        self,
        github_id: int = ...,
        github_email: str = ...,
        username: str = ...,
        role: Role = ...,
    ) -> User: ...
