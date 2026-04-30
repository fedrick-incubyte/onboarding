from flask import Flask
from app.config import config_map


def create_app(config_name: str = 'default') -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_map[config_name])

    from app.users import users_bp
    app.register_blueprint(users_bp)

    return app