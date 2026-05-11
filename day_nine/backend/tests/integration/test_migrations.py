"""Integration tests verifying database schema matches migrations."""
from sqlalchemy import inspect


def should_have_user_id_column_on_projects_table(app):
    from app.database import db
    with app.app_context():
        cols = {c["name"] for c in inspect(db.engine).get_columns("projects")}
    assert "user_id" in cols
