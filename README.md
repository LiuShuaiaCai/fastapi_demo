# FastAPI 演示项目

一个完整的、可用于生产环境的 FastAPI 模板，包含认证、用户管理、完整的日志系统和测试框架。

## ✨ 主要特性

- ✅ FastAPI 框架 + 异步支持
- ✅ SQLAlchemy ORM 数据库集成
- ✅ JWT 身份验证（注册/登录）
- ✅ 用户管理端点
- ✅ **完整的日志系统**（文件自动轮转）
- ✅ 错误处理和中间件
- ✅ CORS 中间件配置
- ✅ Docker & Docker Compose 支持
- ✅ Pytest 单元测试框架
- ✅ 环境配置管理
- ✅ Pydantic 请求/响应验证
- ✅ **uv 包管理器**（超快依赖管理）
- ✅ 可扩展架构（易于添加新模块）
- ✅ Alembic 数据库迁移

## 📁 项目结构

```
fastapi-demo/
├── app/
│   ├── __init__.py
│   ├── main.py                 # 应用入口
│   ├── config.py               # 配置管理
│   ├── dependencies.py         # 依赖注入
│   │
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── endpoints/
│   │       │   ├── __init__.py
│   │       │   ├── auth.py     # 认证端点
│   │       │   └── users.py    # 用户端点
│   │       └── router.py       # v1 路由汇总
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py             # SQLAlchemy 基础模型
│   │   └── user.py             # 用户数据模型
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py             # Pydantic 用户模型
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py     # 用户业务逻辑
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── base.py             # 数据库基础配置
│   │   ├── session.py          # 数据库会话
│   │   └── init_db.py          # 数据库初始化
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── error_handler.py    # 错误处理中间件
│   │   └── logging_middleware.py # HTTP 请求/响应日志
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py           # 日志工具
│   │   ├── logging_config.py   # 日志配置
│   │   ├── logging_formatter.py # JSON 格式化器
│   │   ├── security.py         # 安全工具（JWT）
│   │   ├── validators.py       # 验证工具
│   │   └── helpers.py          # 辅助函数
│   │
│   └── core/
│       ├── __init__.py
│       ├── security.py         # 核心安全函数
│       └── constants.py        # 常量定义
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest 配置
│   ├── test_auth.py            # 认证测试
│   └── test_users.py           # 用户端点测试
│
├── migrations/                 # Alembic 数据库迁移
│   ├── env.py                  # Alembic 环境配置
│   └── versions/
│       └── 001_initial_create_users_table.py
│
├── logs/                       # 日志文件目录（自动创建）
│   ├── debug.log
│   ├── info.log
│   ├── error.log
│   └── app.log
│
├── pyproject.toml              # uv 和项目配置
├── .python-version             # Python 版本
├── .env                        # 环境变量（勿提交）
├── .env.example                # 环境变量示例
├── .gitignore
├── .dockerignore
├── alembic.ini                 # Alembic 配置
├── Dockerfile                  # Docker 容器配置
├── docker-compose.yml          # Docker Compose 配置
├── pytest.ini                  # Pytest 配置
├── MIGRATIONS_GUIDE.md         # 数据库迁移指南
└── README.md                   # 项目文档
```

## 📝 日志系统

### 日志文件

应用会自动在 `logs/` 目录下创建和管理以下日志文件：

- **debug.log** - 调试级别及以上的所有日志（详细格式）
- **info.log** - 信息级别及以上的日志（简洁格式）
- **error.log** - 仅错误级别的日志（详细格式）
- **app.log** - 应用级日志（详细格式）

### 日志特性

- 📝 **多个日志级别**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- 🔄 **自动文件轮转**: 文件达到 10MB 时自动备份
- 📊 **结构化日志**: 支持 JSON 格式
- 🏗️ **日志分层**: 为 app、database、API 和 services 独立配置
- 🌐 **HTTP 请求日志**: 中间件记录所有请求和响应
- ⚡ **性能追踪**: 通过 `X-Process-Time` 头追踪响应时间
- 🔍 **错误追踪**: 完整的异常堆栈跟踪

### 使用日志

```python
from app.utils.logger import get_logger

logger = get_logger(__name__)

logger.debug("调试信息")
logger.info("信息")
logger.warning("警告")
logger.error("错误", exc_info=True)
logger.critical("严重错误")
```

## 🔧 系统需求

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) 包管理器

## 📦 安装

### 1. 安装 uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. 克隆仓库

```bash
git clone https://github.com/LiuShuaiaCai/fastapi_demo.git
cd fastapi_demo
```

### 3. 安装依赖

```bash
# 只安装生产依赖
uv sync

# 安装包括开发依赖
uv sync --all-extras
```

### 4. 配置环境

```bash
cp .env.example .env
```

编辑 `.env` 文件，根据需要修改配置。

## 🚀 运行应用

### 开发模式

```bash
uv run uvicorn app.main:app --reload
```

访问 API：
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **API 文档**: http://localhost:8000/openapi.json

### 使用 Docker

```bash
docker-compose up
```

## 📡 API 端点

### 认证
- `POST /api/v1/auth/register` - 注册新用户
- `POST /api/v1/auth/login` - 登录并获取访问令牌

### 用户
- `GET /api/v1/users/` - 获取所有用户
- `GET /api/v1/users/{user_id}` - 根据 ID 获取用户
- `GET /api/v1/users/me` - 获取当前用户（需要认证）

### 健康检查
- `GET /health` - 健康检查
- `GET /` - 欢迎消息

## 🧪 测试

```bash
# 运行所有测试
uv run pytest

# 运行并显示覆盖率
uv run pytest --cov=app

# 运行特定测试文件
uv run pytest tests/test_auth.py -v

# 详细输出
uv run pytest tests/ -vv --tb=long
```

## 📊 查看日志

```bash
# 实时查看应用日志
tail -f logs/app.log

# 查看错误日志
tail -f logs/error.log

# 搜索特定错误
grep "ERROR" logs/error.log

# 查看最后 100 行日志
tail -100 logs/app.log
```

## 💾 数据库

### 默认配置：SQLite

```env
DATABASE_URL=sqlite:///./test.db
```

### 使用 PostgreSQL

1. 更新 `.env`：
   ```env
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

2. 安装驱动：
   ```bash
   uv add psycopg2-binary
   ```

### 数据库初始化

```python
from app.database.session import SessionLocal
from app.database.init_db import init_db

db = SessionLocal()
init_db(db)
```

### 数据库迁移（Alembic）

```bash
# 生成迁移文件
uv run alembic revision --autogenerate -m "描述变更"

# 应用迁移
uv run alembic upgrade head

# 回滚迁移
uv run alembic downgrade -1

# 查看迁移历史
uv run alembic history
```

详细信息请参考 [MIGRATIONS_GUIDE.md](./MIGRATIONS_GUIDE.md)

## 🎨 代码质量

```bash
# 代码格式化
uv run black app/ tests/

# 代码检查
uv run ruff check app/ tests/

# 类型检查
uv run mypy app/
```

## 📝 API 使用示例

### 注册用户

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "email": "john@example.com",
    "password": "password123"
  }'
```

### 登录

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "password": "password123"
  }'
```

响应示例：
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 获取当前用户（需要认证）

```bash
curl -X GET "http://localhost:8000/api/v1/users/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## ⚙️ 配置

所有配置都在 `.env` 文件中管理：

```env
# 数据库
DATABASE_URL=sqlite:///./test.db

# 安全
SECRET_KEY=your-secret-key-change-this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# 应用
DEBUG=True
APP_NAME=FastAPI 演示
APP_VERSION=1.0.0
API_PREFIX=/api/v1

# CORS
CORS_ORIGINS=["http://localhost", "http://localhost:3000"]

# 日志
LOG_LEVEL=INFO
```

## 📚 添加新端点

### 1. 创建数据模型

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

### 2. 创建 Pydantic Schema

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

### 3. 创建业务服务

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

### 4. 创建 API 端点

```python
# app/api/v1/endpoints/products.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import ProductService

router = APIRouter()

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    return ProductService.create_product(db, data)

@router.get("/", response_model=list[ProductResponse])
async def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
```

### 5. 注册到路由

```python
# app/api/v1/router.py
from app.api.v1.endpoints import products

router.include_router(products.router, prefix="/products", tags=["products"])
```

### 6. 编写测试

```python
# tests/test_products.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post(
        "/api/v1/products/",
        json={
            "name": "测试产品",
            "price": 99.99
        }
    )
    assert response.status_code == 201
    assert response.json()["name"] == "测试产品"
```

## 🔒 安全建议

- ✅ 生产环境中修改 `SECRET_KEY`
- ✅ 使用环境变量存储敏感数据
- ✅ 验证和清理所有用户输入
- ✅ 生产环境使用 HTTPS
- ✅ 实施速率限制
- ✅ 定期更新依赖：`uv sync --upgrade`
- ✅ 定期审查日志
- ✅ 使用强密码（至少 8 个字符）

## 🛠️ 工具函数

### 验证器

```python
from app.utils.validators import validate_email, validate_username, validate_password

validate_email("user@example.com")  # True
validate_username("john_doe")       # True
validate_password("secure123")      # True
```

### 辅助函数

```python
from app.utils.helpers import flatten_dict, paginate

# 扁平化嵌套字典
result = flatten_dict({"user": {"name": "John", "age": 30}})
# {"user.name": "John", "user.age": 30}

# 分页
data = paginate(items, skip=0, limit=10)
# {"data": [...], "total": 100, "page": 1, "pages": 10}
```

## 📦 uv 命令速查

```bash
uv sync                    # 安装依赖
uv sync --all-extras       # 安装包括开发依赖
uv add package-name        # 添加依赖
uv add --dev package-name  # 添加开发依赖
uv remove package-name     # 移除依赖
uv sync --upgrade          # 更新所有依赖
uv run command            # 在虚拟环境中运行命令
uv venv                   # 创建虚拟环境
```

## uv 的优势

| 特性 | 优势 |
|------|------|
| 速度 | **比 pip 快 10-100 倍** |
| 确定性 | 自动生成锁文件，版本完全确定 |
| 一体化 | 包管理 + 虚拟环境 + 脚本运行 |
| 零依赖 | 单个编译二进制文件 |
| 兼容性 | 支持 PEP 517/518 标准 |

## 📖 参考资源

- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [SQLAlchemy 文档](https://docs.sqlalchemy.org/)
- [Pydantic 文档](https://docs.pydantic.dev/)
- [Alembic 文档](https://alembic.sqlalchemy.org/)
- [uv 文档](https://docs.astral.sh/uv/)

## 📄 许可证

MIT

## 💬 支持

如有问题或建议，请在仓库中创建 Issue。

## 🤝 贡献

欢迎提交 Pull Request！

---

**仓库地址**: https://github.com/LiuShuaiaCai/fastapi_demo
