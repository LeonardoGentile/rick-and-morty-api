from typing import List

from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session

from .db import get_db
from src.models import Character
from src.schemas import CharacterRead
from ..crud.characters import CharacterCrud

router = APIRouter()


@router.get("", status_code=200, response_model=List[CharacterRead])
def get_characters(
        offset: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
) -> List[Character]:
    crud = CharacterCrud()
    characters = crud.get_many(db, offset, limit)
    return characters
