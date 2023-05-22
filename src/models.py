from datetime import date
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    joined: date
    is_admin: bool = False
    nickname: Optional[str]
    

class UserResponse(BaseModel):
    id: str