def should_hash_password_to_non_plaintext():
    from app.services.auth_service import hash_password
    hashed = hash_password("mysecretpass")
    assert hashed != "mysecretpass"


def should_verify_correct_password():
    from app.services.auth_service import hash_password, verify_password
    hashed = hash_password("mysecretpass")
    assert verify_password("mysecretpass", hashed) is True


def should_reject_wrong_password():
    from app.services.auth_service import hash_password, verify_password
    hashed = hash_password("mysecretpass")
    assert verify_password("wrongpass", hashed) is False


def should_create_jwt_with_sub_and_email_claims(app):
    import jwt as pyjwt
    from app.services.auth_service import create_access_token
    token = create_access_token(user_id=42, email="a@b.com")
    payload = pyjwt.decode(token, options={"verify_signature": False})
    assert payload["sub"] == "42"
    assert payload["email"] == "a@b.com"
