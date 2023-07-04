"""
schemas.py contains all templates that are used to manage object in database
"""
from pydantic import BaseModel


class Contact(BaseModel):
    """Schema for contact in database"""

    first_name: str
    last_name: str
    phone_number: int
    email: str

    class Config:
        orm_mode = True


class Credintials(BaseModel):
    """Schema for user credentials in database"""

    username: str
    password: str

    class Config:
        orm_mode = True
