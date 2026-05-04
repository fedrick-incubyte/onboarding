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
