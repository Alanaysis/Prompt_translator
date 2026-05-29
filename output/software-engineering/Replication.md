---
term: "Replication"
domain: software-engineering
aliases: ["复制", "主从复制", "读写分离", "Replica"]
tags: [glossary, software-engineering]
---

# Replication

**别名**: 复制, 主从复制, 读写分离, Replica

## 定义

**中文**: 将数据从一个数据库服务器复制到一个或多个其他服务器，用于冗余和读扩展

**English**: Copying data from one database server to one or more others for redundancy and read scalability

> 💡 **Agent 提示**: Replication = copy data to multiple servers. '复制'/'主从复制'. Primary handles writes, replicas handle reads.

## 示例

- "用主从复制做读写分离"
  → 主库负责写入，从库负责读取，分摊压力

## 关联术语

- database
- sharding
- availability
