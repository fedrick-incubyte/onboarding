from flask import Blueprint, jsonify
from flask_pydantic import validate

from task_manager.schemas import TaskCreateBody, TaskListQuery
from task_manager.services import task_service

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.get("/tasks")
@validate(query=TaskListQuery)
def list_tasks(query: TaskListQuery):
    if query.cursor_id is not None:
        return jsonify(task_service.list_tasks_by_cursor(query))
    return jsonify(task_service.list_tasks(query))


@tasks_bp.post("/tasks")
@validate()
def create_task(body: TaskCreateBody):
    task = task_service.create_task(body)
    return jsonify(task.to_dict()), 201
