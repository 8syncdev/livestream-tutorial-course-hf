from ninja import Schema

class UserSchema(Schema):
    id: int
    name: str
    email: str


