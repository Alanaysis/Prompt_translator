---
term: "Caching"
domain: software-engineering
aliases: ["缓存", "Cache", "缓存策略"]
tags: [glossary, software-engineering]
---

# Caching

**别名**: 缓存, Cache, 缓存策略

## 定义

**中文**: 将频繁访问的数据存储在更快的存储层中，以减少访问时间和后端负载

**English**: Storing frequently accessed data in a faster storage layer to reduce access time and backend load

> 💡 **Agent 提示**: Caching = storing data closer to consumer for speed. '加缓存' = add caching layer. Cache invalidation is a hard problem.

## 示例

- "加个缓存吧"
  → 在数据访问路径上增加缓存层来提升性能

- "缓存失效了"
  → 缓存中的数据过期或被清除，需要重新从数据源获取

## 关联术语

- Redis
- [[software-engineering/CDN|CDN]]
- cache-invalidation
- 性能优化

## 跨领域映射

### → product

- [[product/Retention|Retention]]
  📌 缓存提升性能从而提高留存
