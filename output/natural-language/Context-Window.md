---
term: "Context Window"
domain: natural-language
aliases: ["上下文窗口", "上下文长度", "Context Length"]
tags: [glossary, natural-language]
---

# Context Window

**别名**: 上下文窗口, 上下文长度, Context Length

## 定义

**中文**: LLM 在单次对话轮次中能处理的最大文本量（以 token 计）

**English**: The maximum amount of text (in tokens) an LLM can process in a single conversation turn

> 💡 **Agent 提示**: Context window = max tokens per turn. '上下文窗口'. Claude: 200k, GPT-4: 128k. Exceeding it = losing earlier context.

## 示例

- "上下文窗口不够了"
  → 对话历史太长，超出模型能处理的范围

## 关联术语

- token
- prompt-engineering
- memory
