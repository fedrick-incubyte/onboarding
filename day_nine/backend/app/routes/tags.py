"""Tags blueprint: CRUD for /tags/."""
from flask import Blueprint, jsonify
from flask_pydantic import validate
from sqlalchemy.exc import IntegrityError

from app.database import db
from app.middleware.jwt_middleware import jwt_required
from app.models.tag import Tag
from app.schemas.tag import TagCreate

tags_bp = Blueprint("tags", __name__)


def _tag_dict(tag: Tag) -> dict:
    """Serialise a Tag to a plain dict for JSON responses."""
    return {"id": tag.id, "name": tag.name, "color": tag.color}


@tags_bp.get("/tags/")
@jwt_required
def list_tags():
    """List all tags. Requires authentication."""
    tags = db.session.execute(db.select(Tag)).scalars().all()
    return jsonify([_tag_dict(t) for t in tags]), 200


@tags_bp.post("/tags/")
@jwt_required
@validate()
def create_tag(body: TagCreate):
    """Create a new tag. Requires authentication."""
    tag = Tag(name=body.name, color=body.color)
    db.session.add(tag)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Tag name already exists"}), 409
    return jsonify(_tag_dict(tag)), 201


@tags_bp.delete("/tags/<int:tag_id>")
@jwt_required
def delete_tag(tag_id: int):
    """Delete a tag by id. Requires authentication."""
    tag = db.session.get(Tag, tag_id)
    db.session.delete(tag)
    db.session.commit()
    return "", 204
