"""SQLAlchemy database instance shared across the application."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Declarative base for all ORM models."""
    pass


db = SQLAlchemy(model_class=Base)
