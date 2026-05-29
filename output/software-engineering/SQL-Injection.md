---
term: "SQL Injection"
domain: software-engineering
aliases: ["SQL 注入", "注入攻击"]
tags: [glossary, software-engineering]
---

# SQL Injection

**别名**: SQL 注入, 注入攻击

## 定义

**中文**: 利用数据库查询构造中的安全漏洞进行代码注入的技术

**English**: A code injection technique that exploits security vulnerabilities in database query construction

> 💡 **Agent 提示**: SQL Injection = malicious SQL via user input. 'SQL 注入'. Fix: parameterized queries, ORM. NEVER concatenate user input into SQL.

## 示例

- "这里可能有 SQL 注入风险"
  → 用户输入直接拼接到 SQL 语句中，可能被执行恶意 SQL

## 关联术语

- security
- [[software-engineering/XSS|XSS]]
- input-validation
