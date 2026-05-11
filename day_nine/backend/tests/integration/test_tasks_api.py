"""Integration tests for the tasks routes."""


def should_return_401_when_creating_task_without_auth(client):
    response = client.post("/tasks/", json={"title": "Secret"})
    assert response.status_code == 401


def should_return_201_when_creating_task_with_auth(client, register_and_login):
    token = register_and_login()
    response = client.post("/tasks/", json={"title": "Buy milk"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "Buy milk"


def should_only_return_tasks_belonging_to_current_user(client, register_and_login):
    token_a = register_and_login("a@example.com")
    token_b = register_and_login("b@example.com")
    client.post("/tasks/", json={"title": "Task A"}, headers={"Authorization": f"Bearer {token_a}"})
    client.post("/tasks/", json={"title": "Task B"}, headers={"Authorization": f"Bearer {token_b}"})
    tasks = client.get("/tasks/", headers={"Authorization": f"Bearer {token_a}"}).get_json()
    assert len(tasks) == 1 and tasks[0]["title"] == "Task A"


def should_return_404_when_creating_task_in_another_users_project(client, register_and_login):
    token_a = register_and_login("a@example.com")
    token_b = register_and_login("b@example.com")
    pid = client.post("/projects/", json={"name": "A's project"}, headers={"Authorization": f"Bearer {token_a}"}).get_json()["id"]
    response = client.post("/tasks/", json={"title": "Hijack", "project_id": pid}, headers={"Authorization": f"Bearer {token_b}"})
    assert response.status_code == 404


def should_return_200_when_getting_own_task(client, register_and_login):
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}
    task_id = client.post("/tasks/", json={"title": "Read book"}, headers=headers).get_json()["id"]
    response = client.get(f"/tasks/{task_id}", headers=headers)
    assert response.status_code == 200
    assert response.get_json()["title"] == "Read book"


def should_return_200_when_updating_task_title(client, register_and_login):
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}
    task_id = client.post("/tasks/", json={"title": "Old Title"}, headers=headers).get_json()["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "New Title"}, headers=headers)
    assert response.status_code == 200
    assert response.get_json()["title"] == "New Title"
