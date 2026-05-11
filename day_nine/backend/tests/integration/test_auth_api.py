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


def should_return_401_when_no_auth_header(client):
    assert client.get("/me").status_code == 401


def should_return_user_profile_with_valid_token(client):
    client.post("/register", json={"email": "user@example.com", "password": "securepass123"})
    token = client.post("/login", json={"email": "user@example.com", "password": "securepass123"}).get_json()["access_token"]
    response = client.get("/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.get_json()["email"] == "user@example.com"
