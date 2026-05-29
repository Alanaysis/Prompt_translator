# 产品术语库 / Product Glossary

> 机器可读数据：[terms.json](./terms.json)

## 术语索引

| 术语 | 中文别名 | 一句话解释 |
|------|----------|-----------|
| [MVP](#mvp) | 最小可行产品 | 最简单的版本，用来验证用户要不要 |
| [PMF](#pmf) | 产品市场契合 | 产品终于对上了市场需求 |
| [User Story](#user-story) | 用户故事 | 用用户视角描述需求 |
| [Scoping](#scoping) | 范围界定 | 这次到底要做哪些 |
| [Stakeholder](#stakeholder) | 利益相关者、干系人 | 跟项目有关的所有人 |
| [AB Testing](#ab-testing) | A/B测试 | 两个版本比一比 |
| [Conversion Rate](#conversion-rate) | 转化率 | 来的人有多少真的用了 |
| [Pain Point](#pain-point) | 痛点 | 用户最头疼的事 |
| [Value Proposition](#value-proposition) | 价值主张 | 用户为什么要选你 |
| [Funnel](#funnel) | 漏斗 | 用户从知道到用上，每一步都在流失 |
| [Growth Hacking](#growth-hacking) | 增长黑客 | 用创意和数据搞增长 |
| [Retention](#retention) | 留存 | 用户还会不会回来 |
| [Churn](#churn) | 流存 | 用户走了多少 |
| [Backlog](#backlog) | 待办列表、需求池 | 要做的事排排坐 |
| [Prioritization](#prioritization) | 优先级排序 | 先做哪个后做哪个 |

---

## 详细条目

### MVP
**中文**: 最小可行产品，Minimum Viable Product

**是什么**: 产品最简单的版本，刚好能验证核心假设。不是原型（prototype）——MVP 是给真实用户用的。

**场景**:
- "先做 MVP 验证一下" = 先做最简单的版本看看用户要不要
- "MVP 不是半成品" = 虽然简单，但核心体验要完整

**关联**: [PMF](#pmf) · [Scoping](#scoping)

---

### PMF
**中文**: 产品市场契合，Product-Market Fit

**是什么**: 产品终于对上了市场需求。感觉就是：用户主动来用，还推荐给别人。

**场景**:
- "还没找到 PMF" = 产品还没有足够多的忠实用户
- "找到 PMF 之后就可以 scale 了" = 验证了市场需求，可以加速增长

**关联**: [MVP](#mvp) · [Pain Point](#pain-point)

---

### User Story
**中文**: 用户故事

**是什么**: 用用户视角描述需求的格式。"作为XX，我想要YY，以便ZZ"。

**场景**:
- "写个用户故事" = 用标准格式描述需求
- "这个用户故事的验收标准是什么？" = 怎么判断做完了

**关联**: [Backlog](#backlog) · [Scoping](#scoping)

---

### Scoping
**中文**: 范围界定

**是什么**: 定义这次到底要做哪些、不做哪些。边界感——知道什么在范围内，什么不是。

**场景**:
- "先 scope 一下" = 先确定范围
- "scope creep 了" = 范围不知不觉扩大了

**关联**: [MVP](#mvp) · [Backlog](#backlog)

---

### Stakeholder
**中文**: 利益相关者、干系人

**是什么**: 跟项目有关的所有人：用户、老板、投资人、团队成员。

**场景**:
- "对齐一下 stakeholder" = 跟所有相关方确认目标一致
- "stakeholder 管理" = 管理各方期望

**关联**: [User Story](#user-story)

---

### AB Testing
**中文**: A/B测试、分流测试

**是什么**: 同时上线两个版本，用数据决定哪个更好。不靠直觉，靠数据。

**场景**:
- "做个 AB 测试" = 对比两个方案哪个效果好
- "A 方案赢了" = 数据显示 A 方案转化率更高

**关联**: [Conversion Rate](#conversion-rate) · [Feature Flag](../software-engineering/README.md#feature-flag)

---

### Conversion Rate
**中文**: 转化率

**是什么**: 来访问的人中，有多少真的做了你希望他们做的事（注册、购买等）。

**场景**:
- "转化率太低了" = 来的人多，但真正行动的人少
- "优化转化率" = 让更多访客变成用户

**关联**: [Funnel](#funnel) · [AB Testing](#ab-testing)

---

### Pain Point
**中文**: 痛点

**是什么**: 用户最头疼、最不方便的地方。痛点 = 产品机会。

**场景**:
- "用户痛点是什么？" = 用户在什么情况下最痛苦
- "解决痛点" = 产品存在的理由

**关联**: [Value Proposition](#value-proposition) · [PMF](#pmf)

---

### Value Proposition
**中文**: 价值主张

**是什么**: 用户为什么要选你而不是别人。你的独特价值是什么。

**场景**:
- "我们的价值主张是什么？" = 我们能提供什么独特价值
- "价值主张要清晰" = 一句话说清楚你能帮用户解决什么问题

**关联**: [Pain Point](#pain-point)

---

### Funnel
**中文**: 漏斗、转化漏斗

**是什么**: 用户从知道产品到最终使用的每一步，每一步都有人流失。像漏斗一样，上面宽下面窄。

**场景**:
- "看看漏斗哪一步流失最多" = 找到转化流程中的瓶颈
- "优化漏斗" = 减少每一步的流失

**关联**: [Conversion Rate](#conversion-rate) · [Retention](#retention)

---

### Growth Hacking
**中文**: 增长黑客

**是什么**: 用创意和数据驱动的方法快速增长用户。不靠砸钱，靠聪明。

**场景**:
- "需要增长黑客的手段" = 需要低成本高效果的增长策略
- "病毒式传播" = growth hacking 的经典手段

**关联**: [Retention](#retention) · [Conversion Rate](#conversion-rate)

---

### Retention
**中文**: 留存、留存率

**是什么**: 用户会不会回来继续用。留存高 = 用户觉得有价值。

**场景**:
- "次日留存多少？" = 第一天用完，第二天还有多少人回来
- "留存是最重要的指标" = 留不住用户，增长也没用

**关联**: [Churn](#churn) · [Funnel](#funnel)

---

### Churn
**中文**: 流失、流失率

**是什么**: 用户停止使用的比例。留存的反面。

**场景**:
- "churn 太高了" = 流失的用户太多
- "降低 churn" = 让更多用户留下来

**关联**: [Retention](#retention) · [Pain Point](#pain-point)

---

### Backlog
**中文**: 待办列表、需求池

**是什么**: 所有待做的功能、bug、任务的列表。按优先级排序。

**场景**:
- "加到 backlog 里" = 先记下来，以后再排
- "清理 backlog" = 处理积压的需求

**关联**: [Prioritization](#prioritization) · [User Story](#user-story)

---

### Prioritization
**中文**: 优先级排序

**是什么**: 决定先做哪个后做哪个。资源有限，要做最有价值的事。

**场景**:
- "排一下优先级" = 评估各需求的重要程度
- "用 RICE 模型" = 用 Reach×Impact×Confidence÷Effort 来量化优先级

**关联**: [Backlog](#backlog) · [Scoping](#scoping)
