from flask import Blueprint, Response, jsonify
from flask_pydantic import validate

from constants import ACCESS_TOKEN_EXPIRE_MINUTES, ErrorMessages, HttpStatus
from database import get_db
from exceptions import EmailAlreadyRegisteredError, InvalidCredentialsError
from models.user import User
from schemas.auth import LoginRequest, RegisterRequest
from services import auth_service, user_service

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
            user = user_service.find_user_by_email(body.email, db)
            if user is None or not auth_service.verify_password(body.password, user.hashed_password):
                raise InvalidCredentialsError(ErrorMessages.INVALID_CREDENTIALS)
            token = auth_service.create_access_token(user.id, user.email)
            return jsonify({
                "access_token": token,
                "token_type": "bearer",
                "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            }), HttpStatus.OK
    except InvalidCredentialsError as error:
        return jsonify({"error": str(error)}), HttpStatus.UNAUTHORIZED
