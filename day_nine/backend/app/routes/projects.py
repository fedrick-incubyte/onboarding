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


def _get_owned_project(project_id: int):
    """Return the project if owned by the current user, else None."""
    return db.session.execute(
        select(Project).where(Project.id == project_id, Project.user_id == g.current_user.id)
    ).scalar_one_or_none()


@projects_bp.get("/projects/<int:project_id>")
@jwt_required
def get_project(project_id: int):
    """Return a single project owned by the current user or 404."""
    project = _get_owned_project(project_id)
    if project is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"id": project.id, "name": project.name}), 200


@projects_bp.put("/projects/<int:project_id>")
@jwt_required
def update_project(project_id: int):
    """Update a project owned by the current user."""
    project = _get_owned_project(project_id)
    if project is None:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    if "name" in data:
        project.name = data["name"]
    db.session.commit()
    return jsonify({"id": project.id, "name": project.name}), 200


@projects_bp.post("/projects/")
@jwt_required
def create_project():
    """Create a project owned by the current user."""
    data = request.get_json()
    project = Project(name=data["name"], user_id=g.current_user.id)
    db.session.add(project)
    db.session.commit()
    return jsonify({"id": project.id, "name": project.name}), 201
