from .models import Book
from .schema import (
    BookInReq, 
    BookOutReq
)
from ninja import Router

book_api = Router()


@book_api.post('/', response=BookOutReq)
def create_book(req, data: BookInReq):
    book = Book.objects.create(**data.dict())
    return book