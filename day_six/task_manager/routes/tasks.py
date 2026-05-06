from flask import Blueprint, jsonify, request
from flask_pydantic import validate

from task_manager.schemas import TaskCreateBody
from task_manager.services import task_service

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.get("/tasks")
def list_tasks():
    cursor_id = request.args.get("cursor_id", type=int)
    page_size = request.args.get("page_size", None, type=int)
    if cursor_id is not None:
        return jsonify(task_service.list_tasks_by_cursor(cursor_id=cursor_id, page_size=page_size))
    page = request.args.get("page", 1, type=int)
    status = request.args.get("status")
    return jsonify(task_service.list_tasks(page=page, page_size=page_size, status=status))


@tasks_bp.post("/tasks")
@validate()
def create_task(body: TaskCreateBody):
    task = task_service.create_task(body)
    return jsonify(task.to_dict()), 201
