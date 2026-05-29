---
term: "Caching Strategy"
domain: software-engineering
aliases: ["缓存策略", "Cache Aside", "Read Through", "Write Through", "Write Behind"]
tags: [glossary, software-engineering]
---

# Caching Strategy

**别名**: 缓存策略, Cache Aside, Read Through, Write Through, Write Behind

## 定义

**中文**: 关于何时以及如何填充、失效和更新缓存数据的方法

**English**: The approach for when and how to populate, invalidate, and update cached data

> 💡 **Agent 提示**: Cache Aside = app manages cache. Read/Write Through = cache manages itself. '缓存策略' = caching strategy.

## 示例

- "用 Cache Aside 模式"
  → 应用先查缓存，没有再查数据库，然后更新缓存

## 关联术语

- caching
- Redis
- cache-invalidation
- 性能优化
