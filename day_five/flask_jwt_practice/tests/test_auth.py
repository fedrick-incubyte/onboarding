from datetime import datetime


# ── Cycle 1 — App Bootstrap ──────────────────────────────────────────────────

def should_return_404_for_unknown_route(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404


# ── Cycle 2 — Public Route ───────────────────────────────────────────────────

def should_return_200_for_public_route(client):
    response = client.get("/public")
    assert response.status_code == 200
