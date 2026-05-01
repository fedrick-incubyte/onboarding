from app.enums import TaskStatus, TaskPriority


def validate_task_status(v):
    if v is None:
        return v
    valid = {s.value for s in TaskStatus}
    if v not in valid:
        raise ValueError(f'status must be one of: {", ".join(sorted(valid))}')
    return v


def validate_task_priority(v):
    if v is None:
        return v
    valid = {p.value for p in TaskPriority}
    if v not in valid:
        raise ValueError(f'priority must be one of: {", ".join(sorted(valid))}')
    return v


def reject_blank(v, field_name: str):
    if v is not None and not v.strip():
        raise ValueError(f'{field_name} must not be blank')
    return v