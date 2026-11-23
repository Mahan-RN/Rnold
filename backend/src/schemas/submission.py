from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SubmissionResponse(BaseModel):
    id: int
    user_id: int
    problem_id: int
    accepted: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CreateSubmissionRequest(BaseModel):
    problem_id: int
    accepted: bool
