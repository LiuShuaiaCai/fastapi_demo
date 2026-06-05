"""Core Security Module"""
from datetime import datetime, timedelta, timezone
from jose import jwt

from app.config import settings


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """Create JWT access token

    Args:
        data: Token payload data
        expires_delta: Token expiration time delta

    Returns:
        Encoded JWT token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def decode_token(token: str) -> dict:
    """Decode JWT token

    Args:
        token: JWT token to decode

    Returns:
        Decoded token payload
    """
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
