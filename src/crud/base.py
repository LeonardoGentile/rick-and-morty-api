from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class BaseCrud(object):
    def __init__(self, model_class):
        """"""
        self.model = model_class

    def create(self, db: Session, obj_in):
        obj_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_one(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.id == id).first()

    def get_many_q(self, db: Session):
        """Return the query, useful for composition"""
        return db.query(self.model)

    def get_many_q_pag(self, db: Session, offset: int = 0, limit: int = 100):
        """Return the query, useful for composition"""
        return self.get_many_q(db).offset(offset).limit(limit)

    def get_many(self, db: Session, offset: int = 0, limit: int = 100):
        return self.get_many_q_pag(db, offset, limit).all()

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
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj




