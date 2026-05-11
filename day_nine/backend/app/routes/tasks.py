"""Tasks blueprint: CRUD for /tasks/."""
from flask import Blueprint

from app.middleware.jwt_middleware import jwt_required

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.post("/tasks/")
@jwt_required
def create_task():
    """Create a task. Requires authentication."""
    pass
