"""Tags blueprint: CRUD for /tags/."""
from flask import Blueprint, jsonify, request

from app.database import db
from app.middleware.jwt_middleware import jwt_required
from app.models.tag import Tag

tags_bp = Blueprint("tags", __name__)


@tags_bp.get("/tags/")
@jwt_required
def list_tags():
    """List all tags. Requires authentication."""
    tags = db.session.execute(db.select(Tag)).scalars().all()
    return jsonify([{"id": t.id, "name": t.name, "color": t.color} for t in tags]), 200


@tags_bp.post("/tags/")
@jwt_required
def create_tag():
    """Create a new tag. Requires authentication."""
    data = request.get_json()
    tag = Tag(name=data["name"], color=data["color"])
    db.session.add(tag)
    db.session.commit()
    return jsonify({"id": tag.id, "name": tag.name, "color": tag.color}), 201
