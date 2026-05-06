from __future__ import annotations

import os

from celery import Celery


def make_celery() -> Celery:
    """Create a Celery instance configured from environment variables."""
    return Celery(
        "task_manager",
        broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
        result_backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0"),
        include=["task_manager.workers.notify_task"],
    )


celery_app = make_celery()
