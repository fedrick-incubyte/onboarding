"""Task ORM model."""
from sqlalchemy import Date, Enum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import db
from app.enums import TaskPriority, TaskStatus
from app.models.base import TimestampMixin


class Task(TimestampMixin, db.Model):
    """A unit of work owned by a user, optionally grouped in a project."""

    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(Enum(TaskStatus, values_callable=lambda e: [i.value for i in e]), nullable=False, default=TaskStatus.TODO.value)
    priority: Mapped[str] = mapped_column(Enum(TaskPriority, values_callable=lambda e: [i.value for i in e]), nullable=False, default=TaskPriority.MEDIUM.value)
    due_date: Mapped[object] = mapped_column(Date, nullable=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=True)
