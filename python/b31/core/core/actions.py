from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest as InputRequest

def hello(req: InputRequest):
    # print(req.accepted_types)
    return JsonResponse({
        'data': 'Hello'
    })