from datetime import datetime


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
    response = client.post("/register", json={"email": "user@example.com", "password": "securepass123"})
    assert response.status_code == 201


def should_return_user_id_in_registration_response(client):
    response = client.post("/register", json={"email": "user@example.com", "password": "securepass123"})
    body = response.get_json()
    assert "user_id" in body
    assert isinstance(body["user_id"], int)


def should_not_return_password_or_hash_in_registration_response(client):
    response = client.post("/register", json={"email": "user@example.com", "password": "securepass123"})
    body = response.get_json()
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
