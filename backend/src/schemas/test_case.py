from pydantic import BaseModel, ConfigDict


class TestCaseResponse(BaseModel):
    id: int
    problem_id: int
    sort_order: int
    code: str
    expected_output: str
    is_hidden: bool

    model_config = ConfigDict(from_attributes=True)


class CreateTestCaseRequest(BaseModel):
    problem_id: int
    sort_order: int
    code: str
    expected_output: str
    is_hidden: bool = True


class PatchTestCaseRequest(BaseModel):
    problem_id: int | None = None
    sort_order: int | None = None
    code: str | None = None
    expected_output: str | None = None
    is_hidden: bool | None = None
