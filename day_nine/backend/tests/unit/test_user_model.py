def should_have_email_field():
    from app.models.user import User
    assert hasattr(User, "email")


def should_have_hashed_password_field():
    from app.models.user import User
    assert hasattr(User, "hashed_password")


def should_have_id_and_created_at():
    from app.models.user import User
    assert hasattr(User, "id") and hasattr(User, "created_at")
