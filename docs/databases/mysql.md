# MySQL 使用指南

本文档介绍如何在本项目中使用 MySQL 作为主事务型数据库的配置、建议的驱动、SQLAlchemy 配置、Alembic 迁移配置，以及 Docker 与常见问题的解决办法。

目录
- 前提
- 安装驱动
- Docker Compose 示例
- .env 配置
- SQLAlchemy（同步与异步）示例
- Alembic 配置与迁移
- 连接池和性能调优建议
- 常见问题与调试

---

前提
- 已安装 uv 包管理器（或可用 pip）
- MySQL 服务可用（本地或远程）

安装驱动

推荐两种方式：同步驱动（pymysql / mysqlclient）或异步驱动（asyncmy + SQLAlchemy 2.0 async）。

- 使用 pymysql（同步，简单）

```bash
uv add pymysql
# 或者 pip install pymysql
```

- 使用 mysqlclient（C 绑定，性能更好，但需系统依赖）

```bash
uv add mysqlclient
# 需要在系统安装 libmysqlclient-dev 等
```

- 使用 asyncmy（异步，配合 SQLAlchemy 2.0）

```bash
uv add asyncmy
# 也可安装 aiomysql，选择与 SQLAlchemy 兼容的驱动
```

Docker Compose 示例

在项目的 docker-compose.yml 中加入 MySQL 服务示例：

```yaml
services:
  mysql:
    image: mysql:8.0
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: fastapi_demo
      MYSQL_USER: demo
      MYSQL_PASSWORD: demopass
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

.env 配置示例

请在项目根目录的 `.env` 中加入：

```env
# MySQL 配置
DATABASE_URL=mysql+pymysql://demo:demopass@localhost:3306/fastapi_demo
# 如果使用异步 asyncmy
# DATABASE_URL=mysql+asyncmy://demo:demopass@localhost:3306/fastapi_demo
```

SQLAlchemy 配置示例

- 同步模式（常见，简单）：

```python
# app/database/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 依赖注入
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

- 异步模式（SQLAlchemy 2.0 async + asyncmy）：

```python
# app/database/async_session.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings

# DATABASE_URL 示例: mysql+asyncmy://user:pass@host:3306/dbname
async_engine = create_async_engine(settings.DATABASE_URL, pool_pre_ping=True)
AsyncSessionLocal = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)

async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session
```

注意：在异步模式下，SQLAlchemy 的模型定义（Base）可以保持相同，但 CRUD 操作需要使用 async/await 和 AsyncSession。

Alembic 配置与迁移

- alembic.ini 中 sqlalchemy.url 可以保留为空，通过 migrations/env.py 从项目配置读取（示例项目已经实现）。
- 生成迁移：

```bash
# 自动检测模型变更并生成迁移
uv run alembic revision --autogenerate -m "Add new table"
```

- 应用迁移：

```bash
uv run alembic upgrade head
```

注意事项
- 如果使用异步数据库 URL（mysql+asyncmy://...），alembic 在某些环境下仍然需要使用同步 URL 来运行 autogenerate。推荐在 env.py 中，将 settings.DATABASE_URL 提供为同步驱动格式（例如 mysql+pymysql），或在 autogenerate 前创建一个临时同步 engine 用于检查元数据。
- 若使用 mysqlclient 或 pymysql，autogenerate 一般工作正常。

连接池与性能调优建议

- 使用 pool_pre_ping=True 防止连接断开错误
- 通过 create_engine 的参数配置 pool_size、max_overflow，根据应用负载调整
- 对于高并发写入场景，考虑批量插入降低事务数量
- 开启慢查询日志并分析 SQL 性能

常见问题与调试

- 连接失败：检查 host、port、用户、密码、依赖包是否安装
- 权限问题：确认 MySQL 用户具有所需数据库和表权限
- 字符集问题：确保数据库使用 utf8mb4，并在 SQLAlchemy URL 或 create_engine 中设置 charset 参数（针对 pymysql: ?charset=utf8mb4）

示例: 在 URL 中添加 charset

```
DATABASE_URL=mysql+pymysql://demo:demopass@localhost:3306/fastapi_demo?charset=utf8mb4
```

总结

MySQL 适合用作主事务数据库，配合 Alembic 管理迁移，推荐在生产中使用 mysqlclient 或 pymysql（同步）或 asyncmy（异步）。确保在 .env 中正确配置 DATABASE_URL，并在 migrations/env.py 中使用该 URL 进行迁移管理。
