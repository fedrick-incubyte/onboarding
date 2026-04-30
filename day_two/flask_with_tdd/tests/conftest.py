import pytest
import app.tasks as tasks_module
from app import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True)
def reset_tasks():
    tasks_module.tasks.clear()
    yield
    # tasks_module.tasks.clear()