from __future__ import annotations

from task_manager.models import Task, db
from task_manager.schemas import TaskCreateBody


def create_task(data: TaskCreateBody) -> Task:
    """Persist a new task and return the saved instance."""
    task = Task(
        title=data.title,
        description=data.description,
        status=data.status,
        due_date=data.due_date,
    )
    db.session.add(task)
    db.session.commit()
    return task
