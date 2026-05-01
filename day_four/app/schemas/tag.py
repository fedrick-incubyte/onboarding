import re
from pydantic import BaseModel, ConfigDict, field_validator

class TagCreate(BaseModel):
    name: str
    color: str

    @field_validator('color')
    @classmethod
    def color_must_be_hex(cls, v: str) -> str:
        if not re.fullmatch(r'#[0-9A-Fa-f]{6}', v):
            raise ValueError('color must be a valid hex color (e.g. #FF0000)')
        return v

class TagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    color: str