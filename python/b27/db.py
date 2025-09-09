from sqlmodel import (
    SQLModel,
    create_engine,
    Session,
    select,
    Field
)
from typing import *

from config import BASE_DIR

engine = create_engine(f"sqlite:///{BASE_DIR / 'db.sqlite3'}")


class AutoId(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True, )

class UserRequest(SQLModel):
    username: str = Field(min_length=5, max_length=10, unique=True)
    password: str = Field(min_length=8)

class UserDB(AutoId, UserRequest, table=True):
    # pass 
    # ...
    '''
        Đã được kế thừa từ AutoId, UserRequest nên mặc định đã có: id, username, password
    '''


def create_all_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as ss:
        yield ss

