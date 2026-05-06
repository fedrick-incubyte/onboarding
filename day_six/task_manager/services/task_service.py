from __future__ import annotations

import math
from typing import Any, Dict, List

from sqlalchemy import asc, desc
from sqlalchemy.orm import Query

from task_manager.constants import DEFAULT_PAGE_SIZE, SORTABLE_FIELDS
from task_manager.exceptions import InvalidSortFieldError
from task_manager.models import Task, db
from task_manager.schemas import TaskCreateBody, TaskListQuery


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


def _apply_filters(q: Query, query: TaskListQuery) -> Query:
    """Apply status and keyword search filters to the query."""
    if query.status:
        q = q.filter(Task.status == query.status)
    if query.search:
        pattern = f"%{query.search}%"
        q = q.filter(Task.title.ilike(pattern) | Task.description.ilike(pattern))
    return q


def _apply_sort(q: Query, query: TaskListQuery) -> Query:
    """Apply column sort and direction to the query."""
    if not query.sort:
        return q
    if query.sort not in SORTABLE_FIELDS:
        raise InvalidSortFieldError(f"'{query.sort}' is not a sortable field. Choose from: {sorted(SORTABLE_FIELDS)}")
    sort_col = getattr(Task, query.sort)
    direction = desc if query.order == "desc" else asc
    return q.order_by(direction(sort_col))


def list_tasks(query: TaskListQuery) -> Dict[str, Any]:
    """Return tasks with offset-limit pagination, filtering, and page metadata."""
    page_size = query.page_size or DEFAULT_PAGE_SIZE
    q = Task.query
    q = _apply_filters(q, query)
    q = _apply_sort(q, query)
    total = q.count()
    tasks = q.offset((query.page - 1) * page_size).limit(page_size).all()
    return _build_page_response(tasks, total, query.page, page_size)


def list_tasks_by_cursor(query: TaskListQuery) -> Dict[str, Any]:
    """Return tasks with id > cursor_id; avoids COUNT(*) for large tables."""
    page_size = query.page_size or DEFAULT_PAGE_SIZE
    tasks = (
        Task.query.filter(Task.id > query.cursor_id)
        .order_by(Task.id)
        .limit(page_size + 1)
        .all()
    )
    has_more = len(tasks) > page_size
    page_tasks = tasks[:page_size]
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
