import jwt
from time import sleep

import datetime

JWT_SECRET = 'dkfghkdfjhgldkshgklhdfsgd6fg56df5g6df5g6df56g5df65g5fdg5dg56df56gdf65'

payload = {
    "sub": '4545',
    "iat": datetime.datetime.now(datetime.UTC),
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=5),

    "userName": 'Vasyl',
    'age': 18,
    'is_admin': False
}

encode_jwt = jwt.encode(
    payload=payload,
    key=JWT_SECRET,
    algorithm='HS256'
)
print(encode_jwt)

# web surfing
# sleep(4)
decode = jwt.decode(
    jwt=encode_jwt,
    key=JWT_SECRET,
    algorithms=['HS256'],
    # options={'verify_signature': False}
)

print(decode)