"""User registration and authentication logic."""
from app.models.user import User
from app.services.auth_service import hash_password


def register_user(email: str, plain_password: str, session) -> User:
    """Create a new User with a hashed password and add it to the session."""
    user = User(email=email, hashed_password=hash_password(plain_password))
    session.add(user)
    return user
