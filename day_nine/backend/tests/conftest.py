import os
import pytest
from app import create_app


@pytest.fixture(scope="session")
def app():
    os.environ["FLASK_ENV"] = "testing"
    return create_app("testing")


@pytest.fixture
def client(app):
    return app.test_client()
