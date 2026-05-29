---
term: "Race Condition"
domain: software-engineering
aliases: ["竞态条件", "竞态", "并发竞争"]
tags: [glossary, software-engineering]
---

# Race Condition

**别名**: 竞态条件, 竞态, 并发竞争

## 定义

**中文**: 系统行为取决于事件的相对时序，导致不可预测结果的缺陷

**English**: A bug where the behavior of a system depends on the relative timing of events, leading to unpredictable results

> 💡 **Agent 提示**: Race condition = timing-dependent bug in concurrent code. '竞态' = race condition. Fix with locks/mutexes/atomic ops.

## 示例

- "这里有竞态问题"
  → 并发执行时存在时序相关的 bug，可能导致数据不一致

## 关联术语

- concurrency
- thread-safety
- mutex
- deadlock
