from typing import Generic, TypeVar 

from pydantic import BaseModel

T = TypeVar("T")

class Page(BaseModel, Generic[T]):
    items: list[T]
    limit:int
    offset:int
    total: int