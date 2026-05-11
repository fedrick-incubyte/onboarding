"""Unit tests for the jwt_required decorator."""
from app.middleware.jwt_middleware import jwt_required


def should_preserve_function_name_with_functools_wraps():
    @jwt_required
    def dummy():
        return "ok"

    assert dummy.__name__ == "dummy"
