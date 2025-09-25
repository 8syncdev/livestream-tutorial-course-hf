from ninja import Router
from django.contrib.auth import get_user_model # import Auth Model User vào
from django.http import HttpResponse
from ..schemas import *
from typing import *

UserModel = get_user_model()

user_router = Router(tags=['users'])

@user_router.get('/', response=List[UserOut])
def list_users(request):
    users = UserModel.objects.all()
    return users