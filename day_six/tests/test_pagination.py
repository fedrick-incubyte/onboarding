def should_return_first_page_with_correct_metadata(client):
    for i in range(5):
        client.post("/tasks", json={"title": f"Task {i}"})

    response = client.get("/tasks?page=1&page_size=3")

    assert response.status_code == 200
    data = response.get_json()
    assert len(data["items"]) == 3
    assert data["total"] == 5
    assert data["page"] == 1
    assert data["page_size"] == 3
    assert data["total_pages"] == 2


def should_return_second_page_with_correct_task_slice(client):
    for i in range(5):
        client.post("/tasks", json={"title": f"Task {i}"})

    response = client.get("/tasks?page=2&page_size=3")

    assert response.status_code == 200
    data = response.get_json()
    assert len(data["items"]) == 2
    assert data["page"] == 2


def should_return_all_tasks_as_list(client):
    client.post("/tasks", json={"title": "Task A"})
    client.post("/tasks", json={"title": "Task B"})

    response = client.get("/tasks")

    assert response.status_code == 200
    data = response.get_json()
    assert len(data["items"]) == 2
