from ninja import NinjaAPI
from django.core.handlers.wsgi import WSGIRequest as InputRequest
from .schema import UserSchema


api = NinjaAPI()

@api.get('/hello')
def hello(req, name: str):
    return {
        'message': f'Xin chào {name}'
    }


@api.post("/users", response=UserSchema)
def create_user(req, data: UserSchema):
    return data