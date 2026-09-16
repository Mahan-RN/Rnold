from pydantic import BaseModel, ConfigDict
from src.models import Difficulty


class ProblemsResponse(BaseModel):
    id: int
    topic_id: int
    sort_order: int
    title: str
    difficulty: Difficulty

    model_config = ConfigDict(from_attributes=True)


class CreateProblemRequest(BaseModel):
    topic_id: int
    sort_order: int
    title: str
    description: str
    difficulty: Difficulty
    starter_code: str


class PatchProblemRequest(BaseModel):
    topic_id: int | None
    sort_order: int | None
    title: str | None
    description: str | None
    difficulty: Difficulty | None
    starter_code: str | None
