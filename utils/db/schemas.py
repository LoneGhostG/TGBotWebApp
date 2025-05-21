from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    username: Optional[str]


class User(UserCreate):
    ...
    
    class Config:
        orm_mode = True
