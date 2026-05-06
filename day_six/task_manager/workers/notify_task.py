from __future__ import annotations

from task_manager.workers.celery_app import celery_app


@celery_app.task
def send_task_notification(task_id: int) -> None:
    """Queue entry point — delegates to notification_service once implemented."""
    pass
