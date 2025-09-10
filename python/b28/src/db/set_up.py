from sqlmodel import (
    SQLModel,
    Session,
    create_engine,
    Field,
    select
)
from typing import *
from src.config import DB_PATH

engine = create_engine(f"sqlite:///{DB_PATH}")

from src.schemas import User


def create_all_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as ss:
        yield ss
