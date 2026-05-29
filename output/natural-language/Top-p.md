---
term: "Top-p"
domain: natural-language
aliases: ["核采样", "Nucleus Sampling", "Top-p Sampling"]
tags: [glossary, natural-language]
---

# Top-p

**别名**: 核采样, Nucleus Sampling, Top-p Sampling

## 定义

**中文**: 将 token 选择限制在累积概率超过 p 的最小集合中的采样参数

**English**: A sampling parameter that limits token selection to the smallest set whose cumulative probability exceeds p

> 💡 **Agent 提示**: Top-p = nucleus sampling. '核采样'. 0.9 = consider top 90% probability mass. Often used with temperature.

## 示例

- "top-p 设成 0.9"
  → 只从累积概率前 90% 的 token 中采样

## 关联术语

- temperature
- sampling
- creativity
