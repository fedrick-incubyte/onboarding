"""Flask application factory."""
from flask import Flask
from flask_cors import CORS

from app.config import config_map
from app.database import db


def create_app(config_name: str = "default") -> Flask:
    """Create and configure a Flask app instance for the given environment."""
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_map[config_name])
    db.init_app(flask_app)
    CORS(flask_app, origins=[flask_app.config["FRONTEND_URL"]])
    from app.routes.auth import auth_bp
    from app.routes.users import users_bp
    from app.routes.tags import tags_bp
    from app.routes.projects import projects_bp
    flask_app.register_blueprint(auth_bp)
    flask_app.register_blueprint(users_bp)
    flask_app.register_blueprint(tags_bp)
    flask_app.register_blueprint(projects_bp)
    return flask_app
