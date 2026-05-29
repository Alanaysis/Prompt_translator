---
term: "Polling"
domain: software-engineering
aliases: ["轮询", "定时请求", "Short Polling"]
tags: [glossary, software-engineering]
---

# Polling

**别名**: 轮询, 定时请求, Short Polling

## 定义

**中文**: 通过定期发送 HTTP 请求来反复检查更新

**English**: Repeatedly checking for updates at regular intervals by making HTTP requests

> 💡 **Agent 提示**: Polling = repeatedly check for updates. '轮询'. Simple but wasteful. WebSocket/SSE better for real-time.

## 示例

- "用轮询获取最新状态"
  → 每隔几秒发一次请求检查数据是否有更新

## 关联术语

- [[software-engineering/WebSocket|WebSocket]]
- real-time
- [[natural-language/Streaming|SSE]]
