import requests


def create_user():
    res = requests.post('http://127.0.0.1:8000/users', json={
        'username': 'user123'
    })

    print(res.json())

create_user()