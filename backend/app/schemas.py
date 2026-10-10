from typing import Literal
from pydantic import BaseModel, Field

FaceName = Literal["U", "R", "F", "D", "L", "B"]

class SolveRequest(BaseModel):
    faces: dict[FaceName, list[str]] = Field(..., description="Four stickers per face")
    constraint: str = ""

class SolveResponse(BaseModel):
    valid: bool
    moves: list[str]
    depth: int
    explanation: str
    parsed_constraint: dict[str, object]

