from __future__ import annotations

from task_manager.constants import NOTIFICATION_MAX_RETRIES, NOTIFICATION_RETRY_COUNTDOWN
from task_manager.services import notification_service
from task_manager.workers.celery_app import celery_app


@celery_app.task(bind=True, max_retries=NOTIFICATION_MAX_RETRIES)
def send_task_notification(self, task_id: int, title: str, status: str) -> None:
    """Log a mock email notification; retries up to max_retries on transient failure."""
    try:
        notification_service.log_notification(task_id, title, status)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=NOTIFICATION_RETRY_COUNTDOWN)
