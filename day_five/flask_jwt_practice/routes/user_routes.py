from flask import Blueprint, Response, jsonify

user_blueprint = Blueprint("user", __name__)


@user_blueprint.get("/public")
def public() -> tuple[Response, int]:
    """Public endpoint — no authentication required."""
    return jsonify({"message": "ok"}), 200
