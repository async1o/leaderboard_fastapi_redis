from typing import List
from pydantic import BaseModel

class UserSchema(BaseModel):
    user_id: int
    username: str
    email: str
    password: str
    points: int

    class Config():
        from_attributes = True

class UserAddSchema(BaseModel):
    username: str
    email: str
    password: str