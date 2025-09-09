import requests

url = 'http://127.0.0.1:8000'

res = requests.post(f'{url}/users', json={
    'username': 'user01',
    'password': '123456789'
})

print(res.json())