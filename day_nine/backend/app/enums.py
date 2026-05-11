"""Task status and priority enumerations."""
import enum


class TaskStatus(enum.Enum):
    """Lifecycle states a task can be in."""

    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskPriority(enum.Enum):
    """Importance level of a task."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
