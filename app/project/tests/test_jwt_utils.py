from utils_pyjwt import create_jwt, extract_payload_from_jwt
from time import sleep
import jwt
import pytest

class TestJWTUtils:
    def test_create(self):
        payload = {}
        subject = 123
        token =  create_jwt(subject=subject, payload=payload)
        assert token
        assert isinstance(token, str)

    def test_full_flow_success(self):
        payload = {'user': 'Vasyl'}
        subject = 123
        token =  create_jwt(subject=subject, payload=payload)
        data = extract_payload_from_jwt(token)
        assert data['user'] == payload['user']
        assert data['sub'] == str(subject)

    def test_full_flow_expired(self):
        payload = {'user': 'Vasyl'}
        subject = 123
        token =  create_jwt(subject=subject, payload=payload, lifetime_sec=1)
        sleep(2)
        with pytest.raises(jwt.exceptions.ExpiredSignatureError):
            extract_payload_from_jwt(token)