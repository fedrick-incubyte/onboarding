import bcrypt


def hash_password(plain_password: str) -> str:
    """
    Hashes a plain text password using bcrypt with an auto-generated salt.
    The returned string contains the salt embedded — store it as-is.
    Never call this with an already-hashed password.
    """
    return bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt()).decode()
