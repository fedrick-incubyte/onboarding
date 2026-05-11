"""Auth blueprint: POST /register and POST /login."""
from flask import Blueprint, jsonify
from flask_pydantic import validate

from app.database import db
from app.exceptions import EmailAlreadyRegisteredError, InvalidCredentialsError
from app.schemas.auth import RegisterRequest, LoginRequest
from app.services.user_service import register_user, login_user

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


@auth_bp.post("/login")
@validate()
def login(body: LoginRequest):
    """Authenticate a user and return a JWT access token."""
    try:
        token = login_user(body.email, body.password, db.session)
        return jsonify({"access_token": token, "token_type": "bearer"}), 200
    except InvalidCredentialsError as exc:
        return jsonify({"error": str(exc)}), 401
