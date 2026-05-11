"""User ORM model."""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import db
from app.models.base import TimestampMixin


class User(TimestampMixin, db.Model):
    """Represents an authenticated user account."""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
