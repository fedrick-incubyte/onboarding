"""Tag ORM model and task_tags association table."""
from sqlalchemy import Column, ForeignKey, Integer, String, Table

from app.database import db
from app.models.base import TimestampMixin

task_tags = Table(
    "task_tags",
    db.metadata,
    Column("task_id", Integer, ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)


class Tag(TimestampMixin, db.Model):
    """A label that can be applied to many tasks."""

    __tablename__ = "tags"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(50), nullable=False, unique=True)
    color: str = db.Column(db.String(7), nullable=False)
