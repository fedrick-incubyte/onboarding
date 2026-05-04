from flask import Blueprint, Response, jsonify
from flask_pydantic import validate

from constants import ACCESS_TOKEN_EXPIRE_MINUTES, HttpStatus
from database import get_db
from exceptions import EmailAlreadyRegisteredError, InvalidCredentialsError
from schemas.auth import LoginRequest, RegisterRequest
from services import user_service

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.post("/register")
@validate()
def register(body: RegisterRequest) -> tuple[Response, int]:
    try:
        with get_db() as db:
            user = user_service.register_user(body.email, body.password, db)
            return jsonify({"message": "User registered successfully", "user_id": user.id}), HttpStatus.CREATED
    except EmailAlreadyRegisteredError as error:
        return jsonify({"error": str(error)}), HttpStatus.BAD_REQUEST


@auth_blueprint.post("/login")
@validate()
def login(body: LoginRequest) -> tuple[Response, int]:
    try:
        with get_db() as db:
            token = user_service.login_user(body.email, body.password, db)
            return jsonify({
                "access_token": token,
                "token_type": "bearer",
                "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            }), HttpStatus.OK
    except InvalidCredentialsError as error:
        return jsonify({"error": str(error)}), HttpStatus.UNAUTHORIZED
