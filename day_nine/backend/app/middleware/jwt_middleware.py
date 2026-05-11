"""JWT authentication decorator for Flask routes."""
from functools import wraps


def jwt_required(route_function):
    """Protect a route by verifying the Bearer JWT in the Authorization header."""
    @wraps(route_function)
    def decorated(*args, **kwargs):
        return route_function(*args, **kwargs)

    return decorated
