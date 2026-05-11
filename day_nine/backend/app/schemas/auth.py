"""Pydantic schemas for auth request validation."""
from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
    """Payload for POST /register."""

    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    """Payload for POST /login."""

    email: EmailStr
    password: str
