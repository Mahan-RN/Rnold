from pydantic import BaseModel, ConfigDict

from src.models import Difficulty


class CurriculumProblemResponse(BaseModel):
    id: int
    title: str
    difficulty: Difficulty

    model_config = ConfigDict(from_attributes=True)


class CurriculumResponse(BaseModel):
    id: int
    name: str
    description: str
    problems: list[CurriculumProblemResponse]

    model_config = ConfigDict(from_attributes=True)
