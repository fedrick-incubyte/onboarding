import jwt as pyjwt
from datetime import datetime

from tests.conftest import auth_header, login_user, register_user


# ── Cycle 1 — App Bootstrap ──────────────────────────────────────────────────

def should_return_404_for_unknown_route(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404


# ── Cycle 2 — Public Route ───────────────────────────────────────────────────

def should_return_200_for_public_route(client):
    response = client.get("/public")
    assert response.status_code == 200


def should_return_message_and_timestamp_in_public_response(client):
    response = client.get("/public")
    body = response.get_json()
    assert "message" in body
    assert "timestamp" in body
    datetime.fromisoformat(body["timestamp"].replace("Z", "+00:00"))


# ── Cycle 3 — Registration Happy Path ────────────────────────────────────────

def should_return_201_when_registering_with_valid_data(client):
    response = register_user(client)
    assert response.status_code == 201


def should_return_user_id_in_registration_response(client):
    body = register_user(client).get_json()
    assert "user_id" in body
    assert isinstance(body["user_id"], int)


def should_not_return_password_or_hash_in_registration_response(client):
    body = register_user(client).get_json()
    assert "password" not in body
    assert "hashed_password" not in body


# ── Cycle 4 — Registration Validation ────────────────────────────────────────

def should_return_400_when_email_format_is_invalid(client):
    response = client.post("/register", json={"email": "not-an-email", "password": "securepass123"})
    assert response.status_code == 400


def should_return_400_when_password_is_shorter_than_eight_characters(client):
    response = client.post("/register", json={"email": "user@example.com", "password": "short"})
    assert response.status_code == 400


def should_return_400_when_request_body_fields_are_missing(client):
    response = client.post("/register", json={})
    assert response.status_code == 400


# ── Cycle 5 — Duplicate Email ─────────────────────────────────────────────────

def should_return_400_when_email_is_already_registered(client):
    register_user(client)
    response = register_user(client)
    assert response.status_code == 400
    assert response.get_json()["error"] == "Email already registered"


# ── Cycle 6 — Login Happy Path ────────────────────────────────────────────────

def should_return_200_with_access_token_on_valid_login(client):
    register_user(client)
    response = client.post("/login", json={"email": "user@example.com", "password": "securepass123"})
    assert response.status_code == 200
    assert "access_token" in response.get_json()


def should_return_token_type_as_bearer_in_login_response(client):
    register_user(client)
    body = client.post("/login", json={"email": "user@example.com", "password": "securepass123"}).get_json()
    assert body["token_type"] == "bearer"


def should_return_expires_in_seconds_in_login_response(client):
    register_user(client)
    body = client.post("/login", json={"email": "user@example.com", "password": "securepass123"}).get_json()
    assert body["expires_in"] == 1800


def should_include_sub_and_email_claims_in_jwt_payload(client):
    register_user(client)
    body = client.post("/login", json={"email": "user@example.com", "password": "securepass123"}).get_json()
    payload = pyjwt.decode(body["access_token"], options={"verify_signature": False})
    assert "sub" in payload
    assert payload["email"] == "user@example.com"


# ── Cycle 7 — Login Failure Cases ────────────────────────────────────────────

def should_return_401_when_email_is_not_registered(client):
    response = client.post("/login", json={"email": "nobody@example.com", "password": "securepass123"})
    assert response.status_code == 401
    assert response.get_json()["error"] == "Invalid credentials"


def should_return_401_when_password_does_not_match(client):
    register_user(client)
    response = client.post("/login", json={"email": "user@example.com", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.get_json()["error"] == "Invalid credentials"


def should_return_identical_error_for_wrong_password_and_unknown_email(client):
    register_user(client)
    wrong_email_response = client.post("/login", json={"email": "nobody@example.com", "password": "securepass123"})
    wrong_password_response = client.post("/login", json={"email": "user@example.com", "password": "wrongpassword"})
    assert wrong_email_response.get_json()["error"] == wrong_password_response.get_json()["error"]


# ── Cycle 8 — Protected Route Stub ───────────────────────────────────────────

def should_return_401_when_no_authorization_header_is_sent_to_protected_route(client):
    response = client.get("/me")
    assert response.status_code == 401
    assert response.get_json()["error"] == "Authorization header missing"


# ── Cycle 9 — JWT Middleware Built Incrementally ──────────────────────────────

def should_return_401_when_authorization_header_is_missing_bearer_prefix(client):
    response = client.get("/me", headers={"Authorization": "Token sometoken"})
    assert response.status_code == 401
    assert response.get_json()["error"] == "Token missing"


def should_return_401_when_token_signature_has_been_tampered_with(client):
    register_user(client)
    token = login_user(client)
    tampered = token[:-5] + "XXXXX"
    response = client.get("/me", headers=auth_header(tampered))
    assert response.status_code == 401
    assert response.get_json()["error"] == "Invalid token"


def should_return_401_when_token_has_expired(client):
    import jwt as pyjwt
    from datetime import timedelta, timezone
    from config import Config
    from constants import JWT_ALGORITHM
    register_user(client)
    payload = {"sub": "1", "email": "user@example.com", "exp": datetime.now(timezone.utc) - timedelta(seconds=1)}
    expired_token = pyjwt.encode(payload, Config.SECRET_KEY, algorithm=JWT_ALGORITHM)
    response = client.get("/me", headers=auth_header(expired_token))
    assert response.status_code == 401
    assert response.get_json()["error"] == "Token has expired"


def should_return_401_when_user_in_token_no_longer_exists_in_database(client):
    import jwt as pyjwt
    from config import Config
    from constants import JWT_ALGORITHM
    from datetime import timedelta, timezone
    token = pyjwt.encode(
        {"sub": "99999", "email": "ghost@example.com", "exp": datetime.now(timezone.utc) + timedelta(minutes=30)},
        Config.SECRET_KEY, algorithm=JWT_ALGORITHM,
    )
    response = client.get("/me", headers=auth_header(token))
    assert response.status_code == 401
    assert response.get_json()["error"] == "User not found"


# ── Cycle 10 — Protected Route Returns Data ───────────────────────────────────

def should_return_200_with_user_email_when_token_is_valid(client):
    register_user(client)
    token = login_user(client)
    response = client.get("/me", headers=auth_header(token))
    assert response.status_code == 200
    body = response.get_json()
    assert body["email"] == "user@example.com"
    assert "user_id" in body
    assert "created_at" in body


def should_return_data_for_the_authenticated_user_not_any_other_user(client):
    register_user(client, email="a@example.com", password="securepass123")
    register_user(client, email="b@example.com", password="securepass123")
    token = login_user(client, email="b@example.com", password="securepass123")
    response = client.get("/me", headers=auth_header(token))
    assert response.get_json()["email"] == "b@example.com"


# ── Cycle 11 — Public Route Unchanged by Token ───────────────────────────────

def should_return_200_on_public_route_even_when_a_valid_token_is_sent(client):
    register_user(client)
    token = login_user(client)
    response = client.get("/public", headers=auth_header(token))
    assert response.status_code == 200
    assert "message" in response.get_json()
