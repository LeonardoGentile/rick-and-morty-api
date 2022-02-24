from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, ForeignKeyConstraint
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    # Rels
    comments = relationship("Comment", back_populates="user")


class CharacterEpisode(Base):
    """M2M Table"""
    __tablename__ = "character_episode"

    character_id = Column(Integer, ForeignKey("character.id"), primary_key=True)
    episode_id = Column(Integer, ForeignKey("episode.id"), primary_key=True)
    # comments = relationship("Comment")



class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String)
    species = Column(String)
    gender = Column(String)
    type = Column(String)


    episodes = relationship("Episode",
                            secondary=CharacterEpisode.__tablename__,
                            back_populates="characters")
    comments = relationship("Comment")


class Episode(Base):
    __tablename__ = "episode"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    air_date = Column(DateTime)
    episode = Column(String)
    # Rels
    characters = relationship("Character", secondary=CharacterEpisode.__tablename__, back_populates="episodes")
    comments = relationship("Comment")


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")

    episode_id = Column(Integer, ForeignKey("episode.id"))
    character_id = Column(Integer, ForeignKey("character.id"))

    # character_in_episode = relationship("CharacterEpisode", foreign_keys=[character_id, episode_id],
    #                                     back_populates="comments")
    #
    # __table_args__ = (ForeignKeyConstraint((episode_id, character_id),
    #                                        (CharacterEpisode.episode_id, CharacterEpisode.character_id)
    #                                        ), {})

