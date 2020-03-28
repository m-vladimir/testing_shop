from abc import ABCMeta
from typing import List

from schemas.base import BaseSchema, BaseSchemaInner
from schemas.consts import UserRoles


class BaseUser(BaseSchema, metaclass=ABCMeta):
    first_name: str
    last_name: str
    email: str
    password: str

    roles: List[UserRoles]


class UserInner(BaseSchemaInner, BaseUser):
    pass
