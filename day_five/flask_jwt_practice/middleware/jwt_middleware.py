from __future__ import annotations

import functools
import logging
from typing import Callable

from flask import g, jsonify, request

from constants import BEARER_PREFIX, ErrorMessages, HttpStatus
from exceptions import InvalidTokenError, TokenExpiredError

logger = logging.getLogger(__name__)


def jwt_required(route_function: Callable) -> Callable:
    """
    Guards a route by validating the Bearer token in the Authorization header.
    On success, sets g.current_user to the authenticated User for the route to read.
    Returns 401 at the first failing step — header absent, prefix missing,
    signature invalid, token expired, or user no longer in the database.
    """
    @functools.wraps(route_function)
    def decorated(*args, **kwargs):
        from database import get_db
        from services import auth_service, user_service

        auth_value = request.headers.get("Authorization")
        if not auth_value:
            return jsonify({"error": ErrorMessages.AUTHORIZATION_HEADER_MISSING}), HttpStatus.UNAUTHORIZED

        if not auth_value.startswith(BEARER_PREFIX):
            return jsonify({"error": ErrorMessages.TOKEN_MISSING}), HttpStatus.UNAUTHORIZED

        token = auth_value[len(BEARER_PREFIX):]

        try:
            payload = auth_service.decode_access_token(token)
        except TokenExpiredError:
            return jsonify({"error": ErrorMessages.TOKEN_EXPIRED}), HttpStatus.UNAUTHORIZED
        except InvalidTokenError:
            return jsonify({"error": ErrorMessages.INVALID_TOKEN}), HttpStatus.UNAUTHORIZED

        user_id = int(payload["sub"])
        with get_db() as db:
            user = user_service.find_user_by_id(user_id, db)
            if user is None:
                return jsonify({"error": ErrorMessages.USER_NOT_FOUND}), HttpStatus.UNAUTHORIZED

            g.current_user = user
            return route_function(*args, **kwargs)

    return decorated
