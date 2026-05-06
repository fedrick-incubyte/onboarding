from __future__ import annotations

import math
from typing import Any, Dict, List, Optional

from task_manager.constants import DEFAULT_PAGE_SIZE
from task_manager.models import Task, db
from task_manager.schemas import TaskCreateBody


def _build_page_response(
    tasks: List[Task], total: int, page: int, page_size: int
) -> Dict[str, Any]:
    """Build the standard pagination envelope."""
    return {
        "items": [t.to_dict() for t in tasks],
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": math.ceil(total / page_size) if total else 0,
    }


def list_tasks(page: int = 1, page_size: Optional[int] = None) -> Dict[str, Any]:
    """Return tasks with offset-limit pagination and page metadata."""
    effective_size = page_size or DEFAULT_PAGE_SIZE
    total = Task.query.count()
    tasks = Task.query.offset((page - 1) * effective_size).limit(effective_size).all()
    return _build_page_response(tasks, total, page, effective_size)


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
