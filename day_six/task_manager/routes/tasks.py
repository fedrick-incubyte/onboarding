from flask import Blueprint, jsonify
from flask_pydantic import validate

from task_manager.schemas import TaskCreateBody, TaskListQuery
from task_manager.services import task_service
from task_manager.workers.notify_task import send_task_notification

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.get("/tasks")
@validate(query=TaskListQuery)
def list_tasks(query: TaskListQuery):
    if query.cursor_id is not None:
        return jsonify(task_service.list_tasks_by_cursor(query))
    return jsonify(task_service.list_tasks(query))


@tasks_bp.get("/tasks/<int:task_id>")
def get_task(task_id: int):
    task = task_service.get_task(task_id)
    return jsonify(task.to_dict())


@tasks_bp.post("/tasks")
@validate()
def create_task(body: TaskCreateBody):
    task = task_service.create_task(body)
    send_task_notification.delay(task.id)
    return jsonify(task.to_dict()), 201
