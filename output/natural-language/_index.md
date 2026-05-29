---
domain: natural-language
tags: [glossary, index]
---

# natural-language 术语索引

共 31 个术语

- [[Agent|Agent]] — 能自主使用工具、做决策和执行操作来完成任务的 AI 系统
- [[Alignment|Alignment]] — 确保 AI 系统的行为符合人类价值观和意图
- [[Chain-of-Thought|Chain of Thought]] — 要求模型在给出最终答案前逐步展示推理过程的提示技术
- [[Context|Context]] — 提供给模型以帮助其理解和适当回复的背景信息
- [[Context-Window|Context Window]] — LLM 在单次对话轮次中能处理的最大文本量（以 token 计）
- [[Embedding|Embedding]] — 将文本转换为捕获语义含义的数值向量表示
- [[Few-shot|Few-shot]] — 在提示词中提供少量示例来引导模型的输出格式和风格
- [[Fine-tuning|Fine-tuning]] — 在预训练模型基础上用特定领域数据进一步训练，以提升特定任务的表现
- [[Grounding|Grounding]] — 将 LLM 输出连接到经过验证的真实数据源，以减少幻觉
- [[Guardrails|Guardrails]] — 约束 LLM 输出以防止有害、不正确或偏离主题回复的安全机制
- [[Hallucination|Hallucination]] — LLM 生成听起来合理但实际上不正确或捏造的信息
- [[Instruction-Tuning|Instruction Tuning]] — 用指令-响应对微调模型以提高其遵循指令的能力
- [[Latency-AI|Latency (AI)]] — 从发送请求到收到模型第一个响应 token 之间的时间延迟
- [[Max-Tokens|Max Tokens]] — 模型在响应中生成的最大 token 数量
- [[Multimodal|Multimodal]] — 能处理和生成多种数据类型（文本、图像、音频、视频）的 AI 模型
- [[Prompt-Engineering|Prompt Engineering]] — 设计有效提示词以从 LLM 获得期望输出的实践
- [[RAG|RAG]] — 将 LLM 生成与从外部知识库检索信息相结合的技术
- [[RLHF|RLHF]] — 使用人类偏好作为奖励信号来对齐模型行为的训练技术
- [[Semantic-Search|Semantic Search]] — 基于含义而非精确关键词匹配的搜索，使用嵌入和相似度
- [[Stop-Sequence|Stop Sequence]] — 告诉模型停止生成更多 token 的特定字符串
- [[Streaming|Streaming]] — 逐个 token 生成并返回 AI 响应，而不是等待完整响应
- [[System-Prompt|System Prompt]] — 在对话开始前给 LLM 的特殊指令，定义其行为、角色和约束
- [[Temperature|Temperature]] — 控制 LLM 输出随机性的参数。越低越确定，越高越有创造性
- [[Token|Token]] — LLM 文本处理的基本单位，英文约 3/4 个单词，中文约 1-2 个字符
- [[Token-Limit|Token Limit]] — 模型在单次请求中能处理的最大 token 总数（输入 + 输出）
- [[Tool-Use|Tool Use]] — LLM 调用外部工具（API、计算器、数据库）以增强自身能力的特性
- [[Top-p|Top-p]] — 将 token 选择限制在累积概率超过 p 的最小集合中的采样参数
- [[Vector-Database|Vector Database]] — 针对存储和搜索高维向量（嵌入）优化的数据库
- [[Zero-shot|Zero-shot]] — 在提示词中不提供任何示例就让模型执行任务
- [[中英文混用|中英文混用]] — 中文技术社区中常见的中英文混合交流方式
- [[术语一致性|术语一致性]] — 在项目中一致使用相同术语以避免混淆（例如，不要混用'用户'和'账号'来指同一概念）