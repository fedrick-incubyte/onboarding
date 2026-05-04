from __future__ import annotations

from datetime import datetime, timedelta, timezone

import bcrypt
import jwt

from constants import ACCESS_TOKEN_EXPIRE_MINUTES, JWT_ALGORITHM


def hash_password(plain_password: str) -> str:
    """
    Hashes a plain text password using bcrypt with an auto-generated salt.
    The returned string contains the salt embedded — store it as-is.
    Never call this with an already-hashed password.
    """
    return bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt()).decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compares a plain password against a stored bcrypt hash using
    constant-time comparison to prevent timing attacks.
    Returns True if matched. Returns False for any mismatch or error.
    Never raises.
    """
    try:
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
    except Exception:
        return False


def create_access_token(user_id: int, email: str) -> str:
    """
    Builds and signs a JWT with payload: sub, email, iat, exp.
    Expiry is set to ACCESS_TOKEN_EXPIRE_MINUTES from now (UTC).
    Returns the encoded token string.
    """
    from config import Config

    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user_id),
        "email": email,
        "iat": now,
        "exp": now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm=JWT_ALGORITHM)
