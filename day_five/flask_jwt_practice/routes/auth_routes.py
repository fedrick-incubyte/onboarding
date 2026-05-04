from flask import Blueprint, Response, jsonify, request
from flask_pydantic import validate

from constants import HttpStatus
from database import get_db
from models.user import User
from schemas.auth import RegisterRequest
from services import auth_service

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.post("/register")
@validate()
def register(body: RegisterRequest) -> tuple[Response, int]:
    with get_db() as db:
        user = User(email=body.email, hashed_password=auth_service.hash_password(body.password))
        db.add(user)
        db.flush()
        return jsonify({"message": "User registered successfully", "user_id": user.id}), HttpStatus.CREATED
