from datetime import date, timedelta
from app.models.task import Task, TaskStatus


def should_be_overdue_when_due_date_is_past_and_not_done():
    task = Task()
    task.status = TaskStatus.TODO
    task.due_date = date.today() - timedelta(days=1)
    assert task.is_overdue is True


def should_not_be_overdue_when_status_is_done():
    task = Task()
    task.status = TaskStatus.DONE
    task.due_date = date.today() - timedelta(days=5)
    assert task.is_overdue is False


def should_not_be_overdue_when_no_due_date():
    task = Task()
    task.status = TaskStatus.TODO
    task.due_date = None
    assert task.is_overdue is False


def should_not_be_overdue_when_due_date_is_today():
    task = Task()
    task.status = TaskStatus.TODO
    task.due_date = date.today()
    assert task.is_overdue is False


def should_not_be_overdue_when_in_progress_and_due_today():
    task = Task()
    task.status = TaskStatus.IN_PROGRESS
    task.due_date = date.today()
    assert task.is_overdue is False


def should_be_overdue_when_in_progress_and_due_date_is_past():
    task = Task()
    task.status = TaskStatus.IN_PROGRESS
    task.due_date = date.today() - timedelta(days=1)
    assert task.is_overdue is True
