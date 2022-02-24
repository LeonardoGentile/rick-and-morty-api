from sqlalchemy.orm import Session

from .base import BaseCrud
from ..models import Character
from ..schemas import StatusEnum, GenderEnum, SpeciesEnum


class CharacterCrud(BaseCrud):

    def __init__(self):
        super().__init__(Character)

    def get_many(self,
                 db: Session,
                 offset: int = 0,
                 limit: int = 10,
                 status: StatusEnum = None,
                 gender: GenderEnum = None,
                 species: SpeciesEnum = None):

        query = self._get_query(db)
        if status:
            query = query.filter(self.model.status == status)
        if gender:
            query = query.filter(self.model.gender == gender)
        if species:
            query = query.filter(self.model.species == species)
        return self._get_query_paginated(db, offset, limit, query).all()
