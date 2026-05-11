"""Unit tests for the Task ORM model."""


def should_have_user_id_on_task():
    from app.models.task import Task
    assert hasattr(Task, "user_id")
