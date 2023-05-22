from datetime import date, datetime
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
    

class CreateUser(BaseModel):
    name: str
    surname: str
    birthdate: Optional[date]
    phone: Optional[int]
    
class UserDB(CreateUser):
    id: int
    created: datetime
    class Config:
        orm_mode = True
