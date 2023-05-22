from sqlalchemy import (
    DateTime,
    Column,
    Integer,
    VARCHAR,
    DATE,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(VARCHAR(255), nullable=False, comment="Логин пользователя")
    password = Column(VARCHAR(255), nullable=False, comment="Пароль пользователя")
    created = Column(DateTime, server_default=func.now(), comment="Дата создания записи")


class UserInfo(Base):
    __tablename__ = "users_info"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(VARCHAR(255), nullable=False, comment="Имя пользователя")
    surname = Column(VARCHAR(255), nullable=False, comment="Фамилия пользователя")
    birthdate = Column(DATE, comment="Дата рождения")
    phone = Column(Integer, comment="Номер телефона")

