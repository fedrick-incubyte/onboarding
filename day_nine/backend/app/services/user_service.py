"""User registration and authentication logic."""
from typing import Optional

from sqlalchemy import select

from app.exceptions import EmailAlreadyRegisteredError, InvalidCredentialsError
from app.models.user import User
from app.services.auth_service import hash_password, verify_password, create_access_token


def find_user_by_email(email: str, session) -> Optional[User]:
    """Return the User with the given email, or None."""
    return session.execute(select(User).where(User.email == email)).scalar_one_or_none()


def find_user_by_id(user_id: int, session) -> Optional[User]:
    """Return the User with the given id, or None."""
    return session.get(User, user_id)


def register_user(email: str, plain_password: str, session) -> User:
    """Create a new User. Raises EmailAlreadyRegisteredError if email is taken."""
    if find_user_by_email(email, session) is not None:
        raise EmailAlreadyRegisteredError(f"{email} is already registered")
    user = User(email=email, hashed_password=hash_password(plain_password))
    session.add(user)
    return user


def login_user(email: str, plain_password: str, session) -> str:
    """Authenticate and return a JWT. Raises InvalidCredentialsError on failure."""
    user = find_user_by_email(email, session)
    if user is None or not verify_password(plain_password, user.hashed_password):
        raise InvalidCredentialsError("Invalid email or password")
    return create_access_token(user.id, user.email)
