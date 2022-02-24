import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.api.db import get_db
from src.database import init_db
import import_data
from src.main import app
from src.settings import DATABASE_URL_TEST, DB_FILE_PATH_TEST, CHARACTERS_TEST_FILE, EPISODES_TEST_FILE

if os.path.exists(DB_FILE_PATH_TEST):
    os.remove(DB_FILE_PATH_TEST)

engine = create_engine(
    DATABASE_URL_TEST,
    connect_args={"check_same_thread": False}
)
SessionTest = sessionmaker(autocommit=False, autoflush=False, bind=engine)
init_db(engine)


def override_get_db():
    try:
        db = SessionTest()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

import_data.create_and_populate_db(
    SessionTest(),
    EPISODES_TEST_FILE,
    CHARACTERS_TEST_FILE
)


@pytest.fixture()
def client():
    return TestClient(app)
