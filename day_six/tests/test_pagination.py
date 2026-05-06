def should_return_all_tasks_as_list(client):
    client.post("/tasks", json={"title": "Task A"})
    client.post("/tasks", json={"title": "Task B"})

    response = client.get("/tasks")

    assert response.status_code == 200
    data = response.get_json()
    assert len(data["items"]) == 2
