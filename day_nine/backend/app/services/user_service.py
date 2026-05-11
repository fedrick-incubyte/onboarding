"""User registration and authentication logic."""
from typing import Optional

from sqlalchemy import select

from app.exceptions import EmailAlreadyRegisteredError
from app.models.user import User
from app.services.auth_service import hash_password


def find_user_by_email(email: str, session) -> Optional[User]:
    """Return the User with the given email, or None."""
    return session.execute(select(User).where(User.email == email)).scalar_one_or_none()


def register_user(email: str, plain_password: str, session) -> User:
    """Create a new User. Raises EmailAlreadyRegisteredError if email is taken."""
    if find_user_by_email(email, session) is not None:
        raise EmailAlreadyRegisteredError(f"{email} is already registered")
    user = User(email=email, hashed_password=hash_password(plain_password))
    session.add(user)
    return user
