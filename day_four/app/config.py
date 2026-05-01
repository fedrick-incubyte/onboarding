import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    FLASK_PYDANTIC_VALIDATION_ERROR_STATUS_CODE = 422

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://localhost/taskmanager_dev')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL', 'postgresql://localhost/taskmanager_test')

config_map = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}