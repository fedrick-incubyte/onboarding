"""Integration tests for user_service — hit the real database."""
import pytest

from app.database import db
from app.exceptions import EmailAlreadyRegisteredError
from app.services.user_service import register_user


def should_register_user_and_persist(app):
    with app.app_context():
        user = register_user("a@b.com", "pass12345", db.session)
        db.session.commit()
        assert user.id is not None


def should_raise_on_duplicate_email(app):
    with app.app_context():
        register_user("a@b.com", "pass12345", db.session)
        db.session.commit()
        with pytest.raises(EmailAlreadyRegisteredError):
            register_user("a@b.com", "other", db.session)
