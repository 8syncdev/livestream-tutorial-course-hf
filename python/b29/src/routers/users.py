from fastapi import APIRouter
from src.deps import SessionAnnotation
from src.db import User, select
from src.schemas import UserRequest

user_router = APIRouter(
    prefix="/users"
)

@user_router.get('/')
def get_all_users(session_db: SessionAnnotation):
    query = select(User)

    users = session_db.exec(query).all()

    return {
        'data': [user.model_dump() for user in users]
    }


@user_router.post('/')
def create_user(data: UserRequest, session_db: SessionAnnotation):
    user = User(**data.model_dump())
    session_db.add(user)
    session_db.commit()
    session_db.refresh(user)

    return {
        'data': user.model_dump()
    }
