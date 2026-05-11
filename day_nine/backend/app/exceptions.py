class EmailAlreadyRegisteredError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class TokenExpiredError(Exception):
    pass


class InvalidTokenError(Exception):
    pass


class UserNotFoundError(Exception):
    pass
