import requests

host = 'http://127.0.0.1:8000'

def test_hello():
    res = requests.get(f"{host}/books/1")
    print(res.json())


def create_book():
    res = requests.post(f"{host}/books", json={
        'id': 3,
        'name': 'Book 3'
    })
    print(res.json())


create_book()