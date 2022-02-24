from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class BaseCrud(object):
    def __init__(self, model_class):
        """"""
        self.model = model_class

    def _get_query(self, db: Session):
        """Return the query, useful for composition"""
        return db.query(self.model)

    def _get_query_paginated(
            self, db: Session,
            offset: int = 0,
            limit: int = 10,
            query=None
    ):
        """Return the query with pagination filter"""
        if query is None:
            query = self._get_query(db)
        return query.offset(offset) \
            .limit(limit)

    def create(self, db: Session, obj_in):
        obj_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_one(self, db: Session, id: int):
        return self._get_query(db) \
            .filter(self.model.id == id).first()

    def get_many(self, db: Session, offset: int = 0, limit: int = 10):
        return self._get_query_paginated(db, offset, limit).all()

    def update(self, db: Session, obj_db, obj_in):
        obj_data = jsonable_encoder(obj_db)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(obj_db, field, update_data[field])
        db.add(obj_db)
        db.commit()
        db.refresh(obj_db)
        return obj_db

    def delete(self, db: Session, id: int):
        obj = self.get_one(db, id)
        db.delete(obj)
        db.commit()
        return obj
