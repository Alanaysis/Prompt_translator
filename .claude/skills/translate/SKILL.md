---
name: translate
description: 跨领域术语翻译 — 将一个领域视角的描述翻译成另一个领域的术语体系
argument-hint: "[--from domain] [--to domain] <text>"
when_to_use: 用户要求翻译术语、将产品需求转为技术方案、或将技术描述转为产品语言时
allowed-tools: Bash Read
---

## 任务

将用户输入的文本从一个领域视角翻译到另一个领域视角。

## 执行步骤

1. 解析用户的输入：
   - 如果包含 `--from` 和 `--to` 参数，使用指定的领域
   - 如果没有指定领域，根据内容自动判断源领域和目标领域
   - 可用领域: `software-engineering`, `product`, `natural-language`

2. 调用翻译工具：
   ```bash
   cd ${CLAUDE_SKILL_DIR}/../.. && python3 tools/translate.py --from <source> --to <target> "<text>"
   ```

3. 将输出格式化展示给用户，包含：
   - 翻译后的句子
   - 术语映射关系和说明
   - 未找到映射的术语（如有）

## 领域判断规则

- 包含 MVP、痛点、用户故事、转化率、留存、PMF、路线图 → 源领域为 `product`
- 包含 API、CI/CD、重构、微服务、缓存、部署、架构 → 源领域为 `software-engineering`
- 包含 prompt、token、embedding、RAG、fine-tune → 源领域为 `natural-language`
- 目标领域默认为另一个最相关的领域

## 输出格式

直接展示翻译结果，不需要额外解释。如果用户需要更多信息，再补充说明。

## 示例用法

用户输入: `/translate 先做 MVP 验证一下用户痛点`
执行: `python3 tools/translate.py --from product --to software-engineering "先做 MVP 验证一下用户痛点"`

用户输入: `/translate --from engineering --to product 需要解耦加熔断`
执行: `python3 tools/translate.py --from software-engineering --to product "需要解耦加熔断"`

## 输入

$ARGUMENTS
