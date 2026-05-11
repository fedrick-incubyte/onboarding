def should_have_email_field():
    from app.models.user import User
    assert hasattr(User, "email")


def should_have_hashed_password_field():
    from app.models.user import User
    assert hasattr(User, "hashed_password")
