from flask import Blueprint, jsonify, request
from flask_pydantic import validate

from task_manager.schemas import TaskCreateBody
from task_manager.services import task_service

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.get("/tasks")
def list_tasks():
    page = request.args.get("page", 1, type=int)
    page_size = request.args.get("page_size", None, type=int)
    return jsonify(task_service.list_tasks(page=page, page_size=page_size))


@tasks_bp.post("/tasks")
@validate()
def create_task(body: TaskCreateBody):
    task = task_service.create_task(body)
    return jsonify(task.to_dict()), 201
