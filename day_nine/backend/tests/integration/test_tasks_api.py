"""Integration tests for the tasks routes."""


def should_return_401_when_creating_task_without_auth(client):
    response = client.post("/tasks/", json={"title": "Secret"})
    assert response.status_code == 401


def should_return_201_when_creating_task_with_auth(client, register_and_login):
    token = register_and_login()
    response = client.post("/tasks/", json={"title": "Buy milk"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "Buy milk"
