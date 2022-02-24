from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, validator, root_validator
from typing import Optional, List


class StatusEnum(str, Enum):
    ALIVE = 'Alive'
    DEAD = 'Dead'
    UNKNOWN = 'unknown'


class GenderEnum(str, Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDERLESS = 'Genderless'
    UNKNOWN = 'unknown'


class SpeciesEnum(str, Enum):
    POOPYBUTTHOLE = 'Poopybutthole'
    ANIMAL = 'Animal'
    MYTHOLOGICAL_CREATURE = 'Mythological Creature'
    ROBOT = 'Robot'
    HUMAN = 'Human'
    HUMANOID = 'Humanoid'
    ALIEN = 'Alien'
    DISEASE = 'Disease'
    UNKNOWN = 'unknown'
    CRONENBERG = 'Cronenberg'


class CharacterBase(BaseModel):
    id: Optional[int]
    name: str
    status: StatusEnum
    gender: GenderEnum
    species: SpeciesEnum
    type: Optional[str] = None

    class Config:
        orm_mode = True


class Character(CharacterBase):
    episodes: List["Episode"]
    pass


class CharacterCreate(CharacterBase):
    """Data Model passed by the user to create a new Character"""
    pass


class CharacterRead(CharacterBase):
    id: int


class EpisodeBase(BaseModel):
    """A base model, not used directly but for inheritance.

    It can also have Field attrs
    """
    id: Optional[int]
    name: str
    air_date: date
    episode: str

    class Config:
        orm_mode = True


class Episode(EpisodeBase):
    characters: List["Character"]


class EpisodeCreate(EpisodeBase):
    """Data Model passed by the user to create a new Character

    This will be called twice:
        - once initial validation from body (body as dict).     `air_date` is str
        - when the model is instantiated, it calls validation.  `air_date` is `date`
    """

    @validator("air_date", pre=True)
    def parse_air_date(cls, value, values):
        if isinstance(value, str):
            return datetime.strptime(
                value,
                "%B %d, %Y"
            ).date()
        return value


class EpisodeRead(EpisodeBase):
    id: int
    comments: List["CommentRead"]


class EpisodeReadWithStringDate(EpisodeRead):
    """Data Model returned to the user"""
    air_date: str

    @validator("air_date", pre=True)
    def parse_air_date(cls, value, values):
        if isinstance(value, date):
            return value.strftime("%B %d, %Y")
        return value


class CommentBase(BaseModel):
    id: Optional[int]
    content: str

    class Config:
        orm_mode = True


class Comment(CommentBase):
    pass


class CommentCreate(CommentBase):
    episode_id: Optional[int] = None
    character_id: Optional[int] = None
    user_id: Optional[int] = None

    @root_validator
    def check_ids(cls, values):
        episode_id, character_id = values.get('episode_id'), values.get('character_id')
        if episode_id is None and character_id is None:
            raise ValueError("Both 'episode_id', 'character_id' can't be empty")
        return values



class CommentRead(CommentBase):
    user_id: Optional[int]
    episode_id: Optional[int]
    character_id: Optional[int]
