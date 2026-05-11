"""Flask application factory."""
from flask import Flask
from flask_cors import CORS

from app.config import config_map
from app.database import db


def create_app(config_name: str = "default") -> Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_map[config_name])
    db.init_app(flask_app)
    CORS(flask_app, origins=[flask_app.config["FRONTEND_URL"]])
    return flask_app
