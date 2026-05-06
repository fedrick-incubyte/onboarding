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


def list_tasks(
    page: int = 1,
    page_size: Optional[int] = None,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """Return tasks with offset-limit pagination and page metadata."""
    effective_size = page_size or DEFAULT_PAGE_SIZE
    query = Task.query
    if status:
        query = query.filter(Task.status == status)
    total = query.count()
    tasks = query.offset((page - 1) * effective_size).limit(effective_size).all()
    return _build_page_response(tasks, total, page, effective_size)


def list_tasks_by_cursor(cursor_id: int, page_size: Optional[int] = None) -> Dict[str, Any]:
    """Return tasks with id > cursor_id; avoids COUNT(*) for large tables."""
    effective_size = page_size or DEFAULT_PAGE_SIZE
    tasks = (
        Task.query.filter(Task.id > cursor_id)
        .order_by(Task.id)
        .limit(effective_size + 1)
        .all()
    )
    has_more = len(tasks) > effective_size
    page_tasks = tasks[:effective_size]
    return {
        "items": [t.to_dict() for t in page_tasks],
        "next_cursor": page_tasks[-1].id if page_tasks else None,
        "has_more": has_more,
    }


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
