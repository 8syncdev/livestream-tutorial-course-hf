from fastapi import APIRouter

user_router = APIRouter(
    prefix="/users"
)

@user_router.get('/')
def get_all_users():
    return {
        'data': 'Get All User Request'
    }