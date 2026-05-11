import pytest
import jwt as pyjwt
from datetime import datetime, timezone, timedelta

from app.constants import JWT_ALGORITHM
from app.exceptions import TokenExpiredError, InvalidTokenError
from app.services.auth_service import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token,
)


def should_hash_password_to_non_plaintext():
    hashed = hash_password("mysecretpass")
    assert hashed != "mysecretpass"


def should_verify_correct_password():
    hashed = hash_password("mysecretpass")
    assert verify_password("mysecretpass", hashed) is True


def should_reject_wrong_password():
    hashed = hash_password("mysecretpass")
    assert verify_password("wrongpass", hashed) is False


def should_create_jwt_with_sub_and_email_claims(app):
    token = create_access_token(user_id=42, email="a@b.com")
    payload = pyjwt.decode(token, options={"verify_signature": False})
    assert payload["sub"] == "42"
    assert payload["email"] == "a@b.com"


def should_raise_token_expired_error_for_expired_token(app):
    expired = pyjwt.encode(
        {"sub": "1", "exp": datetime.now(timezone.utc) - timedelta(seconds=1)},
        app.config["SECRET_KEY"],
        algorithm=JWT_ALGORITHM,
    )
    with pytest.raises(TokenExpiredError):
        decode_access_token(expired)


def should_raise_invalid_token_error_for_tampered_token(app):
    with pytest.raises(InvalidTokenError):
        decode_access_token("garbage.token.value")
