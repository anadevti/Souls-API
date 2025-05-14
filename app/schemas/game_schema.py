from typing import Optional
from datetime import date
from pydantic import BaseModel, Field

class GameBase(BaseModel):
    name: str = Field(..., example="Dark Souls")
    description: Optional[str] = Field(None, example="Um RPG de ação desafiador")

class GameCreate(GameBase):
    release_date: date = Field(..., example="2011-09-22")

class GameOut(GameBase):
    id: int
    release_date: date

    class Config:
        orm_mode = True
