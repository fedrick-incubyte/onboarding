"""Integration tests for the tasks routes."""


def should_return_401_when_creating_task_without_auth(client):
    response = client.post("/tasks/", json={"title": "Secret"})
    assert response.status_code == 401
