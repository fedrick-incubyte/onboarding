import re

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator, model_validator

_PASSWORD_SPECIAL_CHARS = r'[@$!%*?&]'
_PASSWORD_SPECIAL_CHARS_DISPLAY = '@$!%*?&'


class UserRegistrationRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    username: str = Field(min_length=3, max_length=50, pattern=r'^[a-zA-Z0-9_]+$')
    email: EmailStr
    password: str
    confirm_password: str

    @field_validator('password')
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'[0-9]', v):
            raise ValueError('Password must contain at least one digit')
        if not re.search(_PASSWORD_SPECIAL_CHARS, v):
            raise ValueError(f'Password must contain at least one special character ({_PASSWORD_SPECIAL_CHARS_DISPLAY})')
        return v

    @model_validator(mode='after')
    def passwords_match(self) -> 'UserRegistrationRequest':
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self


class UserPublic(BaseModel):
    username: str
    email: str


class UserRegistrationResponse(BaseModel):
    message: str
    user: UserPublic