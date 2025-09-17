from ninja import NinjaAPI
from django.core.handlers.wsgi import WSGIRequest as InputRequest

api = NinjaAPI()

@api.get('/hello')
def hello(req, name: str):
    return {
        'message': f'Xin chào {name}'
    }