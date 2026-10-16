from datetime import datetime
from pydantic import BaseModel, ConfigDict


class SubmissionResponse(BaseModel):
    id: int
    user_id: int
    problem_id: int
    status: int
    created_at: datetime
    runtime_ms: int
    code: str

    model_config = ConfigDict(from_attributes=True)


class CreateSubmissionRequest(BaseModel):
    user_id: int
    problem_id: int
    status: int
    runtime_ms: int
    code: str
