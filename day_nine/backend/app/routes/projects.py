"""Projects blueprint: CRUD for /projects/."""
from flask import Blueprint, g, jsonify, request

from app.database import db
from app.middleware.jwt_middleware import jwt_required
from app.models.project import Project

projects_bp = Blueprint("projects", __name__)


@projects_bp.post("/projects/")
@jwt_required
def create_project():
    """Create a project owned by the current user."""
    data = request.get_json()
    project = Project(name=data["name"], user_id=g.current_user.id)
    db.session.add(project)
    db.session.commit()
    return jsonify({"id": project.id, "name": project.name}), 201
