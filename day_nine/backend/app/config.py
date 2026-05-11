import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    FLASK_PYDANTIC_VALIDATION_ERROR_STATUS_CODE = 422
    SECRET_KEY = os.environ.get("SECRET_KEY", "test-secret-key-32-chars-minimum!")
    FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:5173")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL")


config_map = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
