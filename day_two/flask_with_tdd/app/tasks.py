import uuid

from flask import Blueprint, jsonify, request

tasks_bp = Blueprint('tasks', __name__)

tasks = []


@tasks_bp.get('/tasks')
def get_tasks():
    return tasks, 200


def _make_task(title):
    return {'id': str(uuid.uuid4()), 'title': title, 'done': False}


def _find_task(task_id):
    return next((t for t in tasks if t['id'] == task_id), None)


def _validate_task_body(body):
    if not body or 'title' not in body:
        return False, "'title' is required"
    return True, None


def _find_task_or_abort(task_id):
    task = _find_task(task_id)
    if task is None:
        return None, ({'error': 'Not found'}, 404)
    return task, None


@tasks_bp.post('/tasks')
def create_task():
    body = request.get_json()
    ok, err_msg = _validate_task_body(body)
    if not ok:
        return {'error': err_msg}, 400
    task = _make_task(body['title'])
    tasks.append(task)
    return task, 201


@tasks_bp.get('/tasks/<task_id>')
def get_task(task_id):
    task, err = _find_task_or_abort(task_id)
    if err:
        return err
    return task, 200


@tasks_bp.put('/tasks/<task_id>')
def update_task(task_id):
    task, err = _find_task_or_abort(task_id)
    if err:
        return err
    body = request.get_json()
    task.update({k: v for k, v in body.items() if k in ('title', 'done')})
    return task, 200


@tasks_bp.delete('/tasks/<task_id>')
def delete_task(task_id):
    task, err = _find_task_or_abort(task_id)
    if err:
        return err
    tasks.remove(task)
    return '', 204
