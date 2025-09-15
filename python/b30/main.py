# from passlib.hash import bcrypt, argon2

# password = '123'




# print(argon2.hash(password))
# print(argon2.verify(password, argon2.hash(password)))

import jwt
import datetime


SECRET_KEY = 'example'

payload = {
    'id': 1,
    'username': 'user0001',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print(token)

print(jwt.decode(token, SECRET_KEY, algorithms=['HS256']))
# Timestamp