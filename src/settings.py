import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

SQLITE_FILE_NAME = "db.sqlite3"
DB_FILE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, SQLITE_FILE_NAME))
DATABASE_URL = f"sqlite:///{DB_FILE_PATH}"


characters_file_name = "./data/rick_morty-characters_v1.json"
CHARACTERS_FILE = os.path.abspath(os.path.join(PROJECT_ROOT, characters_file_name))

episodes_file_name = "./data/rick_morty-episodes_v1.json"
EPISODES_FILE = os.path.abspath(os.path.join(PROJECT_ROOT, episodes_file_name))
