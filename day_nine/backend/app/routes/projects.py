"""Projects blueprint: CRUD for /projects/."""
from flask import Blueprint

from app.middleware.jwt_middleware import jwt_required

projects_bp = Blueprint("projects", __name__)


@projects_bp.post("/projects/")
@jwt_required
def create_project():
    """Create a project. Requires authentication."""
    pass
