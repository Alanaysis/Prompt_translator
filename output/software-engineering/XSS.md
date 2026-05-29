---
term: "XSS"
domain: software-engineering
aliases: ["跨站脚本", "Cross-Site Scripting"]
tags: [glossary, software-engineering]
---

# XSS

**别名**: 跨站脚本, Cross-Site Scripting

## 定义

**中文**: 将恶意脚本注入到其他用户查看的网页中的安全漏洞

**English**: A security vulnerability where malicious scripts are injected into web pages viewed by other users

> 💡 **Agent 提示**: XSS = inject malicious script into webpage. '跨站脚本'. Fix: escape user input, use CSP headers.

## 示例

- "这里有个 XSS 漏洞"
  → 用户输入没有转义，可能被注入恶意脚本

## 关联术语

- security
- [[software-engineering/CSRF|CSRF]]
- input-validation
