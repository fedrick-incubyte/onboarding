"""Import all models so SQLAlchemy metadata is populated."""
from app.models.user import User  # noqa
from app.models.project import Project  # noqa
from app.models.task import Task  # noqa
