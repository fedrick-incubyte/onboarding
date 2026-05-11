"""Integration tests for auth routes: POST /register and POST /login."""


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
