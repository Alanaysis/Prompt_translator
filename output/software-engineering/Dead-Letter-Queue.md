---
term: "Dead Letter Queue"
domain: software-engineering
aliases: ["死信队列", "DLQ"]
tags: [glossary, software-engineering]
---

# Dead Letter Queue

**别名**: 死信队列, DLQ

## 定义

**中文**: 无法成功处理的消息被发送到的队列，供后续分析

**English**: A queue where messages that cannot be processed successfully are sent for later analysis

> 💡 **Agent 提示**: Dead Letter Queue = where failed messages go. '死信队列'. For debugging, retry, or manual intervention.

## 示例

- "失败消息发到死信队列"
  → 处理失败的消息不要丢弃，放到 DLQ 后续排查

## 关联术语

- message-queue
- retry
- resilience
