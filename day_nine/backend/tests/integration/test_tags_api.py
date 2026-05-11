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


def should_return_200_with_tag_list(client):
    token = _register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/tags/", json={"name": "urgent", "color": "#FF0000"}, headers=headers)
    response = client.get("/tags/", headers=headers)
    assert response.status_code == 200
    assert len(response.get_json()) == 1


def should_return_204_when_deleting_tag(client):
    token = _register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    tag_id = client.post("/tags/", json={"name": "urgent", "color": "#FF0000"}, headers=headers).get_json()["id"]
    response = client.delete(f"/tags/{tag_id}", headers=headers)
    assert response.status_code == 204


def should_return_409_for_duplicate_tag_name(client):
    token = _register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/tags/", json={"name": "urgent", "color": "#FF0000"}, headers=headers)
    response = client.post("/tags/", json={"name": "urgent", "color": "#00FF00"}, headers=headers)
    assert response.status_code == 409


def should_return_422_for_invalid_hex_color(client):
    token = _register_and_login(client)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/tags/", json={"name": "urgent", "color": "not-a-color"}, headers=headers)
    assert response.status_code == 422
