from datetime import date
from typing import List, Optional
from sqlalchemy import String, Text, Enum as SAEnum, Date, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import db
from app.enums import TaskStatus, TaskPriority
from app.models.base import TimestampMixin
from app.models.tag import task_tags

class Task(TimestampMixin, db.Model):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[TaskStatus] = mapped_column(
        SAEnum(TaskStatus, native_enum=False, values_callable=lambda x: [e.value for e in x]),
        default=TaskStatus.TODO, nullable=False,
    )
    priority: Mapped[TaskPriority] = mapped_column(
        SAEnum(TaskPriority, native_enum=False, values_callable=lambda x: [e.value for e in x]),
        default=TaskPriority.MEDIUM, nullable=False,
    )
    due_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    project_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey('projects.id', ondelete='CASCADE'), nullable=True
    )
    project: Mapped[Optional['Project']] = relationship('Project', back_populates='tasks')
    tags: Mapped[List['Tag']] = relationship('Tag', secondary=task_tags, back_populates='tasks')

    @property
    def is_overdue(self) -> bool:
        if self.due_date is None:
            return False
        return self.due_date < date.today() and self.status != TaskStatus.DONE
