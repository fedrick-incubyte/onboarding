"""JWT authentication decorator for Flask routes."""
from functools import wraps

from flask import g, jsonify, request

from app.constants import BEARER_PREFIX, ErrorMessages, HttpStatus


def jwt_required(route_function):
    """Protect a route by verifying the Bearer JWT in the Authorization header."""
    @wraps(route_function)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"error": ErrorMessages.AUTHORIZATION_HEADER_MISSING}), HttpStatus.UNAUTHORIZED
        from app.exceptions import TokenExpiredError, InvalidTokenError
        from app.services.auth_service import decode_access_token
        from app.services.user_service import find_user_by_id
        from app.database import db
        token = auth_header[len(BEARER_PREFIX):]
        try:
            payload = decode_access_token(token)
        except TokenExpiredError:
            return jsonify({"error": ErrorMessages.TOKEN_EXPIRED}), HttpStatus.UNAUTHORIZED
        except InvalidTokenError:
            return jsonify({"error": ErrorMessages.INVALID_TOKEN}), HttpStatus.UNAUTHORIZED
        g.current_user = find_user_by_id(int(payload["sub"]), db.session)
        return route_function(*args, **kwargs)

    return decorated
