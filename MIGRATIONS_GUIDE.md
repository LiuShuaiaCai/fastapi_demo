# 数据库迁移指南

## 什么是 Alembic？

Alembic 是 SQLAlchemy 的数据库迁移工具，用于管理数据库模式变更。

## 安装

```bash
uv add alembic
```

## 初始化 Alembic

```bash
alembic init migrations
```

这会创建 `migrations/` 目录和 `alembic.ini` 配置文件。

## 配置 alembic.ini

编辑 `alembic.ini`，设置数据库 URL：

```ini
# sqlalchemy.url 应该指向您的数据库
# 可以从环境变量读取
sqlalchemy.url = driver://user:password@localhost/dbname
```

## 工作流程

### 1. 修改模型

```python
# app/models/user.py
from sqlalchemy import Column, Integer, String
from app.models.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
```

### 2. 生成迁移文件（自动）

```bash
# 自动检测模型变更并生成迁移文件
uv run alembic revision --autogenerate -m "Add user table"
```

这会在 `migrations/versions/` 下创建一个新的迁移文件，类似：
```
migrations/versions/002_add_user_table.py
```

### 3. 查看生成的迁移文件

```python
# migrations/versions/002_add_user_table.py
from alembic import op
import sqlalchemy as sa

revision = '002'
down_revision = '001'

def upgrade():
    """添加用户表"""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email'),
    )

def downgrade():
    """回滚"""
    op.drop_table('users')
```

### 4. 应用迁移

```bash
# 应用所有未应用的迁移
uv run alembic upgrade head

# 应用到特定版本
uv run alembic upgrade 002

# 回滚一个版本
uv run alembic downgrade -1

# 回滚到特定版本
uv run alembic downgrade 001
```

## 常用命令

```bash
# 查看当前数据库版本
uv run alembic current

# 查看迁移历史
uv run alembic history

# 查看即将执行的迁移
uv run alembic upgrade head --sql

# 生成空的迁移文件（手动编辑）
uv run alembic revision -m "Add new column"

# 自动生成迁移文件
uv run alembic revision --autogenerate -m "Auto-generated migration"
```

## 手动创建迁移文件

有时你需要手动创建迁移文件，特别是对于复杂的数据库操作：

```bash
uv run alembic revision -m "Add status column"
```

编辑生成的文件：

```python
# migrations/versions/003_add_status_column.py
from alembic import op
import sqlalchemy as sa

revision = '003'
down_revision = '002'

def upgrade():
    """Add status column to users table"""
    op.add_column('users', sa.Column('status', sa.String(20), default='active'))

def downgrade():
    """Remove status column"""
    op.drop_column('users', 'status')
```

## 迁移文件结构

```python
from alembic import op
import sqlalchemy as sa

revision = '003'              # 当前版本 ID
down_revision = '002'         # 上一个版本 ID
branch_labels = None
depends_on = None

def upgrade():
    """应用迁移 - 向前升级"""
    # 执行数据库变更
    op.create_table(...)
    op.add_column(...)
    op.drop_column(...)
    etc.

def downgrade():
    """回滚迁移 - 向后降级"""
    # 反向操作
    op.drop_table(...)
    op.drop_column(...)
    etc.
```

## 常见操作示例

### 创建表

```python
op.create_table(
    'products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(100), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
)
```

### 删除表

```python
op.drop_table('products')
```

### 添加列

```python
op.add_column('users', sa.Column('phone', sa.String(20)))
```

### 删除列

```python
op.drop_column('users', 'phone')
```

### 修改列

```python
op.alter_column('users', 'username', new_column_name='user_name')
```

### 添加索引

```python
op.create_index('idx_users_email', 'users', ['email'])
```

### 删除索引

```python
op.drop_index('idx_users_email')
```

### 添加约束

```python
op.create_unique_constraint('uq_users_email', 'users', ['email'])
```

### 执行原始 SQL

```python
op.execute("INSERT INTO users (username, email) VALUES ('admin', 'admin@example.com')")
```

## 项目中的迁移配置

### 1. 配置文件 (alembic.ini)

已在项目根目录配置好

### 2. 迁移脚本目录

```
migrations/
├── env.py                           # 迁移环境配置
└── versions/
    └── 001_initial_create_users_table.py  # 初始迁移
```

### 3. 运行迁移

```bash
# 应用迁移
uv run alembic upgrade head

# 回滚迁移
uv run alembic downgrade -1
```

## 最佳实践

✅ **DO**
- 每次数据库变更都创建一个迁移
- 使用 `--autogenerate` 自动生成迁移
- 编写有意义的迁移消息
- 测试迁移的 `upgrade` 和 `downgrade`
- 在版本控制中提交迁移文件

❌ **DON'T**
- 直接修改数据库，跳过迁移
- 删除或修改已应用的迁移文件
- 在迁移中执行复杂的业务逻辑
- 忽视迁移的 `downgrade` 部分

## 故障排除

### 迁移冲突

如果多个开发者创建了迁移：

```bash
# 查看迁移历史
uv run alembic history

# 编辑迁移文件的 down_revision，解决冲突
```

### 重置数据库

```bash
# 回滚所有迁移
uv run alembic downgrade base

# 重新应用所有迁移
uv run alembic upgrade head
```

### 检查当前版本

```bash
uv run alembic current
```

## 项目使用示例

### 场景 1：添加新的用户字段

```bash
# 修改 app/models/user.py，添加 phone 字段
# 自动生成迁移
uv run alembic revision --autogenerate -m "Add phone field to users"

# 应用迁移
uv run alembic upgrade head
```

### 场景 2：创建新的数据表

```bash
# 创建新模型
cat > app/models/category.py << 'EOF'
from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
EOF

# 生成迁移
uv run alembic revision --autogenerate -m "Create categories table"

# 应用迁移
uv run alembic upgrade head
```

## 参考资源

- [Alembic 官方文档](https://alembic.sqlalchemy.org/)
- [SQLAlchemy 数据类型](https://docs.sqlalchemy.org/en/20/core/types.html)
- [操作参考](https://alembic.sqlalchemy.org/en/latest/ops.html)
