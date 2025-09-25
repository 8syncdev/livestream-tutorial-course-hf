import requests


user = requests.get("http://127.0.0.1:8080/api/users")

print(user.json())
