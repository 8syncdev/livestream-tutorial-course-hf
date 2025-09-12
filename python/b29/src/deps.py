from typing import Annotated
from fastapi import Depends
from src.db import Session, get_session

SessionAnnotation = Annotated[Session, Depends(get_session)]