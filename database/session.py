from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core import config


engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=config.DATABASE_DEBUG
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
