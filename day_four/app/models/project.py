from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from app.database import db
from app.models.base import TimestampMixin

class Project(TimestampMixin, db.Model):
    __tablename__ = 'projects'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    tasks: Mapped[List['Task']] = relationship(
        'Task', back_populates='project', cascade='all, delete-orphan'
    )
