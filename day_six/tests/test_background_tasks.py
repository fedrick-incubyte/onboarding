import logging
from unittest.mock import patch

from task_manager.workers.notify_task import send_task_notification


def should_retry_notification_task_on_transient_failure():
    from unittest.mock import ANY
    from task_manager.constants import NOTIFICATION_MAX_RETRIES, NOTIFICATION_RETRY_COUNTDOWN

    assert send_task_notification.max_retries == NOTIFICATION_MAX_RETRIES

    with patch(
        "task_manager.workers.notify_task.notification_service.log_notification",
        side_effect=Exception("SMTP timeout"),
    ):
        with patch.object(
            send_task_notification, "retry", side_effect=Exception("retried")
        ) as mock_retry:
            try:
                send_task_notification.apply(args=[1, "Deploy", "todo"])
            except Exception:
                pass

    mock_retry.assert_called_once_with(exc=ANY, countdown=NOTIFICATION_RETRY_COUNTDOWN)


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
