"""Flask configuration classes selected by FLASK_ENV."""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration — shared defaults."""
    FLASK_PYDANTIC_VALIDATION_ERROR_STATUS_CODE = 422
    SECRET_KEY = os.environ.get("SECRET_KEY", "test-secret-key-32-chars-minimum!")
    FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:5173")


class DevelopmentConfig(Config):
    """Local development: debug mode on, uses DATABASE_URL."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(Config):
    """Test suite: TESTING flag on, uses TEST_DATABASE_URL."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL")


config_map = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
