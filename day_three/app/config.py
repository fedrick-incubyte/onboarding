class Config:
    FLASK_PYDANTIC_VALIDATION_ERROR_STATUS_CODE = 422


class TestingConfig(Config):
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True


config_map = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}