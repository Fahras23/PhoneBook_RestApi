"""models.py contains all models used in database"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    """
    Model for contact object in phonebook database
    Values phone number and email are unique in database and cannot be repeated
    """

    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)


class Credintials(Base):
    """
    Model for user credentials object in phonebook database
    Value username is unique in database and cannot be repeated
    """

    __tablename__ = "credentials"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
