import os


SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL") + os.getenv("DATABASE_NAME")
