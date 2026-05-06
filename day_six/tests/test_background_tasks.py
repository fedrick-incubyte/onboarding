import logging
from unittest.mock import patch


def should_log_email_payload_when_notification_task_executes(client, caplog):
    with caplog.at_level(logging.INFO):
        client.post("/tasks", json={"title": "Deploy hotfix", "status": "todo"})

    assert any("Deploy hotfix" in record.message for record in caplog.records)


def should_queue_notification_task_after_task_creation(client):
    with patch("task_manager.routes.tasks.send_task_notification") as mock_task:
        response = client.post("/tasks", json={"title": "Send report"})

    data = response.get_json()
    assert response.status_code == 201
    mock_task.delay.assert_called_once_with(data["id"], data["title"], data["status"])
