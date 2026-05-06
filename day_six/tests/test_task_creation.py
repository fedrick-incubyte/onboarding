def should_create_task_and_return_201_with_task_data(client):
    response = client.post("/tasks", json={"title": "Buy milk", "status": "todo"})

    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Buy milk"
    assert data["status"] == "todo"
    assert "id" in data
    assert "created_at" in data
