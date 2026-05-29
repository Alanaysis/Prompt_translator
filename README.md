# Prompt_translator

> 把你的"人话"翻译成 agent 懂的"黑话"，再把 agent 的"黑话"翻译回你能理解的语言。

## 解决什么问题

Vibe coding 的时候，你和 coding agent 说的是两种语言：

| 你说的 | Agent 需要的 |
|--------|-------------|
| 先做个最简单的版本试试水 | 先用脚手架搭建 MVP，feature flag 控制灰度 |
| 这个功能太慢了，用户都跑了 | 接口延迟高导致跳出率高，需要缓存+索引优化 |
| 用户不喜欢用，留存太低 | 次日留存低，需要优化 onboarding 和 activation |

**Prompt_translator** 就是干这个的——它是一个**跨领域术语翻译知识库**，让你能用自己的话描述需求，agent 能用它理解的术语去实现。

## 核心功能

### 1. 跨领域翻译

从一个领域视角翻译到另一个领域：

```bash
# 产品说人话 → 翻译成工程术语
python tools/translate.py --from product --to software-engineering \
  "先做 MVP 验证一下用户痛点，用 AB 测试看转化率"

# 输出:
# 翻译: 先做 Scaffold 验证一下API，用 AB 测试看Feature Flag
#
# MVP → Scaffold 📌 快速搭建可运行的最小版本
# Pain Point → API 📌 痛点通常通过技术方案来解决
# Conversion Rate → Feature Flag 📌 通过功能开关做 A/B 测试优化转化率
```

```bash
# 工程说术语 → 翻译成产品能理解的
python tools/translate.py --from software-engineering --to product \
  "需要解耦，加个熔断和限流"

# 输出:
# 翻译: 需要Scoping，加个Churn和Conversion Rate
#
# Decoupling → Scoping 📌 解耦让范围界定更灵活
# Circuit Breaker → Churn 📌 熔断防止系统崩溃导致用户流失
# Rate Limiting → Conversion Rate 📌 限流保障服务稳定，维护转化率
```

### 2. 术语知识库

152 个术语，覆盖 3 个领域：

| 领域 | 术语数 | 覆盖内容 |
|------|--------|----------|
| [软件工程](./domains/software-engineering/) | 82 | 架构、DevOps、安全、数据库、测试、设计模式、Git |
| [产品](./domains/product/) | 39 | 敏捷、Scrum、用户研究、增长、分析、战略 |
| [自然语言](./domains/natural-language/) | 31 | LLM、提示工程、AI Agent、模型训练、RAG |

每个术语都有：
- 中英文定义
- 通俗解释和场景示例
- 跨领域关联映射
- 模型提示（给 agent 用的 hint）

### 3. 结构化数据

所有术语都是 JSON 格式，支持程序化查询和扩展：

```json
{
  "term": "MVP",
  "aliases": ["最小可行产品", "Minimum Viable Product"],
  "definition": {
    "en": "The simplest version of a product...",
    "zh": "产品最简单的版本，可以发布以测试核心假设..."
  },
  "cross_domain": {
    "software-engineering": [
      {"term": "Scaffold", "note": "快速搭建可运行的最小版本"}
    ]
  }
}
```

## 快速开始

### 安装

```bash
git clone https://github.com/Alanaysis/Prompt_translator.git
cd Prompt_translator
```

### 浏览术语

直接看各领域的 README：
- [软件工程术语索引](./domains/software-engineering/README.md)
- [产品术语索引](./domains/product/README.md)
- [自然语言与 AI 模型](./domains/natural-language/README.md)

### 使用翻译工具

```bash
# 产品 → 工程
python tools/translate.py --from product --to software-engineering "你的需求描述"

# 工程 → 产品
python tools/translate.py --from software-engineering --to product "你的技术方案"

# 列出所有领域
python tools/translate.py --list-domains

# 列出某个领域的所有术语
python tools/translate.py --list-terms product

# 交互模式
python tools/translate.py --interactive
```

### 配置

编辑 [config/primary-domain.json](./config/primary-domain.json) 设置你的默认领域：

```json
{
  "primary": "software-engineering",
  "fallback": "natural-language",
  "context": "你的项目描述"
}
```

## 术语格式

每个术语遵循 [term.schema.json](./schema/term.schema.json) 定义的格式：

| 字段 | 说明 |
|------|------|
| `term` | 主术语名 |
| `aliases` | 别名列表（中文、英文、缩写） |
| `definition` | 多语言定义 |
| `domain` | 所属领域 |
| `related` | 关联术语（可跨领域） |
| `cross_domain` | 显式跨领域映射（带说明） |
| `examples` | 使用示例 |
| `model_hints` | 给 LLM 的提示 |

## 目录结构

```
Prompt_translator/
├── README.md
├── CLAUDE.md                       # Agent 使用指南
├── schema/term.schema.json         # 术语 JSON Schema
├── domains/
│   ├── software-engineering/       # 82 个工程术语
│   │   ├── README.md
│   │   └── terms.json
│   ├── product/                    # 39 个产品术语
│   │   ├── README.md
│   │   └── terms.json
│   └── natural-language/           # 31 个 AI/NL 术语
│       ├── README.md
│       └── terms.json
├── config/
│   ├── primary-domain.json
│   └── vibe-link.json
└── tools/
    └── translate.py                # 跨领域翻译 CLI
```

## 如何贡献

### 添加术语

1. 编辑对应领域的 `terms.json`
2. 遵循 [term.schema.json](./schema/term.schema.json) 格式
3. 如果有跨领域关联，填写 `cross_domain` 字段
4. 提交 PR

### 添加新领域

1. 在 `domains/` 下创建新目录
2. 创建 `terms.json` 和 `README.md`
3. 更新主 README 的领域表格
4. 为现有术语添加到新领域的 `cross_domain` 映射

## Roadmap

- [x] Phase 1: 基础结构 + 152 个术语
- [x] Phase 2: 跨领域翻译 CLI
- [ ] Phase 3: Agent Skill（`/translate`）
- [ ] Phase 4: Obsidian 合并工具
- [ ] Phase 5: 社区化（CONTRIBUTING.md + CI 验证）

## License

MIT
