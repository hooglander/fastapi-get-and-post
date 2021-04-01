from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, conint


class Score(BaseModel):
    home: Optional[conint(ge=0)] = Field(0, title="Home")
    away: Optional[conint(ge=0)] = Field(0, title="Away")

    class Config:
        orm_mode = True


class Team(str, Enum):
    home = "home"
    away = "away"


class ValidationError(BaseModel):
    loc: List[str] = Field(..., title="Location")
    msg: str = Field(..., title="Message")
    type: str = Field(..., title="Error Type")


class Goal(BaseModel):
    player: Optional[str] = Field(None, title="Player")
    team: Team


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title="Detail")
