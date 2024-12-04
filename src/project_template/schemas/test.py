from uuid import UUID
from pydantic import BaseModel, ConfigDict


class TestBase(BaseModel):
    name: str
    age: int

    model_config=ConfigDict(from_attributes=True)

class TestIn(TestBase):
    comment: str

class TestOut(TestIn):
    id: UUID

class TestPatch(TestIn):
    pass