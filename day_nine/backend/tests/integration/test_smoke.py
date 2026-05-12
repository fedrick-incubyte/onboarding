def should_return_404_for_unknown_route(client):
    assert client.get("/nonexistent").status_code == 404


def should_include_cors_header_for_frontend_origin(client):
    r = client.options(
        "/register",
        headers={
            "Origin": "http://localhost:5174",
            "Access-Control-Request-Method": "POST",
        },
    )
    assert "Access-Control-Allow-Origin" in r.headers
