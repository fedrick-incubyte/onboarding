"""Domain exceptions raised by services and caught by route handlers."""


class EmailAlreadyRegisteredError(Exception):
    """Raised when registering with an email that already exists."""
    pass


class InvalidCredentialsError(Exception):
    """Raised when email or password does not match during login."""
    pass


class TokenExpiredError(Exception):
    """Raised when a JWT has passed its expiration time."""
    pass


class InvalidTokenError(Exception):
    """Raised when a JWT is malformed or its signature is invalid."""
    pass


class UserNotFoundError(Exception):
    """Raised when a user ID from a token no longer exists in the database."""
    pass
