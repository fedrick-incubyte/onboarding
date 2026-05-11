JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
BCRYPT_ROUNDS = 12
BEARER_PREFIX = "Bearer "


class ErrorMessages:
    AUTHORIZATION_HEADER_MISSING = "Authorization header is missing"
    TOKEN_MISSING = "Token is missing"
    TOKEN_EXPIRED = "Token has expired"
    INVALID_TOKEN = "Invalid token"
    USER_NOT_FOUND = "User not found"
    INVALID_CREDENTIALS = "Invalid email or password"
    EMAIL_ALREADY_REGISTERED = "Email already registered"


class HttpStatus:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    CONFLICT = 409
    UNPROCESSABLE = 422
