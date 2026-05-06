from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv
from flask import Flask, jsonify

from task_manager.models import db

load_dotenv()


def create_app(test_config: dict[str, Any] | None = None) -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///tasks.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    from task_manager.exceptions import InvalidSortFieldError, TaskNotFoundError
    from task_manager.routes.tasks import tasks_bp

    app.register_blueprint(tasks_bp)

    @app.errorhandler(InvalidSortFieldError)
    def handle_invalid_sort(err: InvalidSortFieldError):
        return jsonify({"error": str(err)}), 400

    @app.errorhandler(TaskNotFoundError)
    def handle_task_not_found(err: TaskNotFoundError):
        return jsonify({"error": str(err)}), 404

    with app.app_context():
        db.create_all()

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    return app
