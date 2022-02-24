from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.settings import DATABASE_URL

connect_args = {"check_same_thread": False}  # specific for sqlite
engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args=connect_args
)

# Each instance of the SessionLocal class will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db(local_engine=None):
    # SQLModel.metadata.create_all(engine)
    from src import models
    if not local_engine:
        local_engine = engine
    models.Base.metadata.create_all(bind=local_engine)


Base = declarative_base()
