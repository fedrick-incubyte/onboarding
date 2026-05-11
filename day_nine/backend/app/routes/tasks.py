"""Tasks blueprint: CRUD for /tasks/."""
from flask import Blueprint, g, jsonify, request
from sqlalchemy import select

from app.database import db
from app.enums import TaskPriority, TaskStatus
from app.middleware.jwt_middleware import jwt_required
from app.models.task import Task

tasks_bp = Blueprint("tasks", __name__)


def _task_dict(task: Task) -> dict:
    """Serialise a Task to a plain dict for JSON responses."""
    return {
        "id": task.id,
        "title": task.title,
        "status": task.status,
        "priority": task.priority,
        "due_date": task.due_date.isoformat() if task.due_date else None,
        "project_id": task.project_id,
        "is_overdue": task.is_overdue,
    }


@tasks_bp.get("/tasks/")
@jwt_required
def list_tasks():
    """List tasks owned by the current user."""
    tasks = db.session.execute(
        select(Task).where(Task.user_id == g.current_user.id)
    ).scalars().all()
    return jsonify([_task_dict(t) for t in tasks]), 200


@tasks_bp.post("/tasks/")
@jwt_required
def create_task():
    """Create a task owned by the current user."""
    data = request.get_json()
    task = Task(
        title=data["title"],
        user_id=g.current_user.id,
        status=data.get("status", TaskStatus.TODO.value),
        priority=data.get("priority", TaskPriority.MEDIUM.value),
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(_task_dict(task)), 201
