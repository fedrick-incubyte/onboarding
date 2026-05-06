def should_return_422_when_title_is_missing_from_request(client):
    response = client.post("/tasks", json={"status": "todo"})

    assert response.status_code == 422
