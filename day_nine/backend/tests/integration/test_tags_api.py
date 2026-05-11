"""Integration tests for the tags routes."""


def should_return_401_when_creating_tag_without_auth(client):
    response = client.post("/tags/", json={"name": "urgent", "color": "#FF0000"})
    assert response.status_code == 401


def _register_and_login(client, email="user@example.com", password="securepass123"):
    client.post("/register", json={"email": email, "password": password})
    return client.post("/login", json={"email": email, "password": password}).get_json()["access_token"]


def should_return_201_when_creating_tag_with_auth(client):
    token = _register_and_login(client)
    response = client.post("/tags/", json={"name": "urgent", "color": "#FF0000"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 201
