from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text

from .database import Base


class Larp(Base):
    __tablename__ = 'larps'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    organizer = Column(String)
    website = Column(String)
    datetime_start = Column(DateTime)
    datetime_end = Column(DateTime)
    image = Column(String)
    description = Column(Text)
    validated = Column(Boolean, default=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(Text, index=True, unique=True)
    password_hash = Column(Text)
    enabled = Column(Boolean, default=False)
