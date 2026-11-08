from pydantic import BaseModel, ConfigDict


class TestCaseResponse(BaseModel):
    id: int
    problem_id: int
    sort_order: int
    code: str

    model_config = ConfigDict(from_attributes=True)


class CreateTestCaseRequest(BaseModel):
    problem_id: int
    sort_order: int
    code: str


class PatchTestCaseRequest(BaseModel):
    problem_id: int | None = None
    sort_order: int | None = None
    code: str | None = None
