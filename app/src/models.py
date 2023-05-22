from datetime import date
from typing import Optional, List
from pydantic import BaseModel


class Phones(BaseModel):
    phone: str
    id: int
    name: str
    joined: date


class User(BaseModel):
    id: int
    name: str
    joined: date
    is_admin: bool = False
    nickname: Optional[str]
    phones: List[Phones]


class UserResponse(BaseModel):
    id: str
