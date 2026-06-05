# FastAPI Demo

A complete, production-ready FastAPI template with authentication, database integration, logging system, and testing setup.

## Features

- ✅ FastAPI framework with async support
- ✅ SQLAlchemy ORM integration
- ✅ JWT Authentication (login/register)
- ✅ User management endpoints
- ✅ **Complete Logging System** with file rotation
- ✅ Error handling and middleware
- ✅ CORS middleware configuration
- ✅ Docker & Docker Compose support
- ✅ Unit testing with Pytest
- ✅ Environment configuration management
- ✅ Request/Response validation with Pydantic
- ✅ **uv package manager** for fast dependency management

## Project Structure

```
fastapi_demo/
├── app/
│   ├── api/v1/
│   │   ├── endpoints/     # API endpoints
│   │   └── router.py      # Route aggregation
│   ├── models/            # SQLAlchemy models
│   ├── schemas/           # Pydantic schemas
│   ├── services/          # Business logic
│   ├── database/          # Database configuration
│   ├── middleware/
│   │   ├── error_handler.py       # Error handling
│   │   └── logging_middleware.py  # HTTP logging
│   ├── utils/
│   │   ├── logger.py              # Logger initialization
│   │   ├── logging_config.py      # Logging configuration
│   │   ├── logging_formatter.py   # JSON formatter
│   │   └── security.py
│   ├── config.py          # Configuration
│   ├── dependencies.py    # FastAPI dependencies
│   └── main.py            # Application entry
├── logs/                  # Log files (auto-created)
│   ├── debug.log          # Debug level logs
│   ├── info.log           # Info level logs
│   ├── error.log          # Error level logs
│   └── app.log            # Application logs
├── tests/                 # Unit tests
├── pyproject.toml         # UV & project configuration
├── .python-version        # Python version
├── .env.example           # Environment variables example
└── README.md
```

## Logging System

### Log Files

The application automatically creates and manages the following log files in the `logs/` directory:

- **debug.log** - All debug level and above logs (verbose format)
- **info.log** - Info level and above logs (simple format)
- **error.log** - Error level logs only (verbose format)
- **app.log** - Application-specific logs (verbose format)

### Log Configuration

All logging is configured in `app/utils/logging_config.py`:

```python
LOGGING_CONFIG = {
    "formatters": {
        "verbose": "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
        "simple": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "json": "Structured JSON logging",
    },
    "handlers": {
        "console": "Console output (stdout)",
        "file_debug": "Rotating file handler for debug logs",
        "file_info": "Rotating file handler for info logs",
        "file_error": "Rotating file handler for error logs",
    },
}
```

### Features

- 📝 **Multiple Log Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- 🔄 **Rotating File Handlers**: Automatically rotates logs when they reach 10MB
- 📊 **Structured Logging**: JSON format support for structured logs
- 🎯 **Logger Hierarchy**: Separate loggers for app, database, API, and services
- 🌐 **HTTP Logging**: Middleware logs all HTTP requests and responses
- ⚡ **Performance Tracking**: Response time tracking with `X-Process-Time` header
- 🔍 **Error Tracking**: Full exception stack traces logged

### Using the Logger

```python
from app.utils.logger import get_logger, get_app_logger, get_database_logger

# Get a logger for the current module
logger = get_logger(__name__)

# Get specific loggers
app_logger = get_app_logger()
db_logger = get_database_logger()

# Log at different levels
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message", exc_info=True)
logger.critical("Critical message")
```

### Log Format Examples

**Verbose Format**:
```
2024-01-15 10:30:45,123 - app.services.user_service - ERROR - [user_service.py:45] - Failed to create user
```

**Simple Format**:
```
2024-01-15 10:30:45,123 - app.api.v1.endpoints.users - INFO - User registration successful
```

### Environment Configuration

Control logging level via `.env`:

```env
# LOG_LEVEL can be: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL=INFO
```

## Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager

## Installation with uv

### 1. Install uv (if not already installed)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (using PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone the repository

```bash
git clone https://github.com/LiuShuaiaCai/fastapi_demo.git
cd fastapi_demo
```

### 3. Install dependencies with uv

```bash
# Install production dependencies
uv sync

# Install with dev dependencies
uv sync --all-extras
```

### 4. Setup environment variables

```bash
cp .env.example .env
```

Edit `.env` file with your settings.

## Running the Application

### Using uv

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`
API Documentation: `http://localhost:8000/docs`

### Using Docker

```bash
docker-compose up
```

## API Endpoints

### Authentication

- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login and get access token

### Users

- `GET /api/v1/users/` - Get all users
- `GET /api/v1/users/{user_id}` - Get user by ID
- `GET /api/v1/users/me` - Get current user (requires authentication)

### Health

- `GET /health` - Health check
- `GET /` - Welcome message

## Testing

Run tests with uv:

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=app

# Run specific test file
uv run pytest tests/test_auth.py -v

# Run with detailed output
uv run pytest tests/ -vv --tb=long
```

## Viewing Logs

```bash
# View latest logs in real-time
tail -f logs/app.log

# View error logs
tail -f logs/error.log

# View all debug logs
cat logs/debug.log

# Search for specific errors
grep "ERROR" logs/error.log
```

## Database

The template uses SQLite by default. To use PostgreSQL:

1. Update `DATABASE_URL` in `.env`:
   ```
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

2. Install PostgreSQL driver:
   ```bash
   uv add psycopg2-binary
   ```

## Code Quality Tools

### Format Code with Black

```bash
uv run black app/ tests/
```

### Lint Code with Ruff

```bash
uv run ruff check app/ tests/
```

### Type Checking with MyPy

```bash
uv run mypy app/
```

## Example API Usage

### Register User

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "email": "john@example.com", "password": "password123"}'
```

### Login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "password123"}'
```

### Get Current User (with token)

```bash
curl -X GET "http://localhost:8000/api/v1/users/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Configuration

All configuration is managed in `.env` file:

```env
# Database
DATABASE_URL=sqlite:///./test.db

# Security
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application
DEBUG=True
APP_NAME=FastAPI Demo
APP_VERSION=1.0.0
API_PREFIX=/api/v1

# CORS
CORS_ORIGINS=["http://localhost","http://localhost:3000"]

# Logging
LOG_LEVEL=INFO
```

## Development

### Add New Endpoint

1. Create schema in `app/schemas/`
2. Create model in `app/models/` if needed
3. Create service in `app/services/`
4. Create endpoint in `app/api/v1/endpoints/`
5. Add router to `app/api/v1/router.py`
6. Add tests in `tests/`

### Add New Model

```python
# app/models/product.py
from sqlalchemy import Column, Integer, String, Float
from app.models.base import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
```

## Security

- Change `SECRET_KEY` in production
- Use environment variables for sensitive data
- Always validate and sanitize input
- Use HTTPS in production
- Implement rate limiting
- Keep dependencies updated with `uv sync --upgrade`
- Review logs regularly for security issues

## uv Commands Quick Reference

```bash
# Install dependencies
uv sync

# Install with dev dependencies
uv sync --all-extras

# Add a new dependency
uv add package-name

# Add a dev dependency
uv add --dev package-name

# Remove a dependency
uv remove package-name

# Update all dependencies
uv sync --upgrade

# Run a command in the virtual environment
uv run command

# Create a virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

## Benefits of uv

| Feature | Benefit |
|---------|----------|
| Speed | **10-100x faster** than pip |
| Deterministic | Auto-generates lock file for reproducible builds |
| All-in-one | Package management + venv + script running |
| Zero dependencies | Single compiled binary |
| Compatible | Supports PEP 517/518 standards |

## License

MIT

## Support

For issues and questions, please create an issue in the repository.
