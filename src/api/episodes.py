from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.db import get_db
from src.crud.episodes import EpisodeCrud
from src.models import Episode
from src.schemas import EpisodeRead

router = APIRouter()


@router.get("", status_code=200, response_model=List[EpisodeRead])
def get_episodes(
        offset: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
) -> List[Episode]:
    crud = EpisodeCrud()
    characters = crud.get_many(db, offset, limit)
    return characters
