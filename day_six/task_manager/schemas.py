from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from task_manager.constants import TASK_STATUS_TODO


class TaskCreateBody(BaseModel):
    title: str
    description: Optional[str] = ""
    status: Optional[str] = TASK_STATUS_TODO
    due_date: Optional[datetime] = None


class TaskListQuery(BaseModel):
    page: Optional[int] = 1
    page_size: Optional[int] = None
    cursor_id: Optional[int] = None
    status: Optional[str] = None
    search: Optional[str] = None
    sort: Optional[str] = None
    order: Optional[str] = "asc"
