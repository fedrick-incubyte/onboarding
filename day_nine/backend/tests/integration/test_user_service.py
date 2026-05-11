"""Integration tests for user_service — hit the real database."""
from app.database import db
from app.services.user_service import register_user


def should_register_user_and_persist(app):
    with app.app_context():
        user = register_user("a@b.com", "pass12345", db.session)
        db.session.commit()
        assert user.id is not None
