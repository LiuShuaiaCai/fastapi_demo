"""Error Handler Middleware"""
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.utils.logger import get_logger
import traceback

logger = get_logger(__name__)


def setup_error_handlers(app: FastAPI):
    """Setup error handlers"""

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """Handle validation errors"""
        logger.warning(
            f"Validation error on {request.method} {request.url.path}: {exc.errors()}"
        )
        logger.debug(f"Request body: {await request.body()}")
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "detail": exc.errors(),
                "message": "Validation error",
            },
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """Handle general exceptions"""
        logger.error(
            f"Unhandled exception on {request.method} {request.url.path}: {str(exc)}",
            exc_info=True,
            extra={"traceback": traceback.format_exc()},
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "Internal server error",
                "detail": str(exc) if str(exc) else "An error occurred",
            },
        )
