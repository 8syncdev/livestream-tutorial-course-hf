from ninja import Schema

class BookInReq(Schema):
    title: str
    author: str
    year: int

class BookOutReq(Schema):
    id: int
    title: str
    author: str
    year: int