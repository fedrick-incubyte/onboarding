class EmailAlreadyRegisteredError(Exception):
    """Raised when attempting to register an email that already exists."""


class InvalidCredentialsError(Exception):
    """Raised when login fails due to wrong email or wrong password."""


class TokenExpiredError(Exception):
    """Raised when a JWT has passed its expiry time."""


class InvalidTokenError(Exception):
    """Raised when a JWT signature is invalid or the token is malformed."""


class UserNotFoundError(Exception):
    """Raised when a user_id from a JWT payload has no matching DB record."""
