from ninja_extra import api_controller, NinjaExtraAPI
from ninja_jwt.controller import TokenObtainPairController

@api_controller('/token', tags=['Auth'])
class CustomTokenController(TokenObtainPairController):
    ...