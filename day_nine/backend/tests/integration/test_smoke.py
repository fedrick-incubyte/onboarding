def should_return_404_for_unknown_route(client):
    assert client.get("/nonexistent").status_code == 404


def should_include_cors_header_for_frontend_origin(client):
    r = client.options(
        "/public",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert "Access-Control-Allow-Origin" in r.headers
