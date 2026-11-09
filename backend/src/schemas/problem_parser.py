from pydantic import BaseModel

from src.models import Difficulty


class ParsedProblem(BaseModel):
    topic_name: str
    sort_order: int
    title: str
    description: str
    difficulty: Difficulty
    starter_code: str


class ParsedTestCase(BaseModel):
    code: str
    sort_order: int
