class ErrorMessages:
    INVALID_CREDENTIALS = "Invalid credentials"
    EMAIL_ALREADY_REGISTERED = "Email already registered"
    AUTHORIZATION_HEADER_MISSING = "Authorization header missing"
    TOKEN_MISSING = "Token missing"
    INVALID_TOKEN = "Invalid token"
    TOKEN_EXPIRED = "Token has expired"
    USER_NOT_FOUND = "User not found"


class HttpStatus:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    UNPROCESSABLE = 422


JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
BCRYPT_ROUNDS = 12
BEARER_PREFIX = "Bearer "
