# _dict = {
#     'username': 'user01',
#     'password': '123'
# }

# def create_user(username: str, password: str):
#     print(username, password)


# create_user(**_dict)

from fastapi import FastAPI
from src.routers import user_router
from src.db import *

create_all_tables()


app = FastAPI()

app.include_router(user_router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)

