"""Validators Module"""
import re
from datetime import datetime


def validate_email(email: str) -> bool:
    """Validate email format

    Args:
        email: Email address to validate

    Returns:
        True if valid, False otherwise
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def validate_username(username: str) -> bool:
    """Validate username format

    Args:
        username: Username to validate

    Returns:
        True if valid, False otherwise
    """
    if len(username) < 3 or len(username) > 50:
        return False
    pattern = r"^[a-zA-Z0-9_-]+$"
    return re.match(pattern, username) is not None


def validate_password(password: str) -> bool:
    """Validate password strength

    Args:
        password: Password to validate

    Returns:
        True if valid, False otherwise
    """
    if len(password) < 8:
        return False
    return True
