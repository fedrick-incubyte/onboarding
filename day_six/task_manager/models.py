from __future__ import annotations

from datetime import datetime
from typing import Any

from flask_sqlalchemy import SQLAlchemy

from task_manager.constants import TASK_STATUS_TODO

db = SQLAlchemy()


class Task(db.Model):
    """Persistent task entity."""

    __tablename__ = "task"

    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(255), nullable=False)
    description: str = db.Column(db.Text, default="")
    status: str = db.Column(db.String(20), nullable=False, default=TASK_STATUS_TODO)
    due_date: datetime | None = db.Column(db.DateTime, nullable=True)
    created_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self) -> dict[str, Any]:
        """Serialize task to a JSON-safe dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "created_at": self.created_at.isoformat(),
        }
