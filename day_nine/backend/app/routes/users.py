"""Users blueprint: GET /me."""
from flask import Blueprint, jsonify, g

from app.middleware.jwt_middleware import jwt_required

users_bp = Blueprint("users", __name__)


@users_bp.get("/me")
@jwt_required
def me():
    """Return the current authenticated user's profile."""
    return jsonify({"email": g.current_user.email, "id": g.current_user.id}), 200
