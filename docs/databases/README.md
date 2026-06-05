# 数据库使用文档总览

本文件夹包含针对项目中可选数据库的使用文档：
- MySQL（事务型数据库）: mysql.md
- ClickHouse（分析型数据库）: clickhouse.md

建议流程：
1. 根据业务需求选择数据库（或组合使用）
2. 配置 `.env` 中的连接字符串
3. 对 MySQL 使用 Alembic 管理迁移
4. 对 ClickHouse 使用脚本化迁移或专用迁移工具

文档位置: `docs/databases/`
