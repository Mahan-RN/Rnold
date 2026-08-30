from pydantic import BaseModel, ConfigDict
from datetime import datetime


class GetUser(BaseModel):
    github_id: int
    github_email: str
    username: str
    created_at: datetime
    last_login: datetime
    role: int

    model_config = ConfigDict(from_attributes=True)
