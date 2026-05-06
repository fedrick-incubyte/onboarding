import pytest
from task_manager.app import create_app
from task_manager.models import db as _db
from task_manager.workers.celery_app import celery_app


@pytest.fixture(autouse=True)
def configure_celery_for_tests():
    """Run Celery tasks synchronously with an in-memory broker — no Redis needed."""
    celery_app.conf.update(
        task_always_eager=True,
        task_eager_propagates=True,
        broker_url="memory://",
        result_backend="cache+memory://",
    )


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
