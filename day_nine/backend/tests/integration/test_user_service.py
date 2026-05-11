"""Integration tests for user_service — hit the real database."""
import pytest

from app.database import db
from app.exceptions import EmailAlreadyRegisteredError, InvalidCredentialsError
from app.services.user_service import register_user, login_user


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


def should_login_and_return_token(app):
    with app.app_context():
        register_user("a@b.com", "pass12345", db.session)
        db.session.commit()
        token = login_user("a@b.com", "pass12345", db.session)
        assert isinstance(token, str) and len(token) > 10


def should_raise_invalid_credentials_for_wrong_password(app):
    with app.app_context():
        register_user("a@b.com", "pass12345", db.session)
        db.session.commit()
        with pytest.raises(InvalidCredentialsError):
            login_user("a@b.com", "wrongpass", db.session)
