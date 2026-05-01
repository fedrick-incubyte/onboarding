from flask import Blueprint
from flask_pydantic import validate
from sqlalchemy import select
from app.database import db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

@projects_bp.post('/')
@validate()
def create_project(body: ProjectCreate):
    project = Project(name=body.name, description=body.description)
    db.session.add(project)
    db.session.commit()
    return ProjectResponse.model_validate(project).model_dump(mode='json'), 201

@projects_bp.get('/')
def list_projects():
    projects = db.session.scalars(select(Project)).all()
    return [ProjectResponse.model_validate(p).model_dump(mode='json') for p in projects], 200

@projects_bp.get('/<int:project_id>')
def get_project(project_id: int):
    project = db.session.get(Project, project_id)
    if project is None:
        return {'error': 'Project not found'}, 404
    return ProjectResponse.model_validate(project).model_dump(mode='json'), 200

@projects_bp.put('/<int:project_id>')
@validate()
def update_project(project_id: int, body: ProjectUpdate):
    project = db.session.get(Project, project_id)
    if project is None:
        return {'error': 'Project not found'}, 404
    if body.name is not None:
        project.name = body.name
    if 'description' in body.model_fields_set:
        project.description = body.description
    db.session.commit()
    return ProjectResponse.model_validate(project).model_dump(mode='json'), 200

@projects_bp.delete('/<int:project_id>')
def delete_project(project_id: int):
    project = db.session.get(Project, project_id)
    if project is None:
        return {'error': 'Project not found'}, 404
    db.session.delete(project)
    db.session.commit()
    return {}, 204