# vibe-glossary

> Vibe coding 的领域术语翻译知识库

## 这是什么

Vibe coding 时，你和 coding agent 之间有一道"语言鸿沟"：你不熟悉目标领域的行业黑话，agent 也不理解你的表达。

**vibe-glossary** 就是解决这个问题的——它是一个结构化的术语知识库，让你能用自己熟悉的话描述需求，agent 能用它理解的术语去实现。

## 核心理念

- **人能读懂**: 每个术语都有通俗解释和场景示例
- **机器能检索**: JSON Schema 结构化数据，支持程序化查询和翻译
- **双向翻译**: 你说"流水线"，agent 知道你说的是 CI/CD
- **跨领域链接**: 产品术语和工程术语之间有关联

## 包含哪些领域

| 领域 | 说明 | 术语数 |
|------|------|--------|
| [软件工程](./domains/software-engineering/) | 前后端、DevOps、架构、测试 | 30 |
| [产品](./domains/product/) | 产品管理、用户研究、增长 | 15 |
| [自然语言](./domains/natural-language/) | 中英文映射、模型语言偏好 | 11 |

## 快速开始

### 1. 浏览术语

直接看各领域的 README：
- [软件工程术语索引](./domains/software-engineering/README.md)
- [产品术语索引](./domains/product/README.md)
- [自然语言与模型偏好](./domains/natural-language/README.md)

### 2. 配置主领域

编辑 [config/primary-domain.json](./config/primary-domain.json)：

```json
{
  "primary": "software-engineering",
  "fallback": "natural-language",
  "context": "你的项目描述"
}
```

### 3. 关联 Vibe 项目

编辑 [config/vibe-link.json](./config/vibe-link.json)：

```json
{
  "project_path": "/path/to/your/project",
  "project_type": "web-app",
  "active_domains": ["software-engineering", "product"]
}
```

### 4. 使用翻译工具

```bash
# CLI 翻译
python tools/translate.py "这个接口延迟太高了" --from software-engineering --to natural-language

# Agent Skill（在 Claude Code 中）
/translate 这个接口延迟太高了
```

## 数据格式

每个术语遵循统一的 JSON Schema（见 [schema/term.schema.json](./schema/term.schema.json)）：

```json
{
  "term": "CI/CD",
  "aliases": ["持续集成", "流水线", "Pipeline"],
  "definition": {
    "en": "Practice of frequently integrating code changes...",
    "zh": "将代码变更频繁集成到共享仓库的实践..."
  },
  "domain": "software-engineering",
  "related": ["pipeline", "deployment"],
  "examples": [
    {
      "context": "我们用了 GitHub Actions 做 CI/CD",
      "meaning": "项目使用 GitHub Actions 实现自动化构建、测试、部署"
    }
  ],
  "model_hints": {
    "preferred_lang": "en",
    "prompt_fragment": "CI/CD = automated build-test-deploy pipeline"
  }
}
```

## 在 Obsidian 中使用

1. 用 Obsidian 打开整个 `vibe-glossary` 文件夹作为 vault
2. 各领域 README 中的锚点链接可以直接跳转
3. terms.json 可以通过 Obsidian 插件（如 Dataview）进行查询

## 目录结构

```
vibe-glossary/
├── README.md                       # 你在这里
├── CLAUDE.md                       # Agent 使用指南
├── schema/
│   └── term.schema.json            # 术语条目的 JSON Schema
├── domains/
│   ├── software-engineering/       # 软件工程术语
│   │   ├── README.md               # 人类可读索引
│   │   └── terms.json              # 机器可读数据
│   ├── product/                    # 产品术语
│   │   ├── README.md
│   │   └── terms.json
│   └── natural-language/           # 自然语言映射
│       ├── README.md
│       └── terms.json
├── config/
│   ├── primary-domain.json         # 主领域配置
│   └── vibe-link.json              # Vibe 项目关联
└── tools/
    ├── translate.py                # CLI 翻译工具
    └── merge.py                    # Obsidian 合并工具
```

## 添加新术语

1. 在对应领域的 `terms.json` 中添加条目
2. 遵循 [term.schema.json](./schema/term.schema.json) 的格式
3. 在对应领域的 `README.md` 中添加索引和详细条目
4. 如果有跨领域关联，在 `related` 字段中引用

## 添加新领域

1. 在 `domains/` 下创建新目录
2. 创建 `terms.json` 和 `README.md`
3. 更新主 README 的领域表格

## Roadmap

- [x] Phase 1: 基础结构 + 首批术语
- [ ] Phase 2: CLI 翻译工具
- [ ] Phase 3: Agent Skill (`/translate`)
- [ ] Phase 4: Obsidian 合并工具
- [ ] Phase 5: 社区化（CONTRIBUTING.md + CI 验证）
