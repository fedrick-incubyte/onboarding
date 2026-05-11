"""Pytest fixtures shared across the test suite."""
import os

import pytest
from alembic import command as alembic_command
from alembic.config import Config as AlembicConfig

from app import create_app
from app.database import db as _db

_ALEMBIC_INI = os.path.join(os.path.dirname(__file__), "..", "alembic.ini")


def _run_alembic(direction: str) -> None:
    """Run alembic upgrade head or downgrade base."""
    cfg = AlembicConfig(_ALEMBIC_INI)
    if direction == "up":
        alembic_command.upgrade(cfg, "head")
    else:
        alembic_command.downgrade(cfg, "base")


@pytest.fixture(scope="session")
def app():
    """Session-scoped Flask app with a fresh schema."""
    os.environ["FLASK_ENV"] = "testing"
    application = create_app("testing")
    with application.app_context():
        _run_alembic("down")
        _run_alembic("up")
        yield application
        _db.session.remove()
        _db.engine.dispose()
    _run_alembic("down")


@pytest.fixture
def client(app):
    """Flask test client."""
    return app.test_client()


@pytest.fixture
def register_and_login(client):
    """Return a helper that registers a user and returns their JWT."""
    def _helper(email="user@example.com", password="securepass123"):
        client.post("/register", json={"email": email, "password": password})
        return client.post("/login", json={"email": email, "password": password}).get_json()["access_token"]
    return _helper


@pytest.fixture(autouse=True)
def clean_tables(app):
    """Delete all rows after each test without dropping the schema."""
    yield
    with app.app_context():
        try:
            for table in reversed(_db.metadata.sorted_tables):
                _db.session.execute(table.delete())
            _db.session.commit()
        except Exception:
            _db.session.rollback()
        finally:
            _db.session.remove()
