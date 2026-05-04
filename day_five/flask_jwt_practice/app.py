from flask import Flask

from config import Config, TestingConfig


def create_app(config: str = "default") -> Flask:
    """
    Application factory — creates and returns a configured Flask instance.
    Accepts a config name so tests can inject TestingConfig without patching globals.
    """
    configs = {
        "testing": TestingConfig,
    }
    app = Flask(__name__)
    app.config.from_object(configs.get(config, Config))
    return app
