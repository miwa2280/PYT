import jwt

import datetime

JWT_SECRET = 'dkfghkdfjhgldkshgklhdfsgd6fg56df5g6df5g6df56g5df65g5fdg5dg56df56gdf65'

def create_jwt(subject: str | int, payload: dict, lifetime_sec: int = 5) -> str:

    base_payload = {
        "sub": str(subject),
        "iat": datetime.datetime.now(datetime.UTC),
        "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=lifetime_sec),
    }
    final_payload = payload | base_payload

    encode_jwt = jwt.encode(
        payload=final_payload,
        key=JWT_SECRET,
        algorithm='HS256'
    )
    return encode_jwt


def extract_payload_from_jwt(jwt_token: str) -> dict:
    decode = jwt.decode(
        jwt=jwt_token,
        key=JWT_SECRET,
        algorithms=['HS256'],
        # options={'verify_signature': False}
    )

    return decode