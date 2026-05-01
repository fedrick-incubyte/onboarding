from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime, date
from typing import Optional, List
from app.schemas.tag import TagResponse
from app.enums import TaskStatus, TaskPriority
from app.schemas.validators import validate_task_status, validate_task_priority, reject_blank


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = TaskStatus.TODO.value
    priority: str = TaskPriority.MEDIUM.value
    due_date: Optional[date] = None
    project_id: Optional[int] = None
    tags: List[int] = []

    @field_validator('title')
    @classmethod
    def title_must_not_be_blank(cls, v: str) -> str:
        return reject_blank(v, 'title')

    @field_validator('status')
    @classmethod
    def validate_status(cls, v):
        return validate_task_status(v)

    @field_validator('priority')
    @classmethod
    def validate_priority(cls, v):
        return validate_task_priority(v)


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[date] = None
    project_id: Optional[int] = None
    tags: Optional[List[int]] = None

    @field_validator('title')
    @classmethod
    def title_must_not_be_blank(cls, v: Optional[str]) -> Optional[str]:
        return reject_blank(v, 'title')

    @field_validator('status')
    @classmethod
    def validate_status(cls, v):
        return validate_task_status(v)

    @field_validator('priority')
    @classmethod
    def validate_priority(cls, v):
        return validate_task_priority(v)


class TaskListFilters(BaseModel):
    project_id: Optional[int] = None
    status: Optional[str] = None

    @field_validator('status')
    @classmethod
    def validate_status(cls, v):
        return validate_task_status(v)


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)
    id: int
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    due_date: Optional[date] = None
    project_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    tags: List[TagResponse] = []
    is_overdue: bool = False