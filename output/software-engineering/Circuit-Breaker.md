---
term: "Circuit Breaker"
domain: software-engineering
aliases: ["熔断", "熔断器", "断路器"]
tags: [glossary, software-engineering]
---

# Circuit Breaker

**别名**: 熔断, 熔断器, 断路器

## 定义

**中文**: 通过停止调用故障服务并返回降级响应来防止级联失败的模式

**English**: A pattern that prevents cascading failures by stopping calls to a failing service and returning a fallback response

> 💡 **Agent 提示**: Circuit Breaker = stop calling failing service. '熔断'. States: closed → open → half-open. Prevents cascade failures.

## 示例

- "加个熔断，防止雪崩"
  → 当下游服务故障时，快速失败而不是让请求堆积

## 关联术语

- resilience
- retry
- fallback
- microservices

## 跨领域映射

### → product

- [[product/Churn|Churn]]
  📌 熔断防止系统崩溃导致用户流失
