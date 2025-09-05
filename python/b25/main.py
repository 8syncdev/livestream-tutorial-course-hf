from fastapi import FastAPI
import uvicorn

app = FastAPI()

BOOKS = [
    {
        'id': 1,
        'name': 'Harry Potter'
    },
    {
        'id': 2,
        'name': 'Spider man'
    }
]

# 127.0.0.1:port/hello
@app.get('/books')
def get_all_books():
    return {
        'data': BOOKS
    }


@app.get('/books/{id}')
def get_one_book(id: int):
    return list(filter(lambda item: item.get('id') == id, BOOKS))


@app.post('/books')
def create_book(data: dict):
    BOOKS.append(data)

    return BOOKS

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)