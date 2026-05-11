def should_hash_password_to_non_plaintext():
    from app.services.auth_service import hash_password
    hashed = hash_password("mysecretpass")
    assert hashed != "mysecretpass"


def should_verify_correct_password():
    from app.services.auth_service import hash_password, verify_password
    hashed = hash_password("mysecretpass")
    assert verify_password("mysecretpass", hashed) is True
