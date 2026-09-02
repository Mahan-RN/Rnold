from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class GetUser(BaseModel):
    github_id: int
    github_email: EmailStr
    username: str
    created_at: datetime
    last_login: datetime
    role: int

    model_config = ConfigDict(from_attributes=True)
