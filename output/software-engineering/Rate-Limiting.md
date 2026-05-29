---
term: "Rate Limiting"
domain: software-engineering
aliases: ["限流", "频率限制", "Rate Limit"]
tags: [glossary, software-engineering]
---

# Rate Limiting

**别名**: 限流, 频率限制, Rate Limit

## 定义

**中文**: 控制客户端在一段时间内可以发送的请求数量

**English**: Controlling the number of requests a client can make within a time period

> 💡 **Agent 提示**: Rate Limiting = cap requests per time period. '限流'. Algorithms: token bucket, sliding window. Return 429 when exceeded.

## 示例

- "接口加个限流"
  → 限制每个用户每分钟最多调用多少次，防止滥用

## 关联术语

- [[software-engineering/API|API]]
- security
- throttling

## 跨领域映射

### → product

- [[product/Conversion-Rate|Conversion Rate]]
  📌 限流保障服务稳定，维护转化率
