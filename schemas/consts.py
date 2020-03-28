from enum import Enum


class UserRoles(str, Enum):
    BASE = "base"
    OPERATOR = "operator"
    ADMIN = "admin"
