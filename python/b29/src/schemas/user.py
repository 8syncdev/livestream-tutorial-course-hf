from sqlmodel import SQLModel, Field
from typing import *

class AutoId(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)

class UserRequest(SQLModel):
    username: str = Field(min_length=5, max_length=10, unique=True)
    password: str = Field(min_length=8, max_length=20)

class User(AutoId, UserRequest, table=True):
    ...