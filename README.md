# FastAPI Demo

A complete, production-ready FastAPI template with authentication, database integration, and testing setup.

## Features

- ✅ FastAPI framework with async support
- ✅ SQLAlchemy ORM integration
- ✅ JWT Authentication (login/register)
- ✅ User management endpoints
- ✅ Error handling and logging
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
│   ├── middleware/        # Middleware setup
│   ├── utils/             # Utilities
│   ├── config.py          # Configuration
│   ├── dependencies.py    # FastAPI dependencies
│   └── main.py            # Application entry
├── tests/                 # Unit tests
├── pyproject.toml         # UV & project configuration
├── .python-version        # Python version
├── .env.example           # Environment variables example
└── README.md
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

# Or using pip
pip install uv
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
# Run with uvicorn
uv run uvicorn app.main:app --reload

# Or directly with the app module
uv run python -m uvicorn app.main:app --reload
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
uv run pytest tests/test_auth.py

# Run tests in watch mode
uv run pytest --tb=short -v
```

## Database

The template uses SQLite by default. To use PostgreSQL:

1. Update `DATABASE_URL` in `.env`:
   ```
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

2. Install PostgreSQL driver:
   ```bash
   uv pip install psycopg2-binary
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
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your-secret-key
DEBUG=True
APP_NAME=FastAPI Demo
CORS_ORIGINS=["http://localhost", "http://localhost:3000"]
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
- Keep dependencies updated with `uv sync`

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

- ⚡ **10-100x faster** than pip for dependency resolution
- 🔒 **Deterministic** lock file for reproducible builds
- 📦 **Single tool** for dependency management and virtual environments
- 🚀 **Zero runtime dependencies** - single compiled binary
- 🔄 **Built-in` lock file** (uv.lock) for version pinning

## License

MIT

## Support

For issues and questions, please create an issue in the repository.
