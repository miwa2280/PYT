from time import sleep
import jwt
from utils_pyjwt import create_jwt, extract_payload_from_jwt

payload = {"surname": "Лисий", "group": "9-А", "sub": "4545"}

token = create_jwt(subject=payload["sub"], payload=payload, lifetime_sec=3)

print(token)
print("-" * 50)

try:
  data = extract_payload_from_jwt(token)
  print("Успішно декодовано:", data)
except Exception as e:
  print("Помилка:", e)

sleep(4)
try:
  extract_payload_from_jwt(token)
except jwt.exceptions.ExpiredSignatureError as e:
  print("Помилка (прострочено)::", e)

fresh_token = create_jwt(subject=payload["sub"], payload=payload, lifetime_sec=60)
wrong_secret = "wrong_key_123"
try:
  jwt.decode(jwt=fresh_token, key=wrong_secret, algorithms=["HS256"])
except jwt.exceptions.InvalidSignatureError as e:
  print("Помилка (невірний підпис):", e)