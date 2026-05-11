"""User ORM model."""
from typing import TYPE_CHECKING, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import db
from app.models.base import TimestampMixin

if TYPE_CHECKING:
    from app.models.project import Project


class User(TimestampMixin, db.Model):
    """Represents an authenticated user account."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    projects: Mapped[List["Project"]] = relationship("Project", back_populates="user")
