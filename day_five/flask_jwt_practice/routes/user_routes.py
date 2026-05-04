from datetime import datetime, timezone

from flask import Blueprint, Response, g, jsonify

from middleware.jwt_middleware import jwt_required

user_blueprint = Blueprint("user", __name__)


@user_blueprint.get("/public")
def public() -> tuple[Response, int]:
    """Public endpoint — no authentication required."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return jsonify({
        "message": "This is a public route. No token needed.",
        "timestamp": timestamp,
    }), 200


@user_blueprint.get("/me")
@jwt_required
def me() -> tuple[Response, int]:
    """Protected endpoint — returns the authenticated user's profile."""
    user = g.current_user
    return jsonify({
        "user_id": user.id,
        "email": user.email,
        "created_at": user.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }), 200
