"""Integration tests for the projects routes."""


def should_return_401_when_creating_project_without_auth(client):
    response = client.post("/projects/", json={"name": "Work"})
    assert response.status_code == 401
