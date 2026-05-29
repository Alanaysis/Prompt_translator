# vibe-glossary — Agent 使用指南

## 这是什么

一个领域术语翻译知识库，用于 vibe coding 时消除用户和 agent 之间的"语言鸿沟"。

## 如何使用

### 浏览术语

当用户提到你不熟悉的行业术语时：
1. 先在对应领域的 `terms.json` 中搜索
2. 如果找不到，尝试在 `related` 字段中查找关联术语
3. 查看 `examples` 字段了解实际用法

### 翻译术语

当用户用自己的术语描述需求时：
1. 读取 `config/primary-domain.json` 确定主领域
2. 在主领域的 `terms.json` 中匹配用户输入（包括 `aliases`）
3. 用 `model_hints.prompt_fragment` 理解术语含义
4. 用 `definition.en` 作为标准术语回复

### 跨领域关联

当用户的需求涉及多个领域时：
1. 通过 `related` 字段找到跨领域关联
2. 使用各领域的 README 中的链接进行跳转
3. 综合多领域术语给出完整解释

## 关键文件

- `config/primary-domain.json` — 主领域和 fallback 配置
- `config/vibe-link.json` — 当前关联的 vibe 项目信息
- `domains/*/terms.json` — 结构化术语数据
- `domains/*/README.md` — 人类可读的术语索引
- `schema/term.schema.json` — 术语条目的 JSON Schema

## 翻译策略

1. **精确匹配优先**: 先在 `term` 和 `aliases` 中精确匹配
2. **语义匹配次之**: 如果精确匹配失败，用语义理解匹配最相关的术语
3. **保持原意**: 翻译时保留用户的核心意图，不要过度解读
4. **附上原文**: 翻译后附上英文/中文原文，确保理解一致

## 添加新术语

当发现用户频繁使用某个术语但知识库中没有时：
1. 提示用户是否要添加
2. 按照 `schema/term.schema.json` 的格式创建条目
3. 更新对应领域的 README
