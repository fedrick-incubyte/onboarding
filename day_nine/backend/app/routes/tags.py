"""Tags blueprint: CRUD for /tags/."""
from flask import Blueprint

from app.middleware.jwt_middleware import jwt_required

tags_bp = Blueprint("tags", __name__)


@tags_bp.post("/tags/")
@jwt_required
def create_tag():
    """Create a new tag. Requires authentication."""
    pass
