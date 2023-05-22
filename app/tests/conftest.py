import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base, User, UserInfo
from db.session import get_db
from main import app

HOST = "mysql_db"
USER = "root"
PASS = os.getenv("MYSQL_ROOT_PASSWORD")
DB = os.getenv("MYSQL_DATABASE")


def create_test_base():
    engine = create_engine(
        f"mysql+mysqlconnector://{USER}:{PASS}@{HOST}:3306/{DB}"
    )
    with engine.connect() as conn:
        conn.execute(f"DROP DATABASE IF EXISTS {DB}_test")
        conn.execute(f"CREATE DATABASE {DB}_test")

    engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASS}@{HOST}:3306/{DB}_test")


def get_test_engine():
    return create_engine(f"mysql+mysqlconnector://{USER}:{PASS}@{HOST}:3306/{DB}_test")

def get_db_overrride():
    engine = get_test_engine()
    session_local = sessionmaker(bind=engine)
    try:
        db = session_local()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = get_db_overrride

@pytest.fixture(scope="session")
def db_engine():
    create_test_base()
    test_engine = get_test_engine()

    Base.metadata.create_all(bind=test_engine)
    yield test_engine
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="session")
def db(db_engine):
    session = sessionmaker(bind=db_engine)
    try:
        db = session()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session")
def user(db):
    user = User(
        username="test_user",
        password="test_password"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    user_info = UserInfo(
        user_id=user.id,
        name="Тестовый админ",
        surname="Тестовый админ"
    )
    db.add(user_info)
    db.commit()
    
    return user
