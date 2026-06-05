# ClickHouse 使用指南

本文档介绍如何在项目中集成 ClickHouse，用于 OLAP / 分析型查询场景。包含驱动安装、连接示例、常用用途建议（例如事件/日志聚合）、以及使用 Docker 启动 ClickHouse 的示例。

目录
- 适用场景
- 安装驱动
- Docker Compose 示例
- .env 配置
- 连接示例
- 与 SQLAlchemy 集成（可选）
- 在项目中使用 ClickHouse（写入/查询）
- ClickHouse 表建模建议
- 迁移与 schema 管理
- 常见问题与优化

---

适用场景

ClickHouse 是为 OLAP 设计的列式数据库，适合：
- 大规模事件、日志、分析数据的写入与聚合
- 实时或近实时分析仪表盘
- 不作为事务数据库（不适合频繁的小事务写入/更新）

安装驱动

常用驱动：
- 官方驱动 `clickhouse-driver`（binary protocol）
- HTTP 驱动 `clickhouse-connect` 或 `clickhouse-driver` 的 http 模式
- SQLAlchemy 支持: `clickhouse-sqlalchemy`（有限支持）

安装示例：

```bash
uv add clickhouse-driver
# 如果需要 SQLAlchemy 方言支持
uv add clickhouse-sqlalchemy
```

Docker Compose 示例

```yaml
services:
  clickhouse:
    image: clickhouse/clickhouse-server:latest
    ports:
      - "8123:8123"  # HTTP
      - "9000:9000"  # Native TCP
    volumes:
      - clickhouse_data:/var/lib/clickhouse

volumes:
  clickhouse_data:
```

.env 配置示例

```bash
# ClickHouse 配置
CLICKHOUSE_HOST=localhost
CLICKHOUSE_PORT=9000
CLICKHOUSE_USER=default
CLICKHOUSE_PASSWORD=
CLICKHOUSE_DATABASE=default
```

连接示例（使用 `clickhouse-driver`）

```python
from clickhouse_driver import Client
from app.config import settings

client = Client(
    host=settings.CLICKHOUSE_HOST,
    port=settings.CLICKHOUSE_PORT,
    user=settings.CLICKHOUSE_USER,
    password=settings.CLICKHOUSE_PASSWORD,
    database=settings.CLICKHOUSE_DATABASE,
)

# 写入单行
client.execute("INSERT INTO events (ts, user_id, action) VALUES", [
    (int(time.time()), 1, 'login'),
])

# 批量写入
data = [(ts1, uid1, 'click'), (ts2, uid2, 'view'), ...]
client.execute('INSERT INTO events (ts, user_id, action) VALUES', data)

# 查询
rows = client.execute('SELECT user_id, count() FROM events WHERE ts >= now() - 3600 GROUP BY user_id')
```

与 SQLAlchemy 集成（可选）

ClickHouse 对 SQLAlchemy 的支持并不完美，但 `clickhouse-sqlalchemy` 提供了一个方言。示例：

```python
# 使用 clickhouse-sqlalchemy
from sqlalchemy import create_engine, text

# dialects: clickhouse+native://user:passwd@host:9000/database
CLICKHOUSE_URL = f'clickhouse+native://{user}:{password}@{host}:{port}/{database}'
engine = create_engine(CLICKHOUSE_URL)

with engine.connect() as conn:
    conn.execute(text("SELECT count() FROM events"))
```

注意：
- `clickhouse-sqlalchemy` 支持 CREATE/SELECT 等 DDL/DML，但并不适合复杂 ORM 操作。
- ClickHouse 不支持传统意义上的事务和行级更新（存在替代策略，如使用 ReplacingMergeTree）。

在项目中使用 ClickHouse（实践建议）

- 将 ClickHouse 用作事件/日志/分析的写入端：在业务主数据库（MySQL）写入事务后，异步将事件发送到 ClickHouse（通过队列如 Kafka、RabbitMQ、或后台任务）
- 批量写入：将多条事件打包后再批量插入以提高吞吐量
- 使用 MergeTree 系列表引擎（例如：MergeTree、ReplacingMergeTree、SummingMergeTree）根据需求选择

示例：在 FastAPI 中异步写入 ClickHouse（使用后台任务）

```python
from fastapi import BackgroundTasks
from app.db.clickhouse_client import client

async def write_event_background(event: dict):
    # 后台任务：批量化逻辑应该在真正生产代码中实现
    client.execute('INSERT INTO events (ts, user_id, action) VALUES', [
        (event['ts'], event['user_id'], event['action'])
    ])

@router.post('/events')
async def create_event(event: EventSchema, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_event_background, event.dict())
    return {'status': 'accepted'}
```

ClickHouse 表建模建议

- 使用合适的分区键和排序键（ORDER BY）提高查询性能
- 对于常见的聚合查询，使用 Summing/Collapsing/SummingMergeTree 等引擎
- 使用 TTL 删除旧数据（例如：保留 90 天）
- 避免频繁更新行；若需要更新，可采用版本化（ReplacingMergeTree）或物化视图

迁移与 schema 管理

- ClickHouse 不适合使用 Alembic：推荐使用脚本化的迁移方式或专门的迁移工具，如 `clickhouse-migrations`、`yandex/clickhouse-migrations` 或者将 DDL 脚本放在 repo 中，由 CI/CD 执行
- 示例脚本目录：

```
clickhouse_migrations/
├── 001_create_events_table.sql
├── 002_add_index_example.sql
```

脚本示例（001_create_events_table.sql）：

```sql
CREATE TABLE IF NOT EXISTS events (
    ts UInt32,
    user_id UInt64,
    action String,
    url String
) ENGINE = MergeTree()
ORDER BY (user_id, ts)
PARTITION BY toYYYYMM(ts)
TTL ts + toIntervalDay(90) DELETE
```

常见问题与优化

- 写入延迟/丢失：确保批量插入并使用重试策略，建议使用消息队列中转
- 内存使用过高：监控 MergeTree 索引和合并任务，调整 `max_memory_usage` 等配置
- 查询慢：检查 ORDER BY、索引以及分区策略

总结

- MySQL 用于事务与在线业务数据
- ClickHouse 用于分析与日志聚合
- 推荐把两者结合：业务写 MySQL（保证 ACID），事件或分析数据异步写 ClickHouse（高吞吐聚合查询）

更多参考：
- ClickHouse 官方文档: https://clickhouse.com/docs/
