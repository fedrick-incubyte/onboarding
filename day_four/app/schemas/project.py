from __future__ import annotations
from pydantic import BaseModel, ConfigDict, field_validator, Field
from datetime import datetime
from typing import Optional, List, Annotated
from app.schemas.validators import reject_blank


class ProjectCreate(BaseModel):
    name: Annotated[str, Field(max_length=200)]
    description: Optional[str] = None

    @field_validator('name')
    @classmethod
    def name_must_not_be_blank(cls, v: str) -> str:
        return reject_blank(v, 'name')


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    @field_validator('name')
    @classmethod
    def name_must_not_be_blank(cls, v: Optional[str]) -> Optional[str]:
        return reject_blank(v, 'name')

class TaskSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True, use_enum_values=True)
    id: int
    title: str
    status: str
    priority: str

class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime
    tasks: List[TaskSummary] = []