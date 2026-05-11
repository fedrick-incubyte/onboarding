"""Integration tests for auth routes: POST /register and POST /login."""
from datetime import datetime, timezone, timedelta

import jwt as pyjwt


def should_return_201_when_registering_with_valid_data(client):
    response = client.post(
        "/register", json={"email": "user@example.com", "password": "securepass123"}
    )
    assert response.status_code == 201


def should_return_400_on_duplicate_email(client):
    client.post("/register", json={"email": "user@example.com", "password": "securepass123"})
    response = client.post(
        "/register", json={"email": "user@example.com", "password": "securepass123"}
    )
    assert response.status_code == 400


def should_return_access_token_on_valid_login(client):
    client.post("/register", json={"email": "user@example.com", "password": "securepass123"})
    response = client.post(
        "/login", json={"email": "user@example.com", "password": "securepass123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.get_json()


def should_return_401_when_no_auth_header(client):
    assert client.get("/me").status_code == 401


def should_return_user_profile_with_valid_token(client):
    client.post("/register", json={"email": "user@example.com", "password": "securepass123"})
    token = client.post("/login", json={"email": "user@example.com", "password": "securepass123"}).get_json()["access_token"]
    response = client.get("/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.get_json()["email"] == "user@example.com"


def should_return_401_for_expired_token(client, app):
    expired_token = pyjwt.encode(
        {"sub": "1", "email": "x@x.com", "exp": datetime.now(timezone.utc) - timedelta(seconds=1)},
        app.config["SECRET_KEY"],
        algorithm="HS256",
    )
    response = client.get("/me", headers={"Authorization": f"Bearer {expired_token}"})
    assert response.status_code == 401


def should_return_401_for_invalid_token(client):
    response = client.get("/me", headers={"Authorization": "Bearer garbage.token.value"})
    assert response.status_code == 401


def should_return_401_when_bearer_prefix_is_missing(client):
    response = client.get("/me", headers={"Authorization": "some-token-without-bearer-prefix"})
    assert response.status_code == 401


def should_return_401_for_nonexistent_email_on_login(client):
    response = client.post("/login", json={"email": "nobody@example.com", "password": "anypassword"})
    assert response.status_code == 401


def should_return_401_for_wrong_password_on_login(client):
    client.post("/register", json={"email": "user@example.com", "password": "securepass123"})
    response = client.post("/login", json={"email": "user@example.com", "password": "wrongpassword"})
    assert response.status_code == 401


def should_return_422_when_register_missing_email(client):
    response = client.post("/register", json={"password": "securepass123"})
    assert response.status_code == 422


def should_return_422_when_register_missing_password(client):
    response = client.post("/register", json={"email": "user@example.com"})
    assert response.status_code == 422
