from abc import ABCMeta
from uuid import UUID

from pydantic import BaseModel


class BaseSchema(BaseModel, metaclass=ABCMeta):
    class Config:
        orm_mode = True
        use_enum_values = True


class BaseSchemaInner(BaseSchema, metaclass=ABCMeta):
    uuid: UUID
    is_deleted: bool


class BaseSchemaIn(BaseSchema, metaclass=ABCMeta):
    pass
