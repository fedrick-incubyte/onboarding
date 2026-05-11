"""Projects blueprint: CRUD for /projects/."""
from flask import Blueprint, g, jsonify, request
from sqlalchemy import select

from app.database import db
from app.middleware.jwt_middleware import jwt_required
from app.models.project import Project

projects_bp = Blueprint("projects", __name__)


@projects_bp.get("/projects/")
@jwt_required
def list_projects():
    """List projects owned by the current user."""
    projects = db.session.execute(
        select(Project).where(Project.user_id == g.current_user.id)
    ).scalars().all()
    return jsonify([{"id": p.id, "name": p.name} for p in projects]), 200


@projects_bp.post("/projects/")
@jwt_required
def create_project():
    """Create a project owned by the current user."""
    data = request.get_json()
    project = Project(name=data["name"], user_id=g.current_user.id)
    db.session.add(project)
    db.session.commit()
    return jsonify({"id": project.id, "name": project.name}), 201
