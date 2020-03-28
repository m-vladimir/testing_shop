from sqlalchemy import Column
from sqlalchemy.dialects.sqlite import BLOB, BOOLEAN

from database.base import Base


class BaseModel(Base):
    __abstract__ = True

    uuid = Column(BLOB, primary_key=True)
    is_deleted = Column(BOOLEAN, default=False)
