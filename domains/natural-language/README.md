# 自然语言与 AI 模型术语库 / Natural Language & AI Glossary

> 涵盖 LLM、提示工程、模型训练、AI Agent 等自然语言和 AI 领域的核心术语。
>
> 机器可读数据：[terms.json](./terms.json) | 共 31 个术语

## 术语索引

| 术语 | 别名 | 一句话解释 |
|------|------|-----------|
| [中英文混用](#中英文混用) | Chinglish in tech, 中英夹杂 | 中文技术社区中常见的中英文混合交流方式 |
| [术语一致性](#术语一致性) | terminology consistency, 术语统一 | 在项目中一致使用相同术语以避免混淆（例如，不要混用'用户'和'账号'来指同一概念） |
| [Context Window](#context-window) | 上下文窗口, 上下文长度, Context Length | LLM 在单次对话轮次中能处理的最大文本量（以 token 计） |
| [Prompt Engineering](#prompt-engineering) | 提示词工程, 提示工程, Prompt | 设计有效提示词以从 LLM 获得期望输出的实践 |
| [Few-shot](#few-shot) | 少样本, 少样本学习, Few-shot Learning | 在提示词中提供少量示例来引导模型的输出格式和风格 |
| [Hallucination](#hallucination) | 幻觉, AI 幻觉, 胡说八道 | LLM 生成听起来合理但实际上不正确或捏造的信息 |
| [Grounding](#grounding) | 接地, 事实锚定, 基于事实 | 将 LLM 输出连接到经过验证的真实数据源，以减少幻觉 |
| [RAG](#rag) | 检索增强生成, Retrieval-Augmented Generation | 将 LLM 生成与从外部知识库检索信息相结合的技术 |
| [Token](#token) | 词元, Token | LLM 文本处理的基本单位，英文约 3/4 个单词，中文约 1-2 个字符 |
| [Temperature](#temperature) | 温度, 随机性 | 控制 LLM 输出随机性的参数。越低越确定，越高越有创造性 |
| [System Prompt](#system-prompt) | 系统提示词, 系统指令, System Message | 在对话开始前给 LLM 的特殊指令，定义其行为、角色和约束 |
| [Fine-tuning](#fine-tuning) | 微调, 模型微调, Fine-tune | 在预训练模型基础上用特定领域数据进一步训练，以提升特定任务的表现 |
| [Embedding](#embedding) | 向量嵌入, 向量化, 词向量 | 将文本转换为捕获语义含义的数值向量表示 |
| [Vector Database](#vector-database) | 向量数据库, 向量检索 | 针对存储和搜索高维向量（嵌入）优化的数据库 |
| [Semantic Search](#semantic-search) | 语义搜索, 语义检索 | 基于含义而非精确关键词匹配的搜索，使用嵌入和相似度 |
| [Chain of Thought](#chain-of-thought) | 思维链, CoT, 逐步推理 | 要求模型在给出最终答案前逐步展示推理过程的提示技术 |
| [Guardrails](#guardrails) | 护栏, 安全护栏, 输出约束 | 约束 LLM 输出以防止有害、不正确或偏离主题回复的安全机制 |
| [Agent](#agent) | AI Agent, 智能体, 自主代理 | 能自主使用工具、做决策和执行操作来完成任务的 AI 系统 |
| [Tool Use](#tool-use) | 工具调用, Function Calling, 工具使用 | LLM 调用外部工具（API、计算器、数据库）以增强自身能力的特性 |
| [Zero-shot](#zero-shot) | 零样本, 零样本学习 | 在提示词中不提供任何示例就让模型执行任务 |
| [Top-p](#top-p) | 核采样, Nucleus Sampling, Top-p Sampling | 将 token 选择限制在累积概率超过 p 的最小集合中的采样参数 |
| [Max Tokens](#max-tokens) | 最大 token 数, 最大长度, 输出长度限制 | 模型在响应中生成的最大 token 数量 |
| [Stop Sequence](#stop-sequence) | 停止序列, 终止符, Stop Token | 告诉模型停止生成更多 token 的特定字符串 |
| [Context](#context) | 上下文, 上下文信息, Context Information | 提供给模型以帮助其理解和适当回复的背景信息 |
| [Instruction Tuning](#instruction-tuning) | 指令微调, 指令调优 | 用指令-响应对微调模型以提高其遵循指令的能力 |
| [RLHF](#rlhf) | 人类反馈强化学习, Reinforcement Learning from Human Feedback | 使用人类偏好作为奖励信号来对齐模型行为的训练技术 |
| [Alignment](#alignment) | 对齐, 价值对齐, AI 对齐 | 确保 AI 系统的行为符合人类价值观和意图 |
| [Multimodal](#multimodal) | 多模态, 多模态模型 | 能处理和生成多种数据类型（文本、图像、音频、视频）的 AI 模型 |
| [Token Limit](#token-limit) | token 限制, 上下文限制 | 模型在单次请求中能处理的最大 token 总数（输入 + 输出） |
| [Latency (AI)](#latency-(ai)) | 推理延迟, 首 token 延迟, TTFT | 从发送请求到收到模型第一个响应 token 之间的时间延迟 |
| [Streaming](#streaming) | 流式输出, 流式响应, SSE | 逐个 token 生成并返回 AI 响应，而不是等待完整响应 |

---

## 详细条目

### 中英文混用
**中文**: 中文技术社区中常见的中英文混合交流方式

**English**: The common practice in Chinese tech communities of mixing Chinese and English in technical communication

**提示**: 中英混用是正常的。保留关键术语的英文原文可以提高准确性。翻译时不要强行统一语言。

**示例**: "这个 component 的 state 管理用 Redux 还是 Zustand？" → 技术讨论中自然地混用中英文，核心术语用英文

---

### 术语一致性
**中文**: 在项目中一致使用相同术语以避免混淆（例如，不要混用'用户'和'账号'来指同一概念）

**English**: Using the same term consistently throughout a project to avoid confusion (e.g., don't mix 'user' and 'account' for the same concept)

**提示**: 术语一致性 = always use same word for same concept. Important in code, docs, and communication. '术语统一'.

**示例**: "代码里叫 user，文档里叫 account，到底叫什么？" → 术语不一致导致团队理解混乱

---

### Context Window
**中文**: LLM 在单次对话轮次中能处理的最大文本量（以 token 计）

**English**: The maximum amount of text (in tokens) an LLM can process in a single conversation turn

**提示**: Context window = max tokens per turn. '上下文窗口'. Claude: 200k, GPT-4: 128k. Exceeding it = losing earlier context.

**示例**: "上下文窗口不够了" → 对话历史太长，超出模型能处理的范围

---

### Prompt Engineering
**中文**: 设计有效提示词以从 LLM 获得期望输出的实践

**English**: The practice of crafting effective prompts to get desired outputs from LLMs

**提示**: Prompt engineering = crafting effective inputs for LLMs. '提示词工程'. Key: clear instructions, examples, constraints.

**示例**: "需要优化一下 prompt" → 需要改进提示词的表述，让 AI 输出更准确

---

### Few-shot
**中文**: 在提示词中提供少量示例来引导模型的输出格式和风格

**English**: Providing a few examples in the prompt to guide the model's output format and style

**提示**: Few-shot = give examples in prompt. Zero-shot = no examples. One-shot = one example. '少样本'.

**示例**: "用 few-shot 的方式给几个例子" → 在提示词中附上几个输入-输出示例，让模型学习格式

---

### Hallucination
**中文**: LLM 生成听起来合理但实际上不正确或捏造的信息

**English**: When an LLM generates plausible-sounding but factually incorrect or fabricated information

**提示**: Hallucination = AI makes things up. '幻觉'. Always verify factual claims. Use grounding/RAG to reduce.

**示例**: "AI 在幻觉" → AI 编造了不存在的信息，需要验证

---

### Grounding
**中文**: 将 LLM 输出连接到经过验证的真实数据源，以减少幻觉

**English**: Connecting LLM outputs to verified, real-world data sources to reduce hallucination

**提示**: Grounding = tie AI output to real data. Opposite of hallucination. RAG is a common grounding technique.

**示例**: "需要 grounding 一下" → 需要把 AI 的回答基于真实数据来验证

---

### RAG
**中文**: 将 LLM 生成与从外部知识库检索信息相结合的技术

**English**: A technique that combines LLM generation with information retrieval from external knowledge bases

**提示**: RAG = retrieve relevant docs, then generate answer. '检索增强生成'. Reduces hallucination for domain-specific Q&A.

**示例**: "用 RAG 接入知识库" → 用检索增强的方式让 AI 基于特定知识库回答问题

---

### Token
**中文**: LLM 文本处理的基本单位，英文约 3/4 个单词，中文约 1-2 个字符

**English**: The basic unit of text processing in LLMs, roughly 3/4 of a word in English or 1-2 characters in Chinese

**提示**: Token = basic text unit for LLMs. '词元'. English: ~0.75 word/token. Chinese: ~1-2 chars/token. Affects cost and context.

**示例**: "这个 prompt 多少 token？" → 这段提示词有多少个 token？影响成本和上下文占用

---

### Temperature
**中文**: 控制 LLM 输出随机性的参数。越低越确定，越高越有创造性

**English**: A parameter controlling the randomness of LLM output. Lower = more deterministic, Higher = more creative

**提示**: Temperature = randomness control. '温度'. 0 = deterministic, 1 = creative, >1 = very random. Code: use low temp.

**示例**: "temperature 调低一点" → 减少随机性，让输出更确定和一致

---

### System Prompt
**中文**: 在对话开始前给 LLM 的特殊指令，定义其行为、角色和约束

**English**: A special instruction given to an LLM before the conversation starts, defining its behavior, persona, and constraints

**提示**: System prompt = instruction before conversation. '系统提示词'. Sets persona, rules, constraints. Hidden from end users.

**示例**: "在 system prompt 里加上约束" → 在系统提示词中定义 AI 的行为规则和限制

---

### Fine-tuning
**中文**: 在预训练模型基础上用特定领域数据进一步训练，以提升特定任务的表现

**English**: Further training a pre-trained model on domain-specific data to improve performance for specific tasks

**提示**: Fine-tuning = further train model on specific data. '微调'. Cheaper than training from scratch. Use when prompts aren't enough.

**示例**: "需要微调一下模型" → 用领域数据进一步训练通用模型，使其更擅长特定任务

---

### Embedding
**中文**: 将文本转换为捕获语义含义的数值向量表示

**English**: Converting text into a numerical vector representation that captures semantic meaning

**提示**: Embedding = text → vector. '向量嵌入'. Similar meanings = nearby vectors. Foundation of RAG, semantic search.

**示例**: "把文档 embedding 后存到向量数据库" → 将文档转换为向量，存入向量数据库以支持语义搜索

---

### Vector Database
**中文**: 针对存储和搜索高维向量（嵌入）优化的数据库

**English**: A database optimized for storing and searching high-dimensional vectors (embeddings)

**提示**: Vector DB = store and search embeddings. '向量数据库'. Tools: Pinecone, Milvus, Weaviate, ChromaDB. Key for RAG.

**示例**: "用向量数据库做语义搜索" → 将文本向量化后存入专用数据库，支持基于语义相似度的搜索

---

### Semantic Search
**中文**: 基于含义而非精确关键词匹配的搜索，使用嵌入和相似度

**English**: Search based on meaning rather than exact keyword matching, using embeddings and similarity

**提示**: Semantic Search = search by meaning, not keywords. '语义搜索'. Uses embeddings + cosine similarity. Better than keyword search for intent.

**示例**: "用语义搜索替代关键词搜索" → 基于语义相似度搜索，而不是精确匹配关键词

---

### Chain of Thought
**中文**: 要求模型在给出最终答案前逐步展示推理过程的提示技术

**English**: A prompting technique that asks the model to show its reasoning step by step before giving a final answer

**提示**: Chain of Thought = ask model to reason step by step. '思维链'. 'Let's think step by step'. Improves math/logic tasks.

**示例**: "用 CoT 提示让模型逐步推理" → 在提示词中要求模型'一步一步想'，提高复杂推理的准确率

---

### Guardrails
**中文**: 约束 LLM 输出以防止有害、不正确或偏离主题回复的安全机制

**English**: Safety mechanisms that constrain LLM outputs to prevent harmful, incorrect, or off-topic responses

**提示**: Guardrails = safety constraints on LLM output. '安全护栏'. Prevent: harmful content, off-topic, hallucination. Implement via prompt, fine-tuning, or tools.

**示例**: "加一些 guardrails 防止模型乱说" → 设置安全约束，限制模型的输出范围和行为

---

### Agent
**中文**: 能自主使用工具、做决策和执行操作来完成任务的 AI 系统

**English**: An AI system that can autonomously use tools, make decisions, and take actions to accomplish tasks

**提示**: Agent = autonomous AI that uses tools and makes decisions. '智能体'. Loop: observe → think → act → observe. Not just chat.

**示例**: "这个 agent 可以自己写代码并运行" → AI 智能体能自主编写代码、执行并调试

---

### Tool Use
**中文**: LLM 调用外部工具（API、计算器、数据库）以增强自身能力的特性

**English**: The ability of an LLM to invoke external tools (APIs, calculators, databases) to augment its capabilities

**提示**: Tool Use = LLM calling external tools. '工具调用'. Extends capabilities beyond text. Examples: search, code execution, API calls.

**示例**: "让模型调用搜索工具" → 给 LLM 提供搜索 API，让它能获取实时信息

---

### Zero-shot
**中文**: 在提示词中不提供任何示例就让模型执行任务

**English**: Asking a model to perform a task without providing any examples in the prompt

**提示**: Zero-shot = no examples in prompt. '零样本'. Simpler prompt, relies on model's pre-training. Use when task is straightforward.

**示例**: "zero-shot 试试看" → 不给例子，直接让模型完成任务，看效果如何

---

### Top-p
**中文**: 将 token 选择限制在累积概率超过 p 的最小集合中的采样参数

**English**: A sampling parameter that limits token selection to the smallest set whose cumulative probability exceeds p

**提示**: Top-p = nucleus sampling. '核采样'. 0.9 = consider top 90% probability mass. Often used with temperature.

**示例**: "top-p 设成 0.9" → 只从累积概率前 90% 的 token 中采样

---

### Max Tokens
**中文**: 模型在响应中生成的最大 token 数量

**English**: The maximum number of tokens the model will generate in its response

**提示**: Max Tokens = output length limit. '最大 token 数'. Separate from context window. Set based on expected output length.

**示例**: "max tokens 设大一点" → 增加输出长度限制，让模型生成更长的回答

---

### Stop Sequence
**中文**: 告诉模型停止生成更多 token 的特定字符串

**English**: A specific string that tells the model to stop generating further tokens

**提示**: Stop Sequence = string that halts generation. '停止序列'. Useful for structured output: stop at '```' after code block.

**示例**: "加个 stop sequence" → 设置一个终止字符串，让模型在输出到特定标记时停止

---

### Context
**中文**: 提供给模型以帮助其理解和适当回复的背景信息

**English**: The background information provided to the model to help it understand and respond appropriately

**提示**: Context = background info for the model. '上下文'. More relevant context = better output. RAG provides dynamic context.

**示例**: "给模型更多上下文" → 提供更多的背景信息帮助模型理解任务

---

### Instruction Tuning
**中文**: 用指令-响应对微调模型以提高其遵循指令的能力

**English**: Fine-tuning a model on instruction-response pairs to improve its ability to follow instructions

**提示**: Instruction Tuning = fine-tune on instruction-response pairs. '指令微调'. Makes models follow instructions better. Foundation of ChatGPT-like models.

**示例**: "经过指令微调的模型更听话" → 模型通过指令微调后更能理解和执行用户的指令

---

### RLHF
**中文**: 使用人类偏好作为奖励信号来对齐模型行为的训练技术

**English**: Training technique where human preferences are used as reward signals to align model behavior

**提示**: RLHF = train with human preferences. '人类反馈强化学习'. Humans rank outputs → reward model → optimize. Key to ChatGPT's quality.

**示例**: "用 RLHF 让模型更安全" → 通过人类反馈训练，让模型的输出更符合人类价值观

---

### Alignment
**中文**: 确保 AI 系统的行为符合人类价值观和意图

**English**: Ensuring AI systems behave in accordance with human values and intentions

**提示**: Alignment = make AI follow human values. '对齐'. Technical challenge: reward hacking, specification gaming. Key research area.

**示例**: "对齐是一个重要问题" → 如何让 AI 的行为真正符合人类的意图，而不是只在表面上看起来正确

---

### Multimodal
**中文**: 能处理和生成多种数据类型（文本、图像、音频、视频）的 AI 模型

**English**: AI models that can process and generate multiple types of data (text, images, audio, video)

**提示**: Multimodal = handles multiple data types. '多模态'. Text + image + audio. Examples: GPT-4V, Claude 3, Gemini.

**示例**: "这个模型是多模态的" → 模型不仅能处理文本，还能理解图片、音频等

---

### Token Limit
**中文**: 模型在单次请求中能处理的最大 token 总数（输入 + 输出）

**English**: The maximum total number of tokens (input + output) a model can handle in a single request

**提示**: Token Limit = max input + output tokens. 'token 限制'. Input tokens + max output tokens ≤ model limit. Plan accordingly.

**示例**: "超过 token limit 了" → 输入和期望输出的总 token 数超出了模型限制

---

### Latency (AI)
**中文**: 从发送请求到收到模型第一个响应 token 之间的时间延迟

**English**: The time delay between sending a request to an AI model and receiving the first token of the response

**提示**: AI Latency = time to first token (TTFT). '推理延迟'. Different from throughput. Streaming reduces perceived latency.

**示例**: "首 token 延迟太高了" → 模型开始响应的时间太长，用户体验差

---

### Streaming
**中文**: 逐个 token 生成并返回 AI 响应，而不是等待完整响应

**English**: Delivering AI responses token by token as they're generated, rather than waiting for the complete response

**提示**: Streaming = deliver tokens as generated. '流式输出'. Reduces perceived latency. Users see response forming in real-time.

**示例**: "用流式输出" → 逐字显示 AI 的回复，而不是等全部生成完再显示

