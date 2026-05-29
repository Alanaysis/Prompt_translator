# 软件工程术语库 / Software Engineering Glossary

> 机器可读数据：[terms.json](./terms.json)

## 术语索引

| 术语 | 中文别名 | 一句话解释 |
|------|----------|-----------|
| [CI/CD](#cicd) | 流水线、持续集成、持续部署 | 代码提交后自动构建、测试、部署 |
| [Refactoring](#refactoring) | 重构 | 不改功能的前提下优化代码结构 |
| [Technical Debt](#technical-debt) | 技术债 | 现在图省事，以后要还的债 |
| [Code Review](#code-review) | 代码审查、审代码 | 同事检查你的代码 |
| [API](#api) | 接口 | 程序之间对话的规则 |
| [Microservices](#microservices) | 微服务 | 把大应用拆成一堆小服务 |
| [Monolith](#monolith) | 单体应用 | 所有功能打包在一起的应用 |
| [Scalability](#scalability) | 可扩展性、伸缩性 | 加资源能不能扛住更大流量 |
| [Latency](#latency) | 延迟、响应时间 | 请求到响应要多久 |
| [Throughput](#throughput) | 吞吐量、QPS | 每秒能处理多少请求 |
| [Caching](#caching) | 缓存 | 把常用数据放近一点，取快一点 |
| [Middleware](#middleware) | 中间件 | 请求和响应之间的处理层 |
| [ORM](#orm) | 对象关系映射 | 用代码操作数据库，不用写 SQL |
| [Containerization](#containerization) | 容器化 | 打包应用+依赖，到处能跑 |
| [Idempotent](#idempotent) | 幂等 | 做一次和做多次结果一样 |
| [Decoupling](#decoupling) | 解耦 | 减少组件之间的依赖 |
| [Hotfix](#hotfix) | 热修复、紧急修复 | 线上出问题，紧急修一下 |
| [Rollback](#rollback) | 回滚 | 新版有问题，退回旧版 |
| [Scaffold](#scaffold) | 脚手架 | 自动生成项目初始结构 |
| [Dependency Injection](#dependency-injection) | 依赖注入 | 外部给依赖，不要自己创建 |
| [Race Condition](#race-condition) | 竞态条件 | 并发时序导致的 bug |
| [Convention over Configuration](#convention-over-configuration) | 约定优于配置 | 有默认值就不用写配置 |
| [Separation of Concerns](#separation-of-concerns) | 关注点分离 | 各管各的事 |
| [Side Effect](#side-effect) | 副作用 | 函数除了返回值还改了别的 |
| [Boilerplate](#boilerplate) | 模板代码 | 到处复制粘贴的重复代码 |
| [Greenfield](#greenfield) | 绿地项目、从零开始 | 全新项目，没有历史包袱 |
| [Feature Flag](#feature-flag) | 功能开关 | 运行时开关控制功能上线 |
| [Observability](#observability) | 可观测性 | 从外部输出推断内部状态 |
| [SLA](#sla) | 服务等级协议 | 服务可用性的承诺 |
| [E2E Testing](#e2e-testing) | 端到端测试 | 模拟真实用户走完整流程 |
| [Caching Strategy](#caching-strategy) | 缓存策略 | 怎么管缓存：存、失效、更新 |

---

## 详细条目

### CI/CD
**中文**: 持续集成/持续部署，俗称"流水线"

**是什么**: 代码提交后自动跑构建、测试、部署的流程。省得每次手动操作。

**场景**:
- "CI/CD 挂了" = 自动化流水线某个步骤失败了
- "跑一下 CI" = 提交代码后等自动化测试结果

**关联**: [Pipeline](#cicd) · [Deployment](#rollback) · [E2E Testing](#e2e-testing)

---

### Refactoring
**中文**: 重构

**是什么**: 在不改变功能的前提下，重新组织代码让它更干净。就像整理房间——东西没变，但找起来更方便了。

**场景**:
- "这段代码需要重构" = 代码能跑但太乱，需要整理
- "重构不是重写" = 重构是渐进式优化，不是推翻重来

**关联**: [Technical Debt](#technical-debt) · [Code Review](#code-review)

---

### Technical Debt
**中文**: 技术债

**是什么**: 为了赶进度而做的技术妥协。就像借钱——现在方便了，但以后要还（而且有利息）。

**场景**:
- "先快速实现，技术债以后再还" = 先上线再说，代码质量以后再补
- "技术债太多了" = 历史妥协太多，开发越来越慢

**关联**: [Refactoring](#refactoring) · [Code Review](#code-review)

---

### Code Review
**中文**: 代码审查，简称 CR

**是什么**: 提交代码前让同事检查一遍。双人舞——一个人写，一个人看。

**场景**:
- "帮我 review 一下" = 请检查我的代码有没有问题
- "CR 过了" = 代码审查通过，可以合并了

**关联**: [CI/CD](#cicd) · [Refactoring](#refactoring)

---

### API
**中文**: 接口

**是什么**: 程序之间对话的规则。就像餐厅菜单——你点菜（请求），厨房做菜（处理），服务员上菜（响应）。

**场景**:
- "对接一下第三方 API" = 调用别人的接口
- "这个 API 返回什么？" = 这个接口的响应格式是什么

**关联**: [Middleware](#middleware) · [ORM](#orm)

---

### Microservices
**中文**: 微服务

**是什么**: 把一个大应用拆成很多小服务，每个服务独立运行。就像把一个大公司拆成多个小团队。

**场景**:
- "我们要拆微服务" = 把单体应用拆分成独立的小服务
- "服务间通信" = 微服务之间怎么互相调用

**关联**: [Monolith](#monolith) · [API](#api) · [Decoupling](#decoupling)

---

### Monolith
**中文**: 单体应用

**是什么**: 所有功能打包在一起的应用。简单粗暴，但规模大了会很笨重。

**场景**:
- "现在是个单体" = 所有代码在一个项目里
- "单体不可怕，烂代码才可怕" = 架构不是问题，代码质量才是

**关联**: [Microservices](#microservices)

---

### Scalability
**中文**: 可扩展性、伸缩性

**是什么**: 系统扛得住更大流量的能力。水平扩展加机器，垂直扩展升级硬件。

**场景**:
- "这个架构能 scale 吗？" = 流量增长时加资源能不能解决
- "scale out" = 加机器（水平扩展）
- "scale up" = 升级硬件（垂直扩展）

**关联**: [Latency](#latency) · [Throughput](#throughput)

---

### Latency
**中文**: 延迟、响应时间

**是什么**: 从请求到响应要多久。低延迟 = 快，高延迟 = 慢。

**场景**:
- "延迟太高了" = 响应太慢
- "p99 延迟 200ms" = 99% 的请求在 200ms 内返回

**关联**: [Throughput](#throughput) · [Caching](#caching)

---

### Throughput
**中文**: 吞吐量，常用 QPS/TPS/RPS

**是什么**: 每秒能处理多少请求。高吞吐 = 能同时服务更多人。

**场景**:
- "QPS 能到多少？" = 每秒能处理多少次请求
- "先优化吞吐量" = 提升系统处理能力

**关联**: [Latency](#latency) · [Scalability](#scalability)

---

### Caching
**中文**: 缓存

**是什么**: 把常用数据放在更快的地方。就像把常用工具放在桌上而不是柜子里。

**场景**:
- "加个缓存吧" = 在数据访问路径上加一层快速存储
- "缓存失效了" = 缓存过期，需要重新获取数据
- "缓存穿透" = 查不存在的数据，每次都打到数据库

**关联**: [Latency](#latency) · [Caching Strategy](#caching-strategy)

---

### Middleware
**中文**: 中间件

**是什么**: 请求和响应之间的处理层。就像安检——每个人都要过，但不影响最终目的地。

**场景**:
- "在 middleware 里加个日志" = 在请求处理的中间层记录日志
- "中间件顺序很重要" = 执行顺序影响结果

**关联**: [API](#api)

---

### ORM
**中文**: 对象关系映射

**是什么**: 用代码操作数据库，不用直接写 SQL。翻译官——把代码翻译成数据库能懂的语言。

**场景**:
- "用 ORM 还是直接写 SQL？" = 选择便捷性还是灵活性
- "N+1 问题" = ORM 常见的性能陷阱

**关联**: [API](#api)

---

### Containerization
**中文**: 容器化

**是什么**: 把应用和依赖打包成容器，保证在任何环境都能跑。集装箱——标准化运输。

**场景**:
- "容器化部署" = 用 Docker 打包部署
- "编排" = 用 Kubernetes 管理多个容器

**关联**: [CI/CD](#cicd)

---

### Idempotent
**中文**: 幂等

**是什么**: 做一次和做多次结果一样。重要的安全网——网络超时重试不会重复扣款。

**场景**:
- "这个接口要保证幂等" = 重复调用不能有副作用
- "支付接口必须幂等" = 不能重复扣钱

**关联**: [API](#api)

---

### Decoupling
**中文**: 解耦

**是什么**: 减少组件之间的依赖。松耦合 = 改一个不影响另一个。

**场景**:
- "这两个模块耦合太紧了" = 改一个必须改另一个
- "通过消息队列解耦" = 用异步通信减少直接依赖

**关联**: [Microservices](#microservices)

---

### Hotfix
**中文**: 热修复、紧急修复

**是什么**: 线上出了严重问题，跳过正常流程紧急修复。消防员——紧急出动。

**场景**:
- "线上出 bug 了，赶紧 hotfix" = 生产环境有严重问题
- "先 hotfix 再复盘" = 先解决问题再分析原因

**关联**: [Rollback](#rollback) · [CI/CD](#cicd)

---

### Rollback
**中文**: 回滚

**是什么**: 新版本有问题，退回旧版本。时间倒流——回到上一个正常的状态。

**场景**:
- "先回滚" = 恢复到上一个稳定版本
- "回滚到上一个 commit" = 代码层面的版本回退

**关联**: [Hotfix](#hotfix) · [CI/CD](#cicd)

---

### Scaffold
**中文**: 脚手架

**是什么**: 自动生成项目初始结构。毛坯房——先把框架搭好，再慢慢装修。

**场景**:
- "用脚手架创建项目" = 用 CLI 工具生成项目模板
- "create-react-app 就是脚手架" = React 项目初始化工具

**关联**: [Boilerplate](#boilerplate)

---

### Dependency Injection
**中文**: 依赖注入，简称 DI

**是什么**: 不要自己创建依赖，让外部给你。点外卖——不需要自己开餐厅。

**场景**:
- "用依赖注入来解耦" = 通过外部注入减少组件间依赖
- "IoC 容器" = 管理依赖注入的工具

**关联**: [Decoupling](#decoupling)

---

### Race Condition
**中文**: 竞态条件

**是什么**: 并发执行时因为时序问题导致的 bug。两个人同时抢一个车位。

**场景**:
- "这里有竞态问题" = 并发时序导致数据不一致
- "用锁解决竞态" = 用 mutex/lock 保证同时只有一个操作

**关联**: [Idempotent](#idempotent)

---

### Convention over Configuration
**中文**: 约定优于配置

**是什么**: 有合理的默认值就不用写配置。交通规则——默认靠右行驶，不需要每个路口都标。

**场景**:
- "Spring Boot 就是约定优于配置" = 框架提供默认约定
- "约定大于配置" = 同义表达

**关联**: [Scaffold](#scaffold)

---

### Separation of Concerns
**中文**: 关注点分离

**是什么**: 各管各的事，不要什么都混在一起。分工合作——前端管展示，后端管逻辑。

**场景**:
- "关注点分离" = 不同功能由不同模块负责
- "MVC 就是关注点分离" = Model/View/Controller 各司其职

**关联**: [Decoupling](#decoupling)

---

### Side Effect
**中文**: 副作用

**是什么**: 函数除了返回值，还改了别的东西。不纯的函数——偷偷改了全局变量。

**场景**:
- "这个函数有副作用" = 函数修改了外部状态
- "纯函数没有副作用" = 相同输入永远相同输出

**关联**: [Idempotent](#idempotent)

---

### Boilerplate
**中文**: 模板代码、样板代码

**是什么**: 到处复制粘贴的重复代码。每个项目都要写的"八股文"。

**场景**:
- "太多 boilerplate 了" = 有大量重复代码
- "用框架减少 boilerplate" = 框架帮你处理重复部分

**关联**: [Scaffold](#scaffold) · [Convention over Configuration](#convention-over-configuration)

---

### Greenfield
**中文**: 绿地项目、从零开始

**是什么**: 全新项目，没有历史包袱。白纸上画画。

**场景**:
- "这是个绿地项目" = 从零开始，可以自由选择技术栈
- "绿地项目机会难得" = 不用处理遗留代码

**关联**: [Monolith](#monolith)（反义）

---

### Feature Flag
**中文**: 功能开关

**是什么**: 运行时控制功能是否启用的开关。不用重新部署就能开关功能。

**场景**:
- "用 feature flag 控制灰度" = 逐步向用户开放新功能
- "这个功能先 flag 关掉" = 功能有问题，先关掉

**关联**: [CI/CD](#cicd)

---

### Observability
**中文**: 可观测性

**是什么**: 从外部输出（日志、指标、追踪）推断系统内部状态。体检报告——通过指标了解身体状况。

**场景**:
- "可观测性不够" = 缺少足够的日志和监控
- "三大支柱：logs, metrics, traces" = 可观测性的三个维度

**关联**: [Latency](#latency) · [SLA](#sla)

---

### SLA
**中文**: 服务等级协议

**是什么**: 对服务可用性的承诺。合同——承诺 99.9% 的时间是可用的。

**场景**:
- "SLA 是 99.9%" = 年停机时间约 8.76 小时
- "三个九、四个九" = 99.9%、99.99%

**关联**: [Observability](#observability)

---

### E2E Testing
**中文**: 端到端测试

**是什么**: 模拟真实用户走完整流程的测试。像用户一样操作——从打开应用到完成任务。

**场景**:
- "加个 E2E 测试" = 写端到端测试覆盖核心流程
- "E2E 挂了" = 端到端测试发现功能有问题

**关联**: [CI/CD](#cicd)

---

### Caching Strategy
**中文**: 缓存策略

**是什么**: 怎么管理缓存：什么时候存、什么时候失效、什么时候更新。

**场景**:
- "用 Cache Aside 模式" = 应用先查缓存，没有再查数据库
- "缓存雪崩" = 大量缓存同时失效，请求全打到数据库

**关联**: [Caching](#caching)
