from http import HTTPStatus

from flask import Blueprint
from flask_pydantic import validate
from app.schemas import UserRegistrationRequest, UserRegistrationResponse, UserPublic

users_bp = Blueprint('users', __name__)


class UserStore:
    def __init__(self):
        self._data: dict = {}

    def exists(self, email: str) -> bool:
        return email in self._data

    def add(self, username: str, email: str) -> None:
        self._data[email] = {"username": username, "email": email}

    def clear(self) -> None:
        self._data.clear()


user_store = UserStore()


@users_bp.route('/api/register', methods=['POST'])
@validate(get_json_params={'silent': True, 'force': True})
def register(body: UserRegistrationRequest):
    if user_store.exists(body.email):
        return {'error': 'Email already registered'}, HTTPStatus.CONFLICT

    user_store.add(body.username, body.email)
    response = UserRegistrationResponse(
        message="User registered successfully",
        user=UserPublic(username=body.username, email=body.email),
    )
    return response, HTTPStatus.CREATED