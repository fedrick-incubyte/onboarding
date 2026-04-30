import pytest
from app import create_app
from app.users import user_store


@pytest.fixture(scope='function')
def app():
    app = create_app('testing')
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True)
def reset_store():
    user_store.clear()
    yield
    user_store.clear()