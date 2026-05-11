def should_return_404_for_unknown_route(client):
    assert client.get("/nonexistent").status_code == 404
