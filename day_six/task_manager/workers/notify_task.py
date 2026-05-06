from __future__ import annotations

from task_manager.services import notification_service
from task_manager.workers.celery_app import celery_app


@celery_app.task
def send_task_notification(task_id: int, title: str, status: str) -> None:
    """Log a mock email notification for the given task."""
    notification_service.log_notification(task_id, title, status)
