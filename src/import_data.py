import json
import os
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

# from src import models
from src.database import SessionLocal, init_db
from src.models import Episode, Character
from src.settings import DB_FILE_PATH, EPISODES_FILE, CHARACTERS_FILE


def populate_episodes(session, file_name):
    with session:
        with open(file_name) as f:
            episodes = json.load(f)

        for episode in episodes:
            air_date = datetime.strptime(episode['air_date'], "%B %d, %Y").date()

            ep_obj = Episode(
                id=episode["id"],
                name=episode["name"],
                air_date=air_date,
                episode=episode["episode"]
            )
            session.add(ep_obj)
        session.commit()



def populate_characters(session: Session, file_name: os.path):

    with session:
        with open(file_name) as f:
            characters = json.load(f)

        for char in characters:
            # Populate M2M link table
            stm = select(Episode).filter(
                Episode.id.in_(char["episode"])
            )
            episodes = session.execute(stm).scalars().all()

            char_create = Character(
                id=char["id"],
                name=char["name"],
                status=char["status"],
                species=char["species"],
                gender=char["gender"],
                type=char["type"],
                episodes=episodes
            )
            session.add(char_create)

        session.commit()



def main():
    """Import Json into DB

    This is naif as everytime we run this script the
    DB will be deleted and recreated.
    I wouldn't do this in prod!
    """

    if os.path.exists(DB_FILE_PATH):
        os.remove(DB_FILE_PATH)

    init_db()
    session = SessionLocal()

    populate_episodes(session, EPISODES_FILE)
    populate_characters(session, CHARACTERS_FILE)


if __name__ == "__main__":
    main()
