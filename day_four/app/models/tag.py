from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from app.database import db
from app.models.base import TimestampMixin

task_tags = Table(
    'task_tags',
    db.metadata,
    Column('task_id', Integer, ForeignKey('tasks.id', ondelete='CASCADE'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id', ondelete='CASCADE'), primary_key=True),
)

class Tag(TimestampMixin, db.Model):
    __tablename__ = 'tags'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    color: Mapped[str] = mapped_column(String(7), nullable=False)
    tasks: Mapped[List['Task']] = relationship(
        'Task', secondary=task_tags, back_populates='tags'
    )