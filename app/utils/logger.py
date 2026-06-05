"""Logger Utility"""
import logging
from app.utils.logging_config import setup_logging

# Initialize logging
setup_logging()


def get_logger(name: str) -> logging.Logger:
    """Get logger instance

    Args:
        name: Logger name (typically __name__)

    Returns:
        Configured logger instance
    """
    return logging.getLogger(name)


def get_app_logger() -> logging.Logger:
    """Get application logger"""
    return logging.getLogger("app")


def get_database_logger() -> logging.Logger:
    """Get database logger"""
    return logging.getLogger("app.database")


def get_api_logger() -> logging.Logger:
    """Get API logger"""
    return logging.getLogger("app.api")
