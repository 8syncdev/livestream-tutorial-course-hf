import requests

url = "http://127.0.0.1:8000"


res = requests.get(f"{url}/users/")

print(res.json())