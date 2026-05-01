from flask import Blueprint
from flask_pydantic import validate
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.database import db
from app.models.tag import Tag
from app.schemas.tag import TagCreate, TagResponse

tags_bp = Blueprint('tags', __name__, url_prefix='/tags')

@tags_bp.post('/')
@validate()
def create_tag(body: TagCreate):
    tag = Tag(name=body.name, color=body.color)
    db.session.add(tag)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {'error': 'Tag name already exists'}, 409
    return TagResponse.model_validate(tag).model_dump(mode='json'), 201

@tags_bp.get('/')
def list_tags():
    tags = db.session.scalars(select(Tag)).all()
    return [TagResponse.model_validate(t).model_dump(mode='json') for t in tags], 200

@tags_bp.delete('/<int:tag_id>')
def delete_tag(tag_id: int):
    tag = db.session.get(Tag, tag_id)
    if tag is None:
        return {'error': 'Tag not found'}, 404
    db.session.delete(tag)
    db.session.commit()
    return {}, 204