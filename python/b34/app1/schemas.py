from ninja import Schema
from typing import Optional
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserOut(Schema):
    id: int
    username: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]


class UserIn(Schema):
    username: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]

class UserUpdate(Schema):
    username: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]

