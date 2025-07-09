import pydantic
from typing import Optional


class CommandCreate(pydantic.BaseModel):
    name: str
    description: str


class CommandUpdate(pydantic.BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True