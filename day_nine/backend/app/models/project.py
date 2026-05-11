"""Project ORM model."""
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.user import User

from app.database import db
from app.models.base import TimestampMixin


class Project(TimestampMixin, db.Model):
    """A collection of related tasks owned by a user."""

    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    user: Mapped["User"] = relationship("User", back_populates="projects")
