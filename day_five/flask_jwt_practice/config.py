import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY: str = os.environ["SECRET_KEY"]
    DATABASE_URL: str = os.environ["DATABASE_URL"]
    TESTING: bool = False


class TestingConfig(Config):
    DATABASE_URL: str = os.environ["TEST_DATABASE_URL"]
    TESTING: bool = True
