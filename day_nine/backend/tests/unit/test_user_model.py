def should_have_email_field():
    from app.models.user import User
    assert hasattr(User, "email")
