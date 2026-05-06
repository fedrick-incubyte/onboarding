def should_return_404_for_nonexistent_task_id(client):
    response = client.get("/tasks/9999")

    assert response.status_code == 404
    assert "error" in response.get_json()


def should_return_422_when_title_is_missing_from_request(client):
    response = client.post("/tasks", json={"status": "todo"})

    assert response.status_code == 422
