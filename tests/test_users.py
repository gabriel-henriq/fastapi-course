from jose import jwt
import pytest

from app.config import settings
from app import schemas
from fastapi import status


def test_create_user(client):
    response = client.post(
        '/users/', json={"email": "g@gmail.com", "password": "123"})
    assert response.status_code == 201


def test_login_user(test_user, client):
    response = client.post(
        '/login/', data={"username": test_user['email'], "password": test_user["password"]})
    login_response = schemas.Token(**response.json())

    payload = jwt.decode(login_response.access_token,
                         settings.secret_key, settings.algorithm)

    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_response.token_type == "bearer"
    assert response.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ('wrongEmail@gmail.com', 'wrongPassword', status.HTTP_403_FORBIDDEN),
    ('g@gmail.com', 'wrongPassword',  status.HTTP_403_FORBIDDEN),
    ('wrongEmail@gmail.com', '123',  status.HTTP_403_FORBIDDEN),
    (None, '123', status.HTTP_422_UNPROCESSABLE_ENTITY),
    ('g@gmail.com', None, status.HTTP_422_UNPROCESSABLE_ENTITY),
    (None, None, status.HTTP_422_UNPROCESSABLE_ENTITY)
])
def test_incorrect_login(client, email, password, status_code):
    response = client.post(
        '/login/', data={"username": email, "password": password})
    assert response.status_code == status_code
