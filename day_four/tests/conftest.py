import os
import pytest
from alembic.config import Config as AlembicConfig
from alembic import command as alembic_command
from app import create_app
from app.database import db as _db

_ALEMBIC_INI = os.path.join(os.path.dirname(__file__), '..', 'alembic.ini')


def _run_alembic(direction: str) -> None:
    cfg = AlembicConfig(_ALEMBIC_INI)
    if direction == 'up':
        alembic_command.upgrade(cfg, 'head')
    else:
        alembic_command.downgrade(cfg, 'base')


@pytest.fixture(scope='session')
def app():
    os.environ['FLASK_ENV'] = 'testing'
    application = create_app('testing')
    _run_alembic('down')
    _run_alembic('up')
    with application.app_context():
        yield application
        _db.session.remove()
        _db.engine.dispose()
    _run_alembic('down')


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db_session(app):
    with app.app_context():
        yield _db.session


@pytest.fixture(autouse=True)
def clean_tables(app):
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
