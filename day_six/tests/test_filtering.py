def should_filter_tasks_by_search_keyword_in_title_and_description(client):
    client.post("/tasks", json={"title": "Buy groceries", "description": "milk and eggs"})
    client.post("/tasks", json={"title": "Call dentist", "description": "book appointment"})

    response = client.get("/tasks?search=milk")

    assert response.status_code == 200
    data = response.get_json()
    assert len(data["items"]) == 1
    assert data["items"][0]["title"] == "Buy groceries"


def should_filter_tasks_by_status(client):
    client.post("/tasks", json={"title": "Done task", "status": "done"})
    client.post("/tasks", json={"title": "Todo task", "status": "todo"})

    response = client.get("/tasks?status=done")

    assert response.status_code == 200
    data = response.get_json()
    assert len(data["items"]) == 1
    assert data["items"][0]["status"] == "done"
