import functools
from typing import Callable

from flask import jsonify, request

from constants import ErrorMessages, HttpStatus


def jwt_required(route_function: Callable) -> Callable:
    """
    Decorator that guards a route by checking for a valid Authorization header.
    Returns 401 immediately if the header is absent.
    """
    @functools.wraps(route_function)
    def decorated(*args, **kwargs):
        if not request.headers.get("Authorization"):
            return jsonify({"error": ErrorMessages.AUTHORIZATION_HEADER_MISSING}), HttpStatus.UNAUTHORIZED
        return route_function(*args, **kwargs)
    return decorated
