from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def log_notification(task_id: int, title: str, status: str) -> None:
    """Log a mock email notification — stand-in for a real SMTP call."""
    logger.info(
        "Sending email notification: task '%s' is now '%s'",
        title,
        status,
        extra={"task_id": task_id},
    )
