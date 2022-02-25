# Rick and Morty Project
Test project for JellySmack

## Installation
I've used a virtualenv w/ python 3.8.9
The installed packages used are listed in requirements.txt
```bash
pip install -r requirements.txt
```
The requirements should be probably separated into dev/test/prod.

## Database
I've used a naif approach to populate the database (sqlite), that is, delete and recreate the database file anytime there is a change
in the table definition or when running the import script again.

## Import script
- Creating and activating the virtualenv
- Install the packages
- cd into the project root and `python import_data.py`

## Run the application

Launch `python server.py` and open the browser at  http://127.0.0.1:8000/docs#/ where the self generated documentation and playground is available. 

## Tests
From the root directory lauch `pytest`

## Development Process
This is my first ever application with FastAPI. 🥳  
I'm a long time Django developer, I've discovered the two frameworks have two very distinct architectures and philosophies.  
It took me few days to develop the application, as I've spent most of the time on the documentation and how to piece together the different parts (SQLAlchemy, Migrations, Pydantic, etcr). 
When I was at 75% of the completion of the application I've realized I've made a bad choice, by using the library [sqlmodel](https://sqlmodel.tiangolo.com/) by the same author of FastAPI.

I've assumed `sqlmodel` was already well tested and integrated into FastAPI, but I've painfully realized this still not the case.
SqlModel tries to merge Pydantic models with SQLAchemy models into a single class. In theory this is would be a nice plus and increase DX.  
Unfortunately this library has still few bugs and lack of functionalities, not to mention that the section on [Advanced User Guide](https://sqlmodel.tiangolo.com/advanced/) is empty...  
Once I've realized this, I had to re-think the entire application, so I re-wrote most of it.


## Models
- The `Character`s and `Episode`s tables are linked via and M2M relationship. 
   This is realized via an intermediary association table `CharacterEpisode`.
- The `Comment` model is connected via foreign key to both `Character` and `Episode`. 
  A third foreign key points to the `User` (I've not completed the `User` model/application)
  - Normally the foreign keys to `Character` and `Episode` are mutually exclusive
  - At least one of them should be passed when creating a comment (I've added a custom validator for this)
  

## Improvements and Limitations
I've realized only the mandatory parts of the excersize as I've spent most of the time on the documentation and by knocking my head against SQLModel 🤕  
The application has some space for improvements.

- Tests are limited in case and coverage
- Many other filter can be added (min and max date for an episode airing date, for example)
- Single and list entity can be served in different shapes by passing extra Path parameter, examples:
  - For an episode list the charcaters appearing in it
  - A comment can list the name of the charcater/episode to which is applied (not only the ids)
- The import script is not suitable for production as all the previous data stored in the db will be lost.
  A production solution would be provided by a migration system, for example `Alembic`.


### Comment on a character on an episode

Since a comment can also be applied to a character appearing on an episode this is technically feasible in two different ways. 

When creating a comment object we can pass both FKs to `Character` and `Episode` at the same time. 
In this case they identify a row in the association table `CharacterEpisode` (this case is not tested ⚠️)

Another easier way to do this: add a **single** primary key to `CharacterEpisode`, 
and a constraint on `character_id` and `episode_id` to be unique together. 
In this case the comment item would simply point with a FK to the primary key of the association table.

---

### Time to get Schwifty
![Rick](rick.jpeg)
