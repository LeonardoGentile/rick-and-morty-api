from typing import List

from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session

from .db import get_db
from src.models import Character
from src.schemas import CharacterRead, StatusEnum, GenderEnum, SpeciesEnum
from ..crud.characters import CharacterCrud

router = APIRouter()


@router.get("", status_code=200, response_model=List[CharacterRead])
def get_characters(
        *,
        offset: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db),
        status: StatusEnum = None,
        gender: GenderEnum = None,
        species: SpeciesEnum = None
) -> List[Character]:
    crud = CharacterCrud()
    characters = crud.get_many(db, offset, limit, status, gender, species)
    return characters


@router.get("/{character_id}", status_code=200, response_model=CharacterRead)
def get_character(
        *,
        character_id: int,
        db: Session = Depends(get_db)
) -> Character:
    crud = CharacterCrud()
    character = crud.get_one(db, character_id)
    return character
