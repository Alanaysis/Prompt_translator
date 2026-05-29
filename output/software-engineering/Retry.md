---
term: "Retry"
domain: software-engineering
aliases: ["重试", "自动重试", "Retry Policy"]
tags: [glossary, software-engineering]
---

# Retry

**别名**: 重试, 自动重试, Retry Policy

## 定义

**中文**: 自动重试失败的操作，通常使用指数退避策略

**English**: Automatically retrying a failed operation, often with exponential backoff

> 💡 **Agent 提示**: Retry = try again on failure. '重试'. Use exponential backoff. Only retry idempotent operations.

## 示例

- "接口超时了，自动重试一下"
  → 调用失败后等待一段时间再重试，通常是指数退避

## 关联术语

- circuit-breaker
- resilience
- idempotent
