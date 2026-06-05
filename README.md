# FastAPI Demo

A clean, production-ready FastAPI template with authentication, user management, complete logging system, and testing setup.

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
- ✅ Extensible architecture - easy to add new modules

## Project Structure

```
fastapi-demo/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── config.py               # Configuration management
│   ├── dependencies.py         # Dependency injection
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── endpoints/
│   │       │   ├── __init__.py
│   │       │   ├── auth.py     # Authentication endpoints
│   │       │   └── users.py    # User endpoints
│   │       └── router.py       # v1 route aggregation
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py             # SQLAlchemy base model
│   │   └── user.py             # User data model
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py             # Pydantic user schemas
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py     # User business logic
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── base.py             # Database base configuration
│   │   ├── session.py          # Database session
│   │   └── init_db.py          # Database initialization
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── error_handler.py    # Error handling middleware
│   │   └── logging_middleware.py # HTTP request/response logging
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py           # Logger utilities
│   │   ├── logging_config.py   # Logging configuration
│   │   ├── logging_formatter.py # JSON formatter
│   │   ├── security.py         # Security utilities (JWT)
│   │   ├── validators.py       # Validation utilities
│   │   └── helpers.py          # Helper functions
│   │
│   └── core/
│       ├── __init__.py
│       ├── security.py         # Core security functions
│       └── constants.py        # Constants definition
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest configuration
│   ├── test_auth.py            # Authentication tests
│   └── test_users.py           # User endpoint tests
│
├── logs/                       # Log files directory (auto-created)
│   ├── debug.log               # Debug level logs
│   ├── info.log                # Info level logs
│   ├── error.log               # Error level logs
│   └── app.log                 # Application logs
│
├── migrations/                 # Alembic database migrations
│   ├── env.py
│   └── versions/
│       └── __init__.py
│
├── pyproject.toml              # UV & project configuration
├── .python-version             # Python version
├── .env                        # Environment variables (do not commit)
├── .env.example                # Environment variables example
├── .gitignore
├── .dockerignore
├── alembic.ini                 # Alembic configuration
├── Dockerfile                  # Docker container config
├── docker-compose.yml          # Docker Compose config
├── pytest.ini                  # Pytest configuration
└── README.md                   # Project documentation
```

## Logging System

### Log Files

The application automatically creates and manages log files in the `logs/` directory:

- **debug.log** - All debug level and above logs (verbose format)
- **info.log** - Info level and above logs (simple format)
- **error.log** - Error level logs only (verbose format)
- **app.log** - Application-specific logs (verbose format)

### Features

- 📝 **Multiple Log Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- 🔄 **Rotating File Handlers**: Automatically rotates logs when reaching 10MB
- 📊 **Structured Logging**: JSON format support
- 🏗️ **Logger Hierarchy**: Separate loggers for app, database, API, and services
- 🌐 **HTTP Logging**: Middleware logs all requests and responses
- ⚡ **Performance Tracking**: Response time tracking with `X-Process-Time` header
- 🔍 **Error Tracking**: Full exception stack traces

### Using the Logger

```python
from app.utils.logger import get_logger

logger = get_logger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message", exc_info=True)
```

## Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager

## Installation

### 1. Install uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone the repository

```bash
git clone https://github.com/LiuShuaiaCai/fastapi_demo.git
cd fastapi_demo
```

### 3. Install dependencies

```bash
# Install production dependencies
uv sync

# Install with development dependencies
uv sync --all-extras
```

### 4. Setup environment

```bash
cp .env.example .env
```

Edit `.env` with your settings.

## Running the Application

### Development

```bash
uv run uvicorn app.main:app --reload
```

Access the API:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Docker

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

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=app

# Run specific test file
uv run pytest tests/test_auth.py -v
```

## Viewing Logs

```bash
# Real-time log viewing
tail -f logs/app.log

# View error logs
tail -f logs/error.log

# Search for specific errors
grep "ERROR" logs/error.log
```

## Database

### Default: SQLite

```env
DATABASE_URL=sqlite:///./test.db
```

### PostgreSQL

1. Update `.env`:
   ```env
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

2. Install driver:
   ```bash
   uv add psycopg2-binary
   ```

### Database Initialization

```python
from app.database.session import SessionLocal
from app.database.init_db import init_db

db = SessionLocal()
init_db(db)
```

### Migrations (Alembic)

```bash
# Generate migration
uv run alembic revision --autogenerate -m "Add user table"

# Apply migrations
uv run alembic upgrade head
```

## Code Quality

```bash
# Format code
uv run black app/ tests/

# Lint code
uv run ruff check app/ tests/

# Type checking
uv run mypy app/
```

## Example API Usage

### Register

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

### Get Current User

```bash
curl -X GET "http://localhost:8000/api/v1/users/me" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Configuration

```env
# Database
DATABASE_URL=sqlite:///./test.db

# Security
SECRET_KEY=your-secret-key-change-this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application
DEBUG=True
APP_NAME=FastAPI Demo
APP_VERSION=1.0.0
API_PREFIX=/api/v1

# CORS
CORS_ORIGINS=["http://localhost", "http://localhost:3000"]

# Logging
LOG_LEVEL=INFO
```

## Adding New Endpoints

### 1. Create Model

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

### 2. Create Schema

```python
# app/schemas/product.py
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)

class ProductResponse(ProductCreate):
    id: int
    class Config:
        from_attributes = True
```

### 3. Create Service

```python
# app/services/product_service.py
from sqlalchemy.orm import Session
from app.models.product import Product

class ProductService:
    @staticmethod
    def create_product(db: Session, product_data):
        product = Product(**product_data.dict())
        db.add(product)
        db.commit()
        db.refresh(product)
        return product
```

### 4. Create Endpoints

```python
# app/api/v1/endpoints/products.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import ProductService

router = APIRouter()

@router.post("/", response_model=ProductResponse)
async def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    return ProductService.create_product(db, data)
```

### 5. Register in Router

```python
# app/api/v1/router.py
from app.api.v1.endpoints import products

router.include_router(products.router, prefix="/products", tags=["products"])
```

## Security

- ✅ Change `SECRET_KEY` in production
- ✅ Use environment variables for sensitive data
- ✅ Validate and sanitize all input
- ✅ Use HTTPS in production
- ✅ Implement rate limiting
- ✅ Keep dependencies updated: `uv sync --upgrade`
- ✅ Review logs regularly

## Utilities

### Validators

```python
from app.utils.validators import validate_email, validate_username, validate_password
```

### Helpers

```python
from app.utils.helpers import flatten_dict, paginate
```

## uv Commands

```bash
uv sync                    # Install dependencies
uv sync --all-extras       # Install with dev dependencies
uv add package-name        # Add dependency
uv add --dev package-name  # Add dev dependency
uv remove package-name     # Remove dependency
uv sync --upgrade          # Update all dependencies
uv run command            # Run command in venv
uv venv                   # Create virtual environment
```

## License

MIT

## Support

For issues, please create an issue in the repository.
