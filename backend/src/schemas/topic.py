from pydantic import BaseModel, ConfigDict


class TopicResponse(BaseModel):
    id: int
    name: str
    description: str
    sort_order: int | None

    model_config = ConfigDict(from_attributes=True)


class UpdateTopicRequest(BaseModel):
    name: str | None
    description: str | None
    sort_order: int | None


class CreateTopicRequest(BaseModel):
    name: str
    description: str
    sort_order: int
