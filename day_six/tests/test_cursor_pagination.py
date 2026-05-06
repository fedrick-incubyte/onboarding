def should_return_tasks_after_cursor_id_with_next_cursor(client):
    for i in range(5):
        client.post("/tasks", json={"title": f"Task {i}"})

    response = client.get("/tasks?cursor_id=2&page_size=2")

    assert response.status_code == 200
    data = response.get_json()
    assert len(data["items"]) == 2
    assert all(t["id"] > 2 for t in data["items"])
    assert data["next_cursor"] == data["items"][-1]["id"]
    assert data["has_more"] is True
