"""Auth blueprint: POST /register and POST /login."""
from flask import Blueprint, jsonify
from flask_pydantic import validate

from app.database import db
from app.exceptions import EmailAlreadyRegisteredError
from app.schemas.auth import RegisterRequest
from app.services.user_service import register_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/register")
@validate()
def register(body: RegisterRequest):
    """Register a new user account."""
    try:
        register_user(body.email, body.password, db.session)
        db.session.commit()
        return jsonify({"message": "User registered"}), 201
    except EmailAlreadyRegisteredError as exc:
        return jsonify({"error": str(exc)}), 400
