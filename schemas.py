from pydantic import BaseModel
from typing import Optional

class Contact(BaseModel):
    first_name: str
    last_name: str
    phone_number: int
    email: str

    class Config:
        orm_mode = True

