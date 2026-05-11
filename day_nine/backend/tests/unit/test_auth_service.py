def should_hash_password_to_non_plaintext():
    from app.services.auth_service import hash_password
    hashed = hash_password("mysecretpass")
    assert hashed != "mysecretpass"
