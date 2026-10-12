"""Pydantic contracts at the frontend-backend boundary."""

from typing import Literal

from pydantic import BaseModel, Field

FaceName = Literal["U", "R", "F", "D", "L", "B"]


class SolveRequest(BaseModel):
    """JSON sent by the React cube input form."""

    faces: dict[FaceName, list[str]] = Field(..., description="Four stickers per face")
    constraint: str = Field(default="", description="Optional natural-language constraint")


class SolveResponse(BaseModel):
    """JSON returned after a solution is found."""

    valid: bool
    moves: list[str]
    depth: int
    explanation: str
    parsed_constraint: dict[str, object]


class ScrambleResponse(BaseModel):
    """JSON returned by the demo scramble route."""

    scramble: list[str]
    faces: dict[str, list[str]]

