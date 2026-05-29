---
term: "Blue-Green Deployment"
domain: software-engineering
aliases: ["蓝绿部署", "蓝绿发布"]
tags: [glossary, software-engineering]
---

# Blue-Green Deployment

**别名**: 蓝绿部署, 蓝绿发布

## 定义

**中文**: 维护两个相同环境的部署策略；流量从蓝色（当前）切换到绿色（新版）

**English**: A deployment strategy with two identical environments; traffic switches from blue (current) to green (new)

> 💡 **Agent 提示**: Blue-Green = two identical envs, switch traffic. '蓝绿部署'. Instant rollback by switching back.

## 示例

- "用蓝绿部署，方便回滚"
  → 同时维护新旧两套环境，切换流量即可回滚

## 关联术语

- deployment
- canary-release
- rollback
