---
term: "Graceful Degradation"
domain: software-engineering
aliases: ["优雅降级", "降级"]
tags: [glossary, software-engineering]
---

# Graceful Degradation

**别名**: 优雅降级, 降级

## 定义

**中文**: 系统在部分组件故障时仍能以降级功能继续运行的能力

**English**: A system's ability to continue operating with reduced functionality when some components fail

> 💡 **Agent 提示**: Graceful Degradation = reduced functionality rather than total failure. '优雅降级'. Return cached/default data when service is down.

## 示例

- "服务挂了就降级返回默认值"
  → 依赖服务不可用时，返回缓存数据或默认值而不是报错

## 关联术语

- circuit-breaker
- resilience
- fallback
