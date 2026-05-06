def should_return_200_from_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def should_create_tasks_table_with_expected_columns(app):
    from sqlalchemy import inspect
    from task_manager.models import db

    with app.app_context():
        inspector = inspect(db.engine)
        columns = {col["name"] for col in inspector.get_columns("task")}

    assert {"id", "title", "description", "status", "due_date", "created_at"} <= columns
