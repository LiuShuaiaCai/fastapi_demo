# FastAPI Demo

A complete, production-ready FastAPI template with authentication, database integration, logging system, and testing setup.

## Features

- ✅ FastAPI framework with async support
- ✅ SQLAlchemy ORM integration
- ✅ JWT Authentication (login/register)
- ✅ User, Product, and Order management
- ✅ **Complete Logging System** with file rotation
- ✅ Error handling and middleware
- ✅ CORS middleware configuration
- ✅ Docker & Docker Compose support
- ✅ Unit testing with Pytest
- ✅ Environment configuration management
- ✅ Request/Response validation with Pydantic
- ✅ **uv package manager** for fast dependency management
- ✅ Multi-version API support (v1, v2)
- ✅ Database migration ready (Alembic)

## Project Structure

```
fastapi-demo/
├── app/
│   ├── __init__.py
│   ├── main.py                 # 应用入口
│   ├── config.py               # 配置管理
│   ├── dependencies.py         # 依赖注入
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py       # 认证端点
│   │   │   │   ├── users.py      # 用户端点
│   │   │   │   ├── products.py   # 产品端点
│   │   │   │   └── orders.py     # 订单端点
│   │   │   └── router.py         # v1 路由汇总
│   │   └── v2/
│   │       ├── __init__.py
│   │       ├── endpoints/
│   │       │   ├── __init__.py
│   │       │   └── users.py      # 用户端点 (v2)
│   │       └── router.py         # v2 路由汇总
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py              # 基础模型
│   │   ├── user.py              # 用户数据模型
│   │   ├── product.py           # 产品数据模型
│   │   └── order.py             # 订单数据模型
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py              # Pydantic 用户模型
│   │   ├── product.py           # Pydantic 产品模型
│   │   └── order.py             # Pydantic 订单模型
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py      # 用户业务逻辑
│   │   ├── product_service.py   # 产品业务逻辑
│   │   └── order_service.py     # 订单业务逻辑
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── base.py              # 数据库基础配置
│   │   ├── session.py           # 数据库会话
│   │   └── init_db.py           # 初始化数据库
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── error_handler.py     # 错误处理中间件
│   │   └── logging_middleware.py # HTTP 日志中间件
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py            # 日志工具
│   │   ├── logging_config.py    # 日志配置
│   │   ├── logging_formatter.py # JSON 日志格式化
│   │   ├── security.py          # 安全工具
│   │   ├── validators.py        # 验证工具
│   │   └── helpers.py           # 辅助函数
│   │
│   └── core/
│       ├── __init__.py
│       ├── security.py          # 认证授权
│       └── constants.py         # 常量定义
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest 配置
│   ├── test_auth.py             # 认证测试
│   ├── test_users.py            # 用户测试
│   ├── test_products.py         # 产品测试
│   └── test_orders.py           # 订单测试
│
├── migrations/                  # Alembic 数据库迁移
│   ├── env.py
│   └── versions/
│       └── __init__.py
│
├── logs/                        # 日志文件目录 (自动创建)
│   ├── debug.log                # 调试日志
│   ├── info.log                 # 信息日志
│   ├── error.log                # 错误日志
│   └── app.log                  # 应用日志
│
├── pyproject.toml               # UV & 项目配置
├── .python-version              # Python 版本
├── .env                         # 环境变量配置 (勿提交)
├── .env.example                 # 环境变量示例
├── .gitignore
├── .dockerignore
├── alembic.ini                  # Alembic 配置
├── Dockerfile                   # Docker 容器配置
├── docker-compose.yml           # Docker Compose 配置
├── pytest.ini                   # Pytest 配置
└── README.md                    # 项目说明
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
- 🏛️ **Logger Hierarchy**: Separate loggers for app, database, API, and services
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

### API v1 Endpoints

#### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login and get access token

#### Users
- `GET /api/v1/users/` - Get all users
- `GET /api/v1/users/{user_id}` - Get user by ID
- `GET /api/v1/users/me` - Get current user (requires authentication)

#### Products
- `POST /api/v1/products/` - Create new product
- `GET /api/v1/products/` - Get all products
- `GET /api/v1/products/{product_id}` - Get product by ID
- `PUT /api/v1/products/{product_id}` - Update product
- `DELETE /api/v1/products/{product_id}` - Delete product

#### Orders
- `POST /api/v1/orders/` - Create new order
- `GET /api/v1/orders/` - Get all orders
- `GET /api/v1/orders/{order_id}` - Get order by ID
- `PUT /api/v1/orders/{order_id}` - Update order
- `DELETE /api/v1/orders/{order_id}` - Delete order

#### Health
- `GET /health` - Health check
- `GET /` - Welcome message

### API v2 Endpoints

#### Users (Enhanced)
- `GET /api/v2/users/` - Get all users (v2)
- `GET /api/v2/users/{user_id}` - Get user by ID (v2)
- `GET /api/v2/users/me` - Get current user (v2)

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

### Database Initialization

The application automatically creates tables on startup. To initialize with sample data:

```python
from app.database.session import SessionLocal
from app.database.init_db import init_db

db = SessionLocal()
init_db(db)
```

### Database Migrations (Alembic)

```bash
# Generate a new migration
uv run alembic revision --autogenerate -m "Add user table"

# Apply migrations
uv run alembic upgrade head

# View migration history
uv run alembic history
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

### Create Product

```bash
curl -X POST "http://localhost:8000/api/v1/products/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "description": "High performance", "price": 999.99, "stock": 10}'
```

### Create Order

```bash
curl -X POST "http://localhost:8000/api/v1/orders/" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "product_id": 1, "quantity": 2, "total_price": 1999.98}'
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

1. Create schema in `app/schemas/` (if needed)
2. Create model in `app/models/` (if needed)
3. Create service in `app/services/`
4. Create endpoint in `app/api/v1/endpoints/`
5. Add router to `app/api/v1/router.py`
6. Add tests in `tests/`

### Example: Add New Model

```python
# app/models/category.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.models.base import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
```

### Example: Add New Schema

```python
# app/schemas/category.py
from pydantic import BaseModel, Field
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = None

class CategoryResponse(CategoryCreate):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
```

### Example: Add New Service

```python
# app/services/category_service.py
from sqlalchemy.orm import Session
from app.models.category import Category

class CategoryService:
    @staticmethod
    def create_category(db: Session, category_data):
        category = Category(**category_data.dict())
        db.add(category)
        db.commit()
        db.refresh(category)
        return category
```

### Example: Add New Endpoint

```python
# app/api/v1/endpoints/categories.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.category import CategoryCreate, CategoryResponse
from app.services.category_service import CategoryService

router = APIRouter()

@router.post("/", response_model=CategoryResponse)
async def create_category(data: CategoryCreate, db: Session = Depends(get_db)):
    return CategoryService.create_category(db, data)
```

Then add to `app/api/v1/router.py`:

```python
from app.api.v1.endpoints import categories

router.include_router(categories.router, prefix="/categories", tags=["categories"])
```

## Security

- Change `SECRET_KEY` in production
- Use environment variables for sensitive data
- Always validate and sanitize input
- Use HTTPS in production
- Implement rate limiting
- Keep dependencies updated with `uv sync --upgrade`
- Review logs regularly for security issues
- Use strong passwords (minimum 8 characters)

## Utilities

### Validators

```python
from app.utils.validators import validate_email, validate_username, validate_password

validate_email("user@example.com")  # True
validate_username("john_doe")       # True
validate_password("secure123")      # True
```

### Helpers

```python
from app.utils.helpers import flatten_dict, paginate

# Flatten nested dictionary
result = flatten_dict({"user": {"name": "John", "age": 30}})
# {"user.name": "John", "user.age": 30}

# Paginate items
data = paginate(items, skip=0, limit=10)
# {"data": [...], "total": 100, "page": 1, "pages": 10}
```

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
.venv\\Scripts\\activate     # Windows
```

## Benefits of uv

| Feature | Benefit |
|---------|----------|
| Speed | **10-100x faster** than pip |
| Deterministic | Auto-generates lock file for reproducible builds |
| All-in-one | Package management + venv + script running |
| Zero dependencies | Single compiled binary |
| Compatible | Supports PEP 517/518 standards |

## Project Statistics

- **Models**: 3 (User, Product, Order)
- **Endpoints**: 15+ across v1 and v2
- **Services**: 4 (User, Product, Order, Health)
- **Tests**: 8+ test files
- **Log Files**: 4 rotating log files
- **Utilities**: 4 utility modules
- **Middleware**: 2 custom middleware

## License

MIT

## Support

For issues and questions, please create an issue in the repository.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
