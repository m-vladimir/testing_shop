import models  # NEEDED FOR CREATING ALL OF MODELS
from database.base import Base
from database.session import engine


def create_all():
    Base.metadata.create_all(bind=engine)


def delete_all():
    Base.metadata.drop_all(bind=engine)
