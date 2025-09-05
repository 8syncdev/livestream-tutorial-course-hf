from pydantic import (
    BaseModel,
    Field
)

class UserRequest(BaseModel):
    username: str = Field(min_length=5, max_length=10)