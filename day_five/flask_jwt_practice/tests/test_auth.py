
def should_return_404_for_unknown_route(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404
