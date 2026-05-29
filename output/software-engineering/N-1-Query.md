---
term: "N+1 Query"
domain: software-engineering
aliases: ["N+1 问题", "N+1 查询"]
tags: [glossary, software-engineering]
---

# N+1 Query

**别名**: N+1 问题, N+1 查询

## 定义

**中文**: 获取 N 条数据需要 N+1 次数据库查询（而非 1-2 次）的性能反模式

**English**: A performance anti-pattern where fetching a list of N items requires N+1 database queries instead of 1-2

> 💡 **Agent 提示**: N+1 query = fetch list + each item separately. 'N+1 问题'. Fix: eager loading, batch query. Common ORM pitfall.

## 示例

- "这里有 N+1 问题"
  → 循环中每次迭代都查询数据库，应该改为批量查询

## 关联术语

- [[software-engineering/ORM|ORM]]
- performance
- database
