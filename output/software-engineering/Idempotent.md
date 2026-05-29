---
term: "Idempotent"
domain: software-engineering
aliases: ["幂等", "幂等性"]
tags: [glossary, software-engineering]
---

# Idempotent

**别名**: 幂等, 幂等性

## 定义

**中文**: 执行一次和执行多次产生相同结果的操作特性

**English**: An operation that produces the same result whether it's executed once or multiple times

> 💡 **Agent 提示**: Idempotent = safe to repeat. Critical for payment APIs, retry logic. '幂等' = idempotent.

## 示例

- "这个接口要保证幂等"
  → 重复调用这个接口不能产生副作用（比如重复扣款）

## 关联术语

- API Design
- retry
- exactly-once
