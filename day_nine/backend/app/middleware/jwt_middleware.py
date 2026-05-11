"""JWT authentication decorator for Flask routes."""
from functools import wraps

from flask import jsonify, request

from app.constants import ErrorMessages, HttpStatus


def jwt_required(route_function):
    """Protect a route by verifying the Bearer JWT in the Authorization header."""
    @wraps(route_function)
    def decorated(*args, **kwargs):
        if not request.headers.get("Authorization"):
            return jsonify({"error": ErrorMessages.AUTHORIZATION_HEADER_MISSING}), HttpStatus.UNAUTHORIZED
        return route_function(*args, **kwargs)

    return decorated
