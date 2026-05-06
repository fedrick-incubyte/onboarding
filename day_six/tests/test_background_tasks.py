from unittest.mock import patch


def should_queue_notification_task_after_task_creation(client):
    with patch("task_manager.routes.tasks.send_task_notification") as mock_task:
        response = client.post("/tasks", json={"title": "Send report"})

    assert response.status_code == 201
    mock_task.delay.assert_called_once_with(response.get_json()["id"])
