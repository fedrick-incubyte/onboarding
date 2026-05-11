"""Pydantic schemas for tag validation."""
import re

from pydantic import BaseModel, field_validator


class TagCreate(BaseModel):
    """Payload for creating a new tag."""

    name: str
    color: str

    @field_validator("color")
    @classmethod
    def color_must_be_hex(cls, v: str) -> str:
        """Reject colors that are not 6-digit hex codes like #FF0000."""
        if not re.fullmatch(r"#[0-9A-Fa-f]{6}", v):
            raise ValueError("color must be a valid hex color (e.g. #FF0000)")
        return v
