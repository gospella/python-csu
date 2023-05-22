import os
from typing import Generator
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


HOST = "mysql_db"
USER = os.getenv("MYSQL_USER")
PASSWORD = os.getenv("MYSQL_PASSWORD")
DB = os.getenv("MYSQL_DATABASE")

engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:3306/{DB}")
Session = sessionmaker(bind=engine)


def get_db() -> Generator:
    with Session.begin() as db:
        yield db