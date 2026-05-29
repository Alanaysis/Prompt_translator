---
term: "CSRF"
domain: software-engineering
aliases: ["跨站请求伪造", "Cross-Site Request Forgery"]
tags: [glossary, software-engineering]
---

# CSRF

**别名**: 跨站请求伪造, Cross-Site Request Forgery

## 定义

**中文**: 欺骗用户浏览器向已认证的网站发送非预期请求的攻击方式

**English**: An attack that tricks a user's browser into making unwanted requests to a site where they're authenticated

> 💡 **Agent 提示**: CSRF = trick browser into unwanted requests. '跨站请求伪造'. Fix: CSRF tokens, SameSite cookies.

## 示例

- "加个 CSRF token 防护"
  → 在表单中添加一次性令牌，防止跨站请求伪造

## 关联术语

- security
- [[software-engineering/XSS|XSS]]
- authentication
