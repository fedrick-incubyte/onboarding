"""Unit tests for the Task ORM model."""
from datetime import date, timedelta

import app.models  # noqa — ensures all models are registered before any test runs
from app.models.task import Task
from app.enums import TaskStatus


def should_have_user_id_on_task():
    assert hasattr(Task, "user_id")


def should_be_overdue_when_due_date_is_past_and_not_done():
    task = Task()
    task.status = TaskStatus.TODO.value
    task.due_date = date.today() - timedelta(days=1)
    assert task.is_overdue is True


def should_not_be_overdue_when_status_is_done():
    task = Task()
    task.status = TaskStatus.DONE.value
    task.due_date = date.today() - timedelta(days=5)
    assert task.is_overdue is False


def should_not_be_overdue_when_no_due_date():
    task = Task()
    task.status = TaskStatus.TODO.value
    task.due_date = None
    assert task.is_overdue is False


def should_not_be_overdue_when_due_date_is_today():
    task = Task()
    task.status = TaskStatus.TODO.value
    task.due_date = date.today()
    assert task.is_overdue is False


def should_not_be_overdue_when_in_progress_and_due_today():
    task = Task()
    task.status = TaskStatus.IN_PROGRESS.value
    task.due_date = date.today()
    assert task.is_overdue is False
