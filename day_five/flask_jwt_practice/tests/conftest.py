import os

import pytest
from alembic import command as alembic_command
from alembic.config import Config as AlembicConfig

from app import create_app


@pytest.fixture(scope="function")
def client():
    """
    Provides a Flask test client with a clean database state for every test.
    Uses Alembic downgrade/upgrade instead of metadata.create_all so the test
    schema is always driven by the same versioned migrations as production.
    """
    app = create_app(config="testing")
    alembic_cfg = AlembicConfig("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", os.environ["TEST_DATABASE_URL"])
    alembic_command.downgrade(alembic_cfg, "base")
    alembic_command.upgrade(alembic_cfg, "head")
    with app.test_client() as c:
        yield c
    alembic_command.downgrade(alembic_cfg, "base")


# ── Helpers ──────────────────────────────────────────────────────────────────

def register_user(client, email: str = "user@example.com", password: str = "securepass123"):
    """Registers a user and returns the full response."""
    return client.post("/register", json={"email": email, "password": password})


def login_user(client, email: str = "user@example.com", password: str = "securepass123") -> str:
    """Logs in a user and returns the access token string."""
    response = client.post("/login", json={"email": email, "password": password})
    return response.get_json()["access_token"]


def auth_header(token: str) -> dict:
    """Returns an Authorization header dict for use in protected requests."""
    return {"Authorization": f"Bearer {token}"}
