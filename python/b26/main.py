# def tong(a: int, b: int):
#     return a + b

from fastapi import FastAPI
from _type import UserRequest
import uvicorn


app = FastAPI()

@app.post('/users', )
def create_user(data: UserRequest):
    print(data.model_dump())

    return data.model_dump()

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)


