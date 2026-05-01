from flask import Blueprint
from flask_pydantic import validate
from sqlalchemy import select
from app.database import db
from app.models.task import Task
from app.enums import TaskStatus, TaskPriority
from app.models.tag import Tag
from app.models.project import Project
from app.schemas.task import TaskCreate, TaskUpdate, TaskListFilters, TaskResponse

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_bp.post('/')
@validate()
def create_task(body: TaskCreate):
    if body.project_id is not None and db.session.get(Project, body.project_id) is None:
        return {'error': 'Project not found'}, 404
    data = body.model_dump(exclude={'tags'})
    task = Task(**data)
    if body.tags:
        task.tags = db.session.query(Tag).filter(Tag.id.in_(body.tags)).all()
    db.session.add(task)
    db.session.commit()
    return TaskResponse.model_validate(task).model_dump(mode='json'), 201

@tasks_bp.get('/')
@validate()
def list_tasks(query: TaskListFilters):
    stmt = select(Task)
    if query.project_id is not None:
        stmt = stmt.where(Task.project_id == query.project_id)
    if query.status is not None:
        stmt = stmt.where(Task.status == TaskStatus(query.status))
    tasks = db.session.scalars(stmt).all()
    return [TaskResponse.model_validate(t).model_dump(mode='json') for t in tasks], 200

@tasks_bp.get('/<int:task_id>')
def get_task(task_id: int):
    task = db.session.get(Task, task_id)
    if task is None:
        return {'error': 'Task not found'}, 404
    return TaskResponse.model_validate(task).model_dump(mode='json'), 200

@tasks_bp.put('/<int:task_id>')
@validate()
def update_task(task_id: int, body: TaskUpdate):
    task = db.session.get(Task, task_id)
    if task is None:
        return {'error': 'Task not found'}, 404
    if body.title is not None:
        task.title = body.title
    if 'description' in body.model_fields_set:
        task.description = body.description
    if body.status is not None:
        task.status = TaskStatus(body.status)
    if body.priority is not None:
        task.priority = TaskPriority(body.priority)
    if 'due_date' in body.model_fields_set:
        task.due_date = body.due_date
    if body.project_id is not None:
        task.project_id = body.project_id
    if body.tags is not None:
        task.tags = db.session.query(Tag).filter(Tag.id.in_(body.tags)).all()
    db.session.commit()
    return TaskResponse.model_validate(task).model_dump(mode='json'), 200

@tasks_bp.delete('/<int:task_id>')
def delete_task(task_id: int):
    task = db.session.get(Task, task_id)
    if task is None:
        return {'error': 'Task not found'}, 404
    db.session.delete(task)
    db.session.commit()
    return {}, 204

@tasks_bp.post('/<int:task_id>/tags/<int:tag_id>')
def attach_tag(task_id: int, tag_id: int):
    task = db.session.get(Task, task_id)
    if task is None:
        return {'error': 'Task not found'}, 404
    tag = db.session.get(Tag, tag_id)
    if tag is None:
        return {'error': 'Tag not found'}, 404
    if tag not in task.tags:
        task.tags.append(tag)
        db.session.commit()
    return TaskResponse.model_validate(task).model_dump(mode='json'), 200

@tasks_bp.delete('/<int:task_id>/tags/<int:tag_id>')
def detach_tag(task_id: int, tag_id: int):
    task = db.session.get(Task, task_id)
    if task is None:
        return {'error': 'Task not found'}, 404
    tag = db.session.get(Tag, tag_id)
    if tag is None:
        return {'error': 'Tag not found'}, 404
    if tag not in task.tags:
        return {'error': 'Tag not attached to task'}, 404
    task.tags.remove(tag)
    db.session.commit()
    return {}, 204