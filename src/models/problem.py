from enum import Enum


class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class Problem:
    def __init__(
        self, id: int, title: str, desc: str, diff: Difficulty, starter_code: str
    ):
        self.id: int = id
        self.title: str = title
        self.desc: str = desc
        self.diff: Difficulty = diff
        self.starter_code = starter_code

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def desc(self) -> str:
        return self._desc

    @property
    def diff(self) -> Difficulty:
        return self._diff

    @property
    def starter_code(self) -> str:
        return self.starter_code

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    @desc.setter
    def desc(self, desc: str) -> None:
        self._desc = desc

    @diff.setter
    def diff(self, diff: Difficulty) -> None:
        self._diff = diff

    @starter_code.setter
    def starter_code(self, starter_code: str) -> None:
        self._starter_code = starter_code
