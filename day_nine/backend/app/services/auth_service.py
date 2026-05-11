"""Cryptography and JWT utilities. No database access — pure functions."""
from datetime import datetime, timezone, timedelta

import bcrypt
import jwt

from app.constants import JWT_ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


def _secret_key() -> str:
    """Read the signing secret from the active Flask app config."""
    from flask import current_app
    return current_app.config["SECRET_KEY"]


def hash_password(plain_password: str) -> str:
    """Return a bcrypt hash of plain_password."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain_password.encode(), salt).decode()


def verify_password(plain_password: str, hashed: str) -> bool:
    """Return True if plain_password matches the bcrypt hash."""
    try:
        return bcrypt.checkpw(plain_password.encode(), hashed.encode())
    except (ValueError, TypeError):
        return False


def create_access_token(user_id: int, email: str) -> str:
    """Encode a signed JWT with sub, email, iat, and exp claims."""
    payload = {
        "sub": str(user_id),
        "email": email,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, _secret_key(), algorithm=JWT_ALGORITHM)


def decode_access_token(token: str) -> dict:
    """Decode and verify a JWT. Raises TokenExpiredError or InvalidTokenError."""
    from app.exceptions import TokenExpiredError, InvalidTokenError
    try:
        return jwt.decode(token, _secret_key(), algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise TokenExpiredError("Token has expired")
    except jwt.DecodeError:
        raise InvalidTokenError("Invalid token")
