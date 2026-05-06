from __future__ import annotations

from typing import Any, Dict, List

from task_manager.models import Task, db
from task_manager.schemas import TaskCreateBody


def list_tasks() -> Dict[str, Any]:
    """Return all tasks as a paginated envelope."""
    tasks = Task.query.all()
    return {"items": [t.to_dict() for t in tasks]}


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
