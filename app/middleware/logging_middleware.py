"""Logging Middleware"""
import time
import logging
from typing import Callable
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware for logging HTTP requests and responses"""

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """Log incoming request and outgoing response"""
        # Start time
        start_time = time.time()

        # Log incoming request
        logger.info(
            f"Incoming Request - {request.method} {request.url.path} - Client: {request.client.host if request.client else 'Unknown'}"
        )
        logger.debug(f"Query params: {dict(request.query_params)}")
        logger.debug(f"Headers: {dict(request.headers)}")

        try:
            # Process request
            response = await call_next(request)
        except Exception as exc:
            # Log error
            logger.error(
                f"Request Error - {request.method} {request.url.path}",
                exc_info=True,
            )
            raise

        # Calculate duration
        duration = time.time() - start_time

        # Log response
        logger.info(
            f"Response - {request.method} {request.url.path} - Status: {response.status_code} - Duration: {duration:.3f}s"
        )

        # Add custom headers
        response.headers["X-Process-Time"] = str(duration)

        return response
