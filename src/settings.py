import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

SQLITE_FILE_NAME = "db.sqlite3"
DB_FILE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, SQLITE_FILE_NAME))
DATABASE_URL = f"sqlite:///{DB_FILE_PATH}"
