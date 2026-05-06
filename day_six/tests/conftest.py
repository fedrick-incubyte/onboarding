import pytest
from task_manager.app import create_app
from task_manager.models import db as _db


@pytest.fixture()
def app():
    """Flask app configured for testing with an in-memory SQLite database."""
    flask_app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with flask_app.app_context():
        _db.create_all()
        yield flask_app
        _db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()
