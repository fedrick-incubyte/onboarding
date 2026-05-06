from datetime import datetime


def should_sort_tasks_by_due_date_descending_when_order_is_desc(client):
    client.post("/tasks", json={"title": "Earlier task", "due_date": "2026-01-01T00:00:00"})
    client.post("/tasks", json={"title": "Later task", "due_date": "2026-06-01T00:00:00"})

    response = client.get("/tasks?sort=due_date&order=desc")

    assert response.status_code == 200
    data = response.get_json()
    assert data["items"][0]["title"] == "Later task"
    assert data["items"][1]["title"] == "Earlier task"


def should_sort_tasks_by_due_date_ascending_by_default(client):
    client.post("/tasks", json={"title": "Later task", "due_date": "2026-06-01T00:00:00"})
    client.post("/tasks", json={"title": "Earlier task", "due_date": "2026-01-01T00:00:00"})

    response = client.get("/tasks?sort=due_date")

    assert response.status_code == 200
    data = response.get_json()
    assert data["items"][0]["title"] == "Earlier task"
    assert data["items"][1]["title"] == "Later task"
