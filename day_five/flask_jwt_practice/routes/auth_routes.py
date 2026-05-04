from flask import Blueprint, Response, jsonify
from flask_pydantic import validate

from constants import HttpStatus
from database import get_db
from exceptions import EmailAlreadyRegisteredError
from schemas.auth import RegisterRequest
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
