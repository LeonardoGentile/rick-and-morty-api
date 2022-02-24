import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


SQLITE_FILE_NAME = "db.sqlite3"
DB_FILE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, SQLITE_FILE_NAME))
DATABASE_URL = f"sqlite:///{DB_FILE_PATH}"


characters_file_name = "./data/rick_morty-characters_v1.json"
CHARACTERS_FILE = os.path.abspath(os.path.join(PROJECT_ROOT, characters_file_name))

episodes_file_name = "./data/rick_morty-episodes_v1.json"
EPISODES_FILE = os.path.abspath(os.path.join(PROJECT_ROOT, episodes_file_name))


SQLITE_FILE_NAME_TEST = "db_test.sqlite3"
DB_FILE_PATH_TEST = os.path.abspath(os.path.join(PROJECT_ROOT, SQLITE_FILE_NAME_TEST))
DATABASE_URL_TEST = f"sqlite:///{DB_FILE_PATH_TEST}"


characters_test_file_name = "./tests/test_characters.json"
CHARACTERS_TEST_FILE = os.path.abspath(os.path.join(PROJECT_ROOT, characters_test_file_name))

episodes_test_file_name = "./tests/test_episodes.json"
EPISODES_TEST_FILE = os.path.abspath(os.path.join(PROJECT_ROOT, episodes_test_file_name))
