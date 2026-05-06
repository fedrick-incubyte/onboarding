from __future__ import annotations


class TaskNotFoundError(Exception):
    """Raised when a task id does not exist in the database."""


class InvalidSortFieldError(Exception):
    """Raised when the sort parameter is not in SORTABLE_FIELDS."""
