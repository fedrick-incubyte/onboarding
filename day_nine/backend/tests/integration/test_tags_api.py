"""Integration tests for the tags routes."""


def should_return_401_when_creating_tag_without_auth(client):
    response = client.post("/tags/", json={"name": "urgent", "color": "#FF0000"})
    assert response.status_code == 401
