from pydantic import BaseModel
from typing import Optional


class CharacterRead(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: Optional[str] = None
    gender: str

    class Config:
        orm_mode = True
