"""Logging Configuration"""
import logging
import logging.config
from pathlib import Path
from app.config import settings

# Create logs directory if it doesn't exist
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

# Define log file paths
DEBUG_LOG = LOGS_DIR / "debug.log"
INFO_LOG = LOGS_DIR / "info.log"
ERROR_LOG = LOGS_DIR / "error.log"
APP_LOG = LOGS_DIR / "app.log"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "json": {
            "()": "app.utils.logging_formatter.JsonFormatter",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "logging.Filter",
            "name": "require_debug_true",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "console_error": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "verbose",
            "stream": "ext://sys.stderr",
        },
        "file_debug": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "verbose",
            "filename": str(DEBUG_LOG),
            "maxBytes": 10485760,  # 10MB
            "backupCount": 10,
        },
        "file_info": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": str(INFO_LOG),
            "maxBytes": 10485760,  # 10MB
            "backupCount": 5,
        },
        "file_error": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "verbose",
            "filename": str(ERROR_LOG),
            "maxBytes": 10485760,  # 10MB
            "backupCount": 10,
        },
        "file_app": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "verbose",
            "filename": str(APP_LOG),
            "maxBytes": 10485760,  # 10MB
            "backupCount": 10,
        },
    },
    "loggers": {
        "app": {
            "level": settings.LOG_LEVEL,
            "handlers": ["console", "file_app", "console_error"],
            "propagate": False,
        },
        "app.database": {
            "level": settings.LOG_LEVEL,
            "handlers": ["file_info"],
            "propagate": False,
        },
        "app.api": {
            "level": settings.LOG_LEVEL,
            "handlers": ["console", "file_app"],
            "propagate": False,
        },
        "app.services": {
            "level": settings.LOG_LEVEL,
            "handlers": ["console", "file_app"],
            "propagate": False,
        },
        "uvicorn": {
            "level": "INFO",
            "handlers": ["console", "file_info"],
            "propagate": False,
        },
        "uvicorn.access": {
            "level": "INFO",
            "handlers": ["file_info"],
            "propagate": False,
        },
        "uvicorn.error": {
            "level": "ERROR",
            "handlers": ["console_error", "file_error"],
            "propagate": False,
        },
    },
    "root": {
        "level": settings.LOG_LEVEL,
        "handlers": ["console"],
    },
}


def setup_logging():
    """Setup logging configuration"""
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    logger.info(f"Logging configured with level: {settings.LOG_LEVEL}")
    logger.debug(f"Debug log: {DEBUG_LOG}")
    logger.debug(f"Info log: {INFO_LOG}")
    logger.debug(f"Error log: {ERROR_LOG}")
    logger.debug(f"App log: {APP_LOG}")
