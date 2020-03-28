from sqlalchemy import Column, String
from sqlalchemy.dialects.sqlite import JSON

from models.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(128))
    password = Column(String)

    roles = Column(JSON)  # represent Python list with strings
