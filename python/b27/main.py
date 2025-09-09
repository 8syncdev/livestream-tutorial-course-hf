from db import (
    create_all_tables,
    get_session,
    UserRequest,
    UserDB
)

create_all_tables()


from fastapi import FastAPI

app = FastAPI()

session = next(get_session())

@app.post('/users')
def create_user(data: UserRequest):
    # user = UserDB(username=data.username, password=data.password) # truyền giá trị theo tên
    user = UserDB(**data.model_dump()) # viết tắt **{...} => ...

    session.add(user)
    session.commit()
    session.refresh(user)

    return {
        'data': user.model_dump()
    }


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True)