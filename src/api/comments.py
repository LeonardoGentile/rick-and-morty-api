from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.models import Comment
from src.schemas import CommentRead, CommentCreate
from .db import get_db
from ..crud.comments import CommentCrud

router = APIRouter()


@router.post("", status_code=201, response_model=CommentRead)
def create_comment(
        *,
        episode: CommentCreate,
        db: Session = Depends(get_db)
) -> Comment:
    crud = CommentCrud()
    comment = crud.create(db, episode)
    return comment


@router.get("/{comment_id}", status_code=200, response_model=CommentRead)
def get_comment(
        *,
        db: Session = Depends(get_db),
        comment_id: int
) -> Comment:
    crud = CommentCrud()
    comment = crud.get_one(db, comment_id)
    # TODO: return something else in case comment doesn't exist
    return comment


@router.get("", status_code=200, response_model=List[CommentRead])
def get_comments(
        *,
        offset: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
) -> List[Comment]:
    crud = CommentCrud()
    comments = crud.get_many(db, offset, limit)
    return comments


@router.delete("/{comment_id}", status_code=204)
def delete_comment(
        *,
        comment_id,
        db: Session = Depends(get_db)
) -> None:
    comment_crud = CommentCrud()
    comment_crud.delete(db, comment_id)
