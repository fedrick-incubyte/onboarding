from __future__ import annotations

import logging

from sqlalchemy.orm import Session

from exceptions import EmailAlreadyRegisteredError
from models.user import User
from services import auth_service

logger = logging.getLogger(__name__)


def find_user_by_email(email: str, db: Session) -> User | None:
    """
    Queries the database for a user with the given email.
    Returns the User if found, None otherwise.
    """
    return db.query(User).filter(User.email == email).first()


def find_user_by_id(user_id: int, db: Session) -> User | None:
    """
    Queries the database for a user with the given id.
    Returns the User if found, None otherwise.
    """
    return db.query(User).filter(User.id == user_id).first()


def login_user(email: str, plain_password: str, db: Session) -> str:
    """
    Authenticates a user and returns a signed JWT access token.
    Raises InvalidCredentialsError if email not found or password does not match.
    The same exception is raised for both failure cases — never reveal which one failed.
    """
    from exceptions import InvalidCredentialsError

    user = find_user_by_email(email, db)
    if user is None or not auth_service.verify_password(plain_password, user.hashed_password):
        logger.warning("Failed login attempt", extra={"email": email})
        raise InvalidCredentialsError("Invalid credentials")

    token = auth_service.create_access_token(user.id, user.email)
    logger.info("User logged in", extra={"user_id": user.id})
    return token


def register_user(email: str, plain_password: str, db: Session) -> User:
    """
    Creates a new user with a hashed password.
    Raises EmailAlreadyRegisteredError if the email is already taken.
    Returns the newly created and persisted User object.
    """
    if find_user_by_email(email, db) is not None:
        raise EmailAlreadyRegisteredError("Email already registered")

    user = User(email=email, hashed_password=auth_service.hash_password(plain_password))
    db.add(user)
    db.flush()
    logger.info("User registered", extra={"user_id": user.id})
    return user
