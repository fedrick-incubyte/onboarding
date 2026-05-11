"""Integration tests for the projects routes."""


def should_return_401_when_creating_project_without_auth(client):
    response = client.post("/projects/", json={"name": "Work"})
    assert response.status_code == 401


def should_return_201_when_creating_project_with_auth(client, register_and_login):
    token = register_and_login()
    response = client.post("/projects/", json={"name": "Work"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 201
    assert response.get_json()["name"] == "Work"
