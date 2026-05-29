# 软件工程术语库 / Software Engineering Glossary

> 涵盖前后端、架构、DevOps、安全、数据库、测试等软件工程领域的核心术语。
>
> 机器可读数据：[terms.json](./terms.json) | 共 82 个术语

## 术语索引

| 术语 | 别名 | 一句话解释 |
|------|------|-----------|
| [CI/CD](#cicd) | 持续集成, 持续部署, Continuous Integration | 将代码变更频繁集成到共享仓库的实践，通过自动化构建、测试和部署来快速交付软件 |
| [Refactoring](#refactoring) | 重构, 代码重构, Refactor | 在不改变代码外部行为的前提下，重新组织代码结构以提高可读性、降低复杂度或提升可维护性 |
| [Technical Debt](#technical-debt) | 技术债, 技术债务, Tech Debt | 由于当前选择了简单/快速的方案而非更优但耗时更长的方案，而导致未来需要额外返工的隐性成本 |
| [Code Review](#code-review) | 代码审查, CR, Review | 由团队成员系统性地检查源代码，以发现缺陷、确保质量和分享知识 |
| [API](#api) | 接口, API接口, Application Programming Interface | 一组规则和协议，允许不同的软件组件之间相互通信 |
| [Microservices](#microservices) | 微服务, 微服务架构, Microservice Architecture | 一种架构风格，将应用拆分为多个小型、可独立部署的服务，通过网络通信协作 |
| [Monolith](#monolith) | 单体应用, 单体架构, Monolithic Architecture | 将所有组件紧密耦合在一起、作为一个整体统一部署的应用架构 |
| [Scalability](#scalability) | 可扩展性, 扩展性, 伸缩性 | 系统通过增加资源来应对更大负载的能力（水平扩展：加机器，垂直扩展：升级硬件） |
| [Latency](#latency) | 延迟, 响应时间, 响应延迟 | 从发起请求到收到响应之间的时间延迟，通常以毫秒为单位 |
| [Throughput](#throughput) | 吞吐量, QPS, TPS | 系统在单位时间内能处理的请求数量或操作数量 |
| [Caching](#caching) | 缓存, Cache, 缓存策略 | 将频繁访问的数据存储在更快的存储层中，以减少访问时间和后端负载 |
| [Middleware](#middleware) | 中间件, 拦截器, Interceptor | 位于操作系统/数据库和应用之间的软件，提供消息传递、身份验证、日志记录等通用服务 |
| [ORM](#orm) | 对象关系映射, Object-Relational Mapping | 在面向对象编程语言和关系型数据库之间进行数据类型转换的技术 |
| [Containerization](#containerization) | 容器化, Container, 容器 | 将应用及其依赖打包成标准化单元（容器），以实现跨环境的一致部署 |
| [Idempotent](#idempotent) | 幂等, 幂等性 | 执行一次和执行多次产生相同结果的操作特性 |
| [Decoupling](#decoupling) | 解耦, 松耦合, Loose Coupling | 减少组件之间的依赖关系，使其可以独立变更、部署或扩展 |
| [Hotfix](#hotfix) | 热修复, 紧急修复, 补丁 | 跳过正常发布流程，紧急部署到生产环境以解决严重问题的代码修复 |
| [Rollback](#rollback) | 回滚, 回退, 版本回退 | 将系统或部署恢复到之前已知正常的状态 |
| [Scaffold](#scaffold) | 脚手架, 项目脚手架, Boilerplate | 预配置的项目结构和模板代码，用于快速启动开发 |
| [Dependency Injection](#dependency-injection) | 依赖注入, DI, IoC | 对象从外部接收其依赖项，而不是在内部自行创建的技术 |
| [Race Condition](#race-condition) | 竞态条件, 竞态, 并发竞争 | 系统行为取决于事件的相对时序，导致不可预测结果的缺陷 |
| [Convention over Configuration](#convention-over-configuration) | 约定优于配置, 约定大于配置, CoC | 提供合理默认值的设计范式，开发者只需指定非常规的部分 |
| [Separation of Concerns](#separation-of-concerns) | 关注点分离, SoC | 将程序划分为不同部分，每个部分处理独立关注点的原则 |
| [Side Effect](#side-effect) | 副作用, Side Effect | 函数调用之外可观察到的任何变化（修改外部状态、I/O 操作等） |
| [Boilerplate](#boilerplate) | 模板代码, 样板代码, 重复代码 | 在项目间或项目内几乎不加修改就重复使用的代码 |
| [Greenfield](#greenfield) | 绿地项目, 全新项目, 从零开始 | 从零开始的项目，没有现有代码库或之前工作的约束 |
| [Feature Flag](#feature-flag) | 功能开关, 特性开关, Feature Toggle | 在运行时启用或禁用功能的机制，无需部署新代码 |
| [Observability](#observability) | 可观测性, 可观测, Telemetry | 通过系统的外部输出（日志、指标、链路追踪）来理解系统内部状态的能力 |
| [SLA](#sla) | 服务等级协议, Service Level Agreement | 服务提供者和客户之间关于预期服务水平的承诺（正常运行时间、响应时间等） |
| [E2E Testing](#e2e-testing) | 端到端测试, End-to-End Testing, E2E | 从头到尾测试整个应用流程，模拟真实用户场景 |
| [Caching Strategy](#caching-strategy) | 缓存策略, Cache Aside, Read Through | 关于何时以及如何填充、失效和更新缓存数据的方法 |
| [Singleton](#singleton) | 单例模式, 单例 | 确保一个类只有一个实例，并提供全局访问点的设计模式 |
| [Factory Pattern](#factory-pattern) | 工厂模式, 工厂方法, Factory Method | 不指定具体类就能创建对象的设计模式 |
| [Observer Pattern](#observer-pattern) | 观察者模式, 发布订阅, Pub/Sub | 对象（主题）维护依赖列表（观察者），状态变化时自动通知它们 |
| [Database Index](#database-index) | 索引, 数据库索引, DB Index | 提高数据库查询速度的数据结构，代价是额外的存储空间和写入开销 |
| [Database Migration](#database-migration) | 数据库迁移, Migration, DB Migration | 对数据库结构的版本化变更（添加表、列、修改结构） |
| [Sharding](#sharding) | 分片, 分库分表, 水平拆分 | 将数据分散到多个数据库实例以提高可扩展性和性能 |
| [Replication](#replication) | 复制, 主从复制, 读写分离 | 将数据从一个数据库服务器复制到一个或多个其他服务器，用于冗余和读扩展 |
| [ACID](#acid) | 事务特性, ACID 特性 | 保证数据库事务可靠性的四个特性：原子性、一致性、隔离性、持久性 |
| [Authentication](#authentication) | 认证, 身份验证, 鉴权 | 验证用户或系统身份的过程 |
| [Authorization](#authorization) | 授权, 权限控制, 权限校验 | 确定已认证用户可以执行哪些操作的过程 |
| [JWT](#jwt) | JSON Web Token, 令牌, Token | 一种紧凑、URL 安全的令牌格式，用于在各方之间安全传输 JSON 对象信息 |
| [OAuth](#oauth) | OAuth2, 第三方登录, 社交登录 | 基于令牌的认证和授权开放标准，常用于第三方登录 |
| [Load Balancer](#load-balancer) | 负载均衡, 负载均衡器, LB | 将网络流量分配到多台服务器的设备或软件 |
| [CDN](#cdn) | 内容分发网络, Content Delivery Network, 加速 | 地理分布的服务器网络，从最近的位置向用户分发内容 |
| [Serverless](#serverless) | 无服务器, Serverless 架构, FaaS | 云服务商管理基础设施、你只需按实际执行时间付费的云计算模型 |
| [Unit Test](#unit-test) | 单元测试, 单测 | 单独测试各个函数或方法以验证其正确性 |
| [Integration Test](#integration-test) | 集成测试, 联调测试 | 测试多个组件协同工作的正确性 |
| [Mock](#mock) | 模拟对象, Mock 对象, Stub | 在测试中模拟真实依赖行为的假对象 |
| [TDD](#tdd) | 测试驱动开发, Test-Driven Development | 先写测试再写实现代码的开发方法（红 → 绿 → 重构） |
| [Event-Driven](#event-driven) | 事件驱动, 事件驱动架构, EDA | 组件通过生产和消费事件（而非直接调用）来通信的架构 |
| [Message Queue](#message-queue) | 消息队列, MQ, 消息中间件 | 通过排队消息实现服务间异步通信的系统 |
| [Circuit Breaker](#circuit-breaker) | 熔断, 熔断器, 断路器 | 通过停止调用故障服务并返回降级响应来防止级联失败的模式 |
| [Retry](#retry) | 重试, 自动重试, Retry Policy | 自动重试失败的操作，通常使用指数退避策略 |
| [Git Branch](#git-branch) | 分支, Git 分支, Branch | 版本控制中独立的开发线路 |
| [Merge](#merge) | 合并, Git Merge, 代码合并 | 将一个分支的变更合并到另一个分支 |
| [Rebase](#rebase) | 变基, Git Rebase | 将一个分支的提交重放到另一个分支的基础上，创建线性历史 |
| [Conflict](#conflict) | 冲突, 合并冲突, Merge Conflict | 两个分支修改了同一行代码，Git 无法自动合并 |
| [XSS](#xss) | 跨站脚本, Cross-Site Scripting | 将恶意脚本注入到其他用户查看的网页中的安全漏洞 |
| [CSRF](#csrf) | 跨站请求伪造, Cross-Site Request Forgery | 欺骗用户浏览器向已认证的网站发送非预期请求的攻击方式 |
| [SQL Injection](#sql-injection) | SQL 注入, 注入攻击 | 利用数据库查询构造中的安全漏洞进行代码注入的技术 |
| [N+1 Query](#n+1-query) | N+1 问题, N+1 查询 | 获取 N 条数据需要 N+1 次数据库查询（而非 1-2 次）的性能反模式 |
| [Profiling](#profiling) | 性能分析, 性能剖析, Profile | 分析程序运行时行为以找到性能瓶颈 |
| [Bottleneck](#bottleneck) | 瓶颈, 性能瓶颈 | 系统中限制整体性能或吞吐量的环节 |
| [Open Source](#open-source) | 开源, 开源软件, OSS | 源代码可供任何人检查、修改和增强的软件 |
| [Git Flow](#git-flow) | Git 工作流, 分支策略 | 定义特定分支角色（main、develop、feature、release、hotfix）的分支模型 |
| [Infrastructure as Code](#infrastructure-as-code) | 基础设施即代码, IaC | 通过机器可读的配置文件（而非手动操作）来管理基础设施 |
| [GitOps](#gitops) | Git 运维 | 以 Git 作为基础设施和应用交付唯一事实来源的部署范式 |
| [Blue-Green Deployment](#blue-green-deployment) | 蓝绿部署, 蓝绿发布 | 维护两个相同环境的部署策略；流量从蓝色（当前）切换到绿色（新版） |
| [Canary Release](#canary-release) | 金丝雀发布, 灰度发布, 灰度 | 在全量部署前，先将新版本逐步推送给一小部分用户 |
| [API Gateway](#api-gateway) | API 网关, 网关 | 所有 API 请求的统一入口，处理路由、认证、限流等 |
| [Webhook](#webhook) | 回调, 钩子, 回调通知 | 由一个系统的事件触发的 HTTP 回调，向另一个系统的 URL 发送数据 |
| [gRPC](#grpc) | gRPC 框架 | 使用 Protocol Buffers 序列化和 HTTP/2 传输的高性能 RPC 框架 |
| [GraphQL](#graphql) | GraphQL 查询语言 | 一种 API 查询语言，让客户端精确请求所需的数据 |
| [REST](#rest) | RESTful, REST API, RESTful API | 使用标准 HTTP 方法（GET、POST、PUT、DELETE）和基于资源的 URL 的 API 架构风格 |
| [WebSocket](#websocket) | WebSocket 连接, 长连接, WS | 在单个 TCP 连接上提供全双工通信通道的协议 |
| [Polling](#polling) | 轮询, 定时请求, Short Polling | 通过定期发送 HTTP 请求来反复检查更新 |
| [Dead Letter Queue](#dead-letter-queue) | 死信队列, DLQ | 无法成功处理的消息被发送到的队列，供后续分析 |
| [Rate Limiting](#rate-limiting) | 限流, 频率限制, Rate Limit | 控制客户端在一段时间内可以发送的请求数量 |
| [Graceful Degradation](#graceful-degradation) | 优雅降级, 降级 | 系统在部分组件故障时仍能以降级功能继续运行的能力 |
| [Chaos Engineering](#chaos-engineering) | 混沌工程 | 故意向系统注入故障以测试其韧性并发现弱点 |
| [SRE](#sre) | 站点可靠性工程, Site Reliability Engineering | 将软件工程实践应用于基础设施和运维问题的学科 |

---

## 详细条目

### CI/CD
**中文**: 将代码变更频繁集成到共享仓库的实践，通过自动化构建、测试和部署来快速交付软件

**English**: Practice of frequently integrating code changes into a shared repository, with automated build, test, and deployment

**提示**: CI/CD = automated build-test-deploy pipeline; '流水线' literally means 'assembly line/pipeline'

**示例**: "我们用了 GitHub Actions 做 CI/CD" → 项目使用 GitHub Actions 实现代码提交后自动构建、测试、部署

---

### Refactoring
**中文**: 在不改变代码外部行为的前提下，重新组织代码结构以提高可读性、降低复杂度或提升可维护性

**English**: Restructuring existing code without changing its external behavior, to improve readability, reduce complexity, or improve maintainability

**提示**: Refactoring = restructure code without behavior change. User says '重构' = they want cleaner code, not new features.

**示例**: "这段代码太乱了，需要重构一下" → 代码结构混乱，需要在不改变功能的情况下重新组织

---

### Technical Debt
**中文**: 由于当前选择了简单/快速的方案而非更优但耗时更长的方案，而导致未来需要额外返工的隐性成本

**English**: The implied cost of future reworking caused by choosing an easy/quick solution now instead of a better approach that would take longer

**提示**: Technical debt = shortcuts taken now that will cost more to fix later. Like financial debt, it accumulates 'interest'.

**示例**: "先快速实现，技术债以后再还" → 先用简单方案上线，承认以后需要重构，但现在赶进度

---

### Code Review
**中文**: 由团队成员系统性地检查源代码，以发现缺陷、确保质量和分享知识

**English**: Systematic examination of source code by peers to find bugs, ensure quality, and share knowledge

**提示**: Code review = peer examination of code changes before merging. 'review' as verb = examine the code.

**示例**: "帮我 review 一下这个 PR" → 请检查这个 Pull Request 中的代码变更是否有问题

---

### API
**中文**: 一组规则和协议，允许不同的软件组件之间相互通信

**English**: A set of rules and protocols that allow different software components to communicate with each other

**提示**: API = interface for programmatic access. User says '接口' = they mean API endpoint. '对接API' = integrate/call an external API.

**示例**: "这个服务暴露了哪些 API？" → 这个服务提供了哪些可调用的接口？

---

### Microservices
**中文**: 一种架构风格，将应用拆分为多个小型、可独立部署的服务，通过网络通信协作

**English**: Architectural style where an application is composed of small, independently deployable services that communicate over a network

**提示**: Microservices = many small services vs monolith = one big app. '拆微服务' = decompose into microservices.

**示例**: "我们要拆成微服务" → 要把现有的单体应用拆分成多个独立的小服务

---

### Monolith
**中文**: 将所有组件紧密耦合在一起、作为一个整体统一部署的应用架构

**English**: An application built as a single, unified unit where all components are tightly coupled and deployed together

**提示**: Monolith = single deployable unit, opposite of microservices.

**示例**: "现在是个单体，后面要拆" → 当前是单体架构，计划未来拆分为微服务

---

### Scalability
**中文**: 系统通过增加资源来应对更大负载的能力（水平扩展：加机器，垂直扩展：升级硬件）

**English**: The ability of a system to handle increased load by adding resources (horizontal: more machines, vertical: bigger machines)

**提示**: Scalability = ability to grow with demand. 'scale up' = vertical (bigger machine), 'scale out' = horizontal (more machines).

**示例**: "这个架构能不能 scale？" → 这个架构在用户量/数据量增长时能否通过加资源来应对？

---

### Latency
**中文**: 从发起请求到收到响应之间的时间延迟，通常以毫秒为单位

**English**: The time delay between a request and its response, typically measured in milliseconds

**提示**: Latency = delay/响应时间. '延迟高' = high latency = slow response. Not to be confused with throughput (吞吐量).

**示例**: "接口延迟太高了" → API 响应时间太长，用户需要等很久

---

### Throughput
**中文**: 系统在单位时间内能处理的请求数量或操作数量

**English**: The number of requests or operations a system can handle per unit of time

**提示**: Throughput = requests per second (QPS/TPS/RPS). High throughput ≠ low latency.

**示例**: "QPS 能到多少？" → 每秒能处理多少次查询请求？

---

### Caching
**中文**: 将频繁访问的数据存储在更快的存储层中，以减少访问时间和后端负载

**English**: Storing frequently accessed data in a faster storage layer to reduce access time and backend load

**提示**: Caching = storing data closer to consumer for speed. '加缓存' = add caching layer. Cache invalidation is a hard problem.

**示例**: "加个缓存吧" → 在数据访问路径上增加缓存层来提升性能

---

### Middleware
**中文**: 位于操作系统/数据库和应用之间的软件，提供消息传递、身份验证、日志记录等通用服务

**English**: Software that sits between the operating system/database and applications, providing common services like messaging, authentication, or logging

**提示**: Middleware = software layer between request and response handler. Handles cross-cutting concerns like auth, logging, CORS.

**示例**: "在 middleware 里加个日志" → 在请求处理的中间层添加日志记录逻辑

---

### ORM
**中文**: 在面向对象编程语言和关系型数据库之间进行数据类型转换的技术

**English**: A technique that converts data between incompatible type systems in object-oriented programming languages and relational databases

**提示**: ORM = maps objects to database tables. Common: SQLAlchemy (Python), TypeORM/Prisma (JS), ActiveRecord (Ruby).

**示例**: "用 ORM 还是直接写 SQL？" → 是用 ORM 框架操作数据库还是直接编写 SQL 语句？

---

### Containerization
**中文**: 将应用及其依赖打包成标准化单元（容器），以实现跨环境的一致部署

**English**: Packaging an application and its dependencies into a standardized unit (container) for consistent deployment across environments

**提示**: Containerization = package app + deps into portable container (Docker). '容器化' = containerize. K8s orchestrates containers.

**示例**: "容器化部署" → 将应用打包成 Docker 容器进行部署

---

### Idempotent
**中文**: 执行一次和执行多次产生相同结果的操作特性

**English**: An operation that produces the same result whether it's executed once or multiple times

**提示**: Idempotent = safe to repeat. Critical for payment APIs, retry logic. '幂等' = idempotent.

**示例**: "这个接口要保证幂等" → 重复调用这个接口不能产生副作用（比如重复扣款）

---

### Decoupling
**中文**: 减少组件之间的依赖关系，使其可以独立变更、部署或扩展

**English**: Reducing dependencies between components so they can be changed, deployed, or scaled independently

**提示**: Decoupling = reduce inter-dependencies. '解耦' = decouple. Opposite of '耦合' (coupling).

**示例**: "这两个模块耦合太紧了，需要解耦" → 两个模块之间依赖过深，需要减少相互依赖

---

### Hotfix
**中文**: 跳过正常发布流程，紧急部署到生产环境以解决严重问题的代码修复

**English**: An urgent code fix deployed to production to resolve a critical issue, bypassing the normal release cycle

**提示**: Hotfix = urgent production fix, bypasses normal cycle. '热修复' or '紧急修复'.

**示例**: "线上出 bug 了，赶紧 hotfix" → 生产环境有严重问题，需要紧急修复并部署

---

### Rollback
**中文**: 将系统或部署恢复到之前已知正常的状态

**English**: Reverting a system or deployment to a previous known-good state

**提示**: Rollback = revert to previous version. '回滚' = rollback. Common when deployment breaks things.

**示例**: "新版本有问题，先回滚" → 最新部署有 bug，先恢复到上一个稳定版本

---

### Scaffold
**中文**: 预配置的项目结构和模板代码，用于快速启动开发

**English**: Pre-configured project structure and boilerplate code generated to quickly start development

**提示**: Scaffold/脚手架 = auto-generated project starter. Tools: create-react-app, vue-cli, django-admin startproject.

**示例**: "用 create-react-app 脚手架创建项目" → 使用 CLI 工具快速生成 React 项目的初始结构

---

### Dependency Injection
**中文**: 对象从外部接收其依赖项，而不是在内部自行创建的技术

**English**: A technique where an object receives its dependencies from external sources rather than creating them internally

**提示**: DI = don't create dependencies yourself, receive them from outside. Promotes testability and loose coupling.

**示例**: "用依赖注入来解耦" → 通过外部注入依赖而不是内部创建，来降低组件间的耦合度

---

### Race Condition
**中文**: 系统行为取决于事件的相对时序，导致不可预测结果的缺陷

**English**: A bug where the behavior of a system depends on the relative timing of events, leading to unpredictable results

**提示**: Race condition = timing-dependent bug in concurrent code. '竞态' = race condition. Fix with locks/mutexes/atomic ops.

**示例**: "这里有竞态问题" → 并发执行时存在时序相关的 bug，可能导致数据不一致

---

### Convention over Configuration
**中文**: 提供合理默认值的设计范式，开发者只需指定非常规的部分

**English**: A design paradigm that provides sensible defaults so developers only need to specify unconventional aspects of the application

**提示**: Convention over Configuration = sensible defaults reduce boilerplate config. Key philosophy of Rails, Spring Boot.

**示例**: "Spring Boot 就是约定优于配置" → 框架提供了大量默认约定，减少了显式配置的工作量

---

### Separation of Concerns
**中文**: 将程序划分为不同部分，每个部分处理独立关注点的原则

**English**: The principle of dividing a program into distinct sections, each addressing a separate concern

**提示**: Separation of Concerns = each part of code does one thing. '关注点分离' = SoC. Foundation of MVC, layered architecture.

**示例**: "前端和后端要关注点分离" → 前端负责展示逻辑，后端负责业务逻辑，不要混在一起

---

### Side Effect
**中文**: 函数调用之外可观察到的任何变化（修改外部状态、I/O 操作等）

**English**: Any observable change outside the function being called (modifying external state, I/O, etc.)

**提示**: Side effect = function changes things outside itself. Pure functions have no side effects. '副作用' = side effect.

**示例**: "这个函数有副作用" → 函数除了返回值外，还修改了外部状态（如全局变量、数据库等）

---

### Boilerplate
**中文**: 在项目间或项目内几乎不加修改就重复使用的代码

**English**: Code that is repeated with little or no alteration across projects or within a project

**提示**: Boilerplate = repetitive code you always write. '模板代码'/'样板代码'. Reduce with frameworks, code generation.

**示例**: "太多 boilerplate 了" → 有大量重复的模板代码，应该抽象或用工具生成

---

### Greenfield
**中文**: 从零开始的项目，没有现有代码库或之前工作的约束

**English**: A project started from scratch with no existing codebase or constraints from prior work

**提示**: Greenfield = start from nothing. Brownfield = work within existing system. '绿地'/'从零开始' = greenfield.

**示例**: "这是个绿地项目" → 全新项目，可以从头选择技术栈和架构

---

### Feature Flag
**中文**: 在运行时启用或禁用功能的机制，无需部署新代码

**English**: A mechanism to enable or disable features at runtime without deploying new code

**提示**: Feature flag = runtime on/off switch for features. '功能开关'. Enables gradual rollout, A/B testing.

**示例**: "用 feature flag 控制新功能的灰度" → 通过功能开关逐步向用户开放新功能

---

### Observability
**中文**: 通过系统的外部输出（日志、指标、链路追踪）来理解系统内部状态的能力

**English**: The ability to understand the internal state of a system from its external outputs (logs, metrics, traces)

**提示**: Observability = understand system from outside. Three pillars: logs, metrics, traces. '可观测性'.

**示例**: "服务可观测性不够" → 缺乏足够的日志、指标和追踪来排查问题

---

### SLA
**中文**: 服务提供者和客户之间关于预期服务水平的承诺（正常运行时间、响应时间等）

**English**: A commitment between a service provider and client defining the expected level of service (uptime, response time, etc.)

**提示**: SLA = service level commitment. 99.9% = 'three nines'. SLO is internal target, SLA is external promise.

**示例**: "我们的 SLA 是 99.9%" → 承诺服务年可用性达到 99.9%（约 8.76 小时/年停机）

---

### E2E Testing
**中文**: 从头到尾测试整个应用流程，模拟真实用户场景

**English**: Testing the entire application flow from start to finish, simulating real user scenarios

**提示**: E2E testing = test full user flow from UI to DB. Tools: Cypress, Playwright, Selenium. '端到端测试'.

**示例**: "加个 E2E 测试覆盖核心流程" → 编写端到端测试来验证用户核心操作路径的正确性

---

### Caching Strategy
**中文**: 关于何时以及如何填充、失效和更新缓存数据的方法

**English**: The approach for when and how to populate, invalidate, and update cached data

**提示**: Cache Aside = app manages cache. Read/Write Through = cache manages itself. '缓存策略' = caching strategy.

**示例**: "用 Cache Aside 模式" → 应用先查缓存，没有再查数据库，然后更新缓存

---

### Singleton
**中文**: 确保一个类只有一个实例，并提供全局访问点的设计模式

**English**: A design pattern that ensures a class has only one instance and provides a global point of access to it

**提示**: Singleton = one instance only. '单例'. Use sparingly, often considered an anti-pattern for testability.

**示例**: "数据库连接用单例模式" → 整个应用只维护一个数据库连接实例

---

### Factory Pattern
**中文**: 不指定具体类就能创建对象的设计模式

**English**: A design pattern that creates objects without specifying the exact class to instantiate

**提示**: Factory = create objects without knowing exact class. '工厂模式'. Decouples creation from usage.

**示例**: "用工厂模式创建不同类型的处理器" → 通过工厂统一创建对象，调用方不需要知道具体实现类

---

### Observer Pattern
**中文**: 对象（主题）维护依赖列表（观察者），状态变化时自动通知它们

**English**: A pattern where an object (subject) maintains a list of dependents (observers) and notifies them of state changes

**提示**: Observer = notify dependents on change. '观察者模式'. Also known as Pub/Sub, Event Emitter.

**示例**: "用观察者模式做事件通知" → 当数据变化时，自动通知所有订阅者更新

---

### Database Index
**中文**: 提高数据库查询速度的数据结构，代价是额外的存储空间和写入开销

**English**: A data structure that improves the speed of data retrieval operations on a database table at the cost of additional storage and write overhead

**提示**: Index = speed up reads, slow down writes. '索引'. Like book index - find content by looking up keywords.

**示例**: "给这个字段加个索引" → 在数据库表的某个字段上创建索引以加速查询

---

### Database Migration
**中文**: 对数据库结构的版本化变更（添加表、列、修改结构）

**English**: Version-controlled changes to database schema (adding tables, columns, modifying structure)

**提示**: Migration = version-controlled DB schema change. '数据库迁移'. Tools: Alembic, Flyway, Rails migrations.

**示例**: "跑一下 migration" → 执行数据库结构变更脚本

---

### Sharding
**中文**: 将数据分散到多个数据库实例以提高可扩展性和性能

**English**: Distributing data across multiple database instances to improve scalability and performance

**提示**: Sharding = split data across multiple DBs. '分片'/'分库分表'. Horizontal scaling for data layer.

**示例**: "数据量太大了，需要分片" → 单个数据库扛不住，需要把数据拆分到多个实例

---

### Replication
**中文**: 将数据从一个数据库服务器复制到一个或多个其他服务器，用于冗余和读扩展

**English**: Copying data from one database server to one or more others for redundancy and read scalability

**提示**: Replication = copy data to multiple servers. '复制'/'主从复制'. Primary handles writes, replicas handle reads.

**示例**: "用主从复制做读写分离" → 主库负责写入，从库负责读取，分摊压力

---

### ACID
**中文**: 保证数据库事务可靠性的四个特性：原子性、一致性、隔离性、持久性

**English**: Properties guaranteeing reliable database transactions: Atomicity, Consistency, Isolation, Durability

**提示**: ACID = Atomicity, Consistency, Isolation, Durability. '事务特性'. Guarantees reliable transactions.

**示例**: "这个操作要保证 ACID" → 数据库操作必须满足事务的四个特性

---

### Authentication
**中文**: 验证用户或系统身份的过程

**English**: The process of verifying the identity of a user or system

**提示**: Authentication = verify identity (who are you?). '认证'/'身份验证'. Different from Authorization (what can you do?).

**示例**: "这个接口需要认证" → 调用前必须先验证身份（登录）

---

### Authorization
**中文**: 确定已认证用户可以执行哪些操作的过程

**English**: The process of determining what an authenticated user is allowed to do

**提示**: Authorization = what can you do? '授权'/'权限控制'. Different from Authentication (who are you?). RBAC is common.

**示例**: "管理员才有权限执行这个操作" → 只有 admin 角色的用户才能调用此接口

---

### JWT
**中文**: 一种紧凑、URL 安全的令牌格式，用于在各方之间安全传输 JSON 对象信息

**English**: A compact, URL-safe token format for securely transmitting information between parties as a JSON object

**提示**: JWT = JSON Web Token for auth. '令牌'. Stateless, contains claims, signed not encrypted.

**示例**: "用 JWT 做身份验证" → 用户登录后发放 JWT，后续请求携带此令牌验证身份

---

### OAuth
**中文**: 基于令牌的认证和授权开放标准，常用于第三方登录

**English**: An open standard for token-based authentication and authorization, commonly used for third-party login

**提示**: OAuth = third-party auth standard. '第三方登录'. Common providers: Google, GitHub, WeChat.

**示例**: "接入微信 OAuth 登录" → 支持用户用微信账号登录你的应用

---

### Load Balancer
**中文**: 将网络流量分配到多台服务器的设备或软件

**English**: A device or software that distributes network traffic across multiple servers

**提示**: Load Balancer = distribute traffic across servers. '负载均衡'. Algorithms: round-robin, least-connections, IP hash.

**示例**: "前面加个负载均衡" → 在服务器集群前部署负载均衡器，分发请求

---

### CDN
**中文**: 地理分布的服务器网络，从最近的位置向用户分发内容

**English**: A geographically distributed network of servers that delivers content to users from the nearest location

**提示**: CDN = content delivered from nearest server. '内容分发网络'. For static assets, reduces latency globally.

**示例**: "静态资源上 CDN" → 把图片、JS、CSS 等静态文件放到 CDN 上加速访问

---

### Serverless
**中文**: 云服务商管理基础设施、你只需按实际执行时间付费的云计算模型

**English**: A cloud model where the provider manages infrastructure and you only pay for actual execution time

**提示**: Serverless = no server management, pay per execution. '无服务器'. Examples: AWS Lambda, Cloudflare Workers.

**示例**: "用 serverless 部署" → 不需要管理服务器，按调用次数付费

---

### Unit Test
**中文**: 单独测试各个函数或方法以验证其正确性

**English**: Testing individual functions or methods in isolation to verify they work correctly

**提示**: Unit test = test individual functions in isolation. '单元测试'. Fast, cheap, many. Testing pyramid base.

**示例**: "写个单测覆盖这个函数" → 为这个函数编写单元测试，验证输入输出

---

### Integration Test
**中文**: 测试多个组件协同工作的正确性

**English**: Testing that multiple components work together correctly as a group

**提示**: Integration test = test components working together. '集成测试'. Slower than unit tests, catches interface issues.

**示例**: "跑一下集成测试" → 测试各模块之间的交互是否正常

---

### Mock
**中文**: 在测试中模拟真实依赖行为的假对象

**English**: A fake object that simulates the behavior of a real dependency in tests

**提示**: Mock = fake object for testing. '模拟对象'. Replaces real dependencies. Mock vs Stub: mock verifies behavior, stub provides data.

**示例**: "把数据库调用 mock 掉" → 用假对象替代真实数据库调用，让测试更快更可控

---

### TDD
**中文**: 先写测试再写实现代码的开发方法（红 → 绿 → 重构）

**English**: A development approach where you write tests before writing the implementation code (Red → Green → Refactor)

**提示**: TDD = write test first, then code. '测试驱动开发'. Cycle: Red (fail) → Green (pass) → Refactor.

**示例**: "用 TDD 的方式开发" → 先写失败的测试，再写代码让测试通过，最后重构

---

### Event-Driven
**中文**: 组件通过生产和消费事件（而非直接调用）来通信的架构

**English**: An architecture where components communicate by producing and consuming events rather than direct calls

**提示**: Event-Driven = communicate via events, not direct calls. '事件驱动'. Enables loose coupling, async processing.

**示例**: "改成事件驱动架构" → 用事件总线替代直接调用，实现松耦合

---

### Message Queue
**中文**: 通过排队消息实现服务间异步通信的系统

**English**: A system for asynchronous communication between services through queued messages

**提示**: Message Queue = async communication between services. '消息队列'. Examples: RabbitMQ, Kafka, Redis Streams.

**示例**: "用消息队列解耦" → 通过 MQ 异步处理，减少服务间的直接依赖

---

### Circuit Breaker
**中文**: 通过停止调用故障服务并返回降级响应来防止级联失败的模式

**English**: A pattern that prevents cascading failures by stopping calls to a failing service and returning a fallback response

**提示**: Circuit Breaker = stop calling failing service. '熔断'. States: closed → open → half-open. Prevents cascade failures.

**示例**: "加个熔断，防止雪崩" → 当下游服务故障时，快速失败而不是让请求堆积

---

### Retry
**中文**: 自动重试失败的操作，通常使用指数退避策略

**English**: Automatically retrying a failed operation, often with exponential backoff

**提示**: Retry = try again on failure. '重试'. Use exponential backoff. Only retry idempotent operations.

**示例**: "接口超时了，自动重试一下" → 调用失败后等待一段时间再重试，通常是指数退避

---

### Git Branch
**中文**: 版本控制中独立的开发线路

**English**: An independent line of development in version control

**提示**: Branch = independent development line. '分支'. Strategies: Git Flow, GitHub Flow, Trunk-based.

**示例**: "拉个新分支开发" → 从主分支创建一个新分支，在上面开发新功能

---

### Merge
**中文**: 将一个分支的变更合并到另一个分支

**English**: Combining changes from one branch into another

**提示**: Merge = combine branches. '合并'. Creates merge commit. vs Rebase = replay commits linearly.

**示例**: "把 feature 分支合并到 main" → 将功能分支的代码变更合并回主分支

---

### Rebase
**中文**: 将一个分支的提交重放到另一个分支的基础上，创建线性历史

**English**: Replaying commits from one branch onto the base of another, creating a linear history

**提示**: Rebase = replay commits on new base. '变基'. Creates linear history. Don't rebase shared branches.

**示例**: "rebase 到 main 上" → 把当前分支的提交重放到 main 分支的最新提交之后

---

### Conflict
**中文**: 两个分支修改了同一行代码，Git 无法自动合并

**English**: When two branches modify the same lines of code and Git cannot automatically merge them

**提示**: Conflict = can't auto-merge, needs manual resolution. '冲突'. Common in team development.

**示例**: "有冲突，需要手动解决" → 合并时同一文件被不同分支修改，需要人工决定保留哪个版本

---

### XSS
**中文**: 将恶意脚本注入到其他用户查看的网页中的安全漏洞

**English**: A security vulnerability where malicious scripts are injected into web pages viewed by other users

**提示**: XSS = inject malicious script into webpage. '跨站脚本'. Fix: escape user input, use CSP headers.

**示例**: "这里有个 XSS 漏洞" → 用户输入没有转义，可能被注入恶意脚本

---

### CSRF
**中文**: 欺骗用户浏览器向已认证的网站发送非预期请求的攻击方式

**English**: An attack that tricks a user's browser into making unwanted requests to a site where they're authenticated

**提示**: CSRF = trick browser into unwanted requests. '跨站请求伪造'. Fix: CSRF tokens, SameSite cookies.

**示例**: "加个 CSRF token 防护" → 在表单中添加一次性令牌，防止跨站请求伪造

---

### SQL Injection
**中文**: 利用数据库查询构造中的安全漏洞进行代码注入的技术

**English**: A code injection technique that exploits security vulnerabilities in database query construction

**提示**: SQL Injection = malicious SQL via user input. 'SQL 注入'. Fix: parameterized queries, ORM. NEVER concatenate user input into SQL.

**示例**: "这里可能有 SQL 注入风险" → 用户输入直接拼接到 SQL 语句中，可能被执行恶意 SQL

---

### N+1 Query
**中文**: 获取 N 条数据需要 N+1 次数据库查询（而非 1-2 次）的性能反模式

**English**: A performance anti-pattern where fetching a list of N items requires N+1 database queries instead of 1-2

**提示**: N+1 query = fetch list + each item separately. 'N+1 问题'. Fix: eager loading, batch query. Common ORM pitfall.

**示例**: "这里有 N+1 问题" → 循环中每次迭代都查询数据库，应该改为批量查询

---

### Profiling
**中文**: 分析程序运行时行为以找到性能瓶颈

**English**: Analyzing a program's runtime behavior to identify performance bottlenecks

**提示**: Profiling = analyze runtime performance. '性能分析'. Tools: cProfile (Python), Chrome DevTools, pprof (Go).

**示例**: "先 profile 一下看看瓶颈在哪" → 用性能分析工具定位代码中的性能瓶颈

---

### Bottleneck
**中文**: 系统中限制整体性能或吞吐量的环节

**English**: The point in a system that limits overall performance or throughput

**提示**: Bottleneck = weakest link limiting performance. '瓶颈'. Find with profiling, fix the slowest part first.

**示例**: "数据库是瓶颈" → 系统的性能瓶颈在数据库层面

---

### Open Source
**中文**: 源代码可供任何人检查、修改和增强的软件

**English**: Software with source code that anyone can inspect, modify, and enhance

**提示**: Open Source = public code, free to use/modify. '开源'. Licenses: MIT, Apache, GPL. '开源' ≠ free (免费).

**示例**: "这个库是开源的" → 代码公开在 GitHub 上，可以免费使用和修改

---

### Git Flow
**中文**: 定义特定分支角色（main、develop、feature、release、hotfix）的分支模型

**English**: A branching model that defines specific branch roles (main, develop, feature, release, hotfix)

**提示**: Git Flow = structured branching model. 'Git 工作流'. main (production), develop (integration), feature/*, release/*, hotfix/*.

**示例**: "用 Git Flow 管理分支" → 按照 Git Flow 模型创建和管理不同用途的分支

---

### Infrastructure as Code
**中文**: 通过机器可读的配置文件（而非手动操作）来管理基础设施

**English**: Managing infrastructure through machine-readable configuration files rather than manual processes

**提示**: IaC = infrastructure as code, not manual setup. '基础设施即代码'. Tools: Terraform, Pulumi, CloudFormation.

**示例**: "用 Terraform 做 IaC" → 用代码定义和管理云基础设施，可版本化、可复现

---

### GitOps
**中文**: 以 Git 作为基础设施和应用交付唯一事实来源的部署范式

**English**: A deployment paradigm where Git is the single source of truth for infrastructure and application delivery

**提示**: GitOps = Git as single source of truth for infra. 'Git 运维'. Declarative, version-controlled, automated.

**示例**: "用 GitOps 管理部署" → 所有基础设施和应用配置都在 Git 中，变更通过 PR 触发自动部署

---

### Blue-Green Deployment
**中文**: 维护两个相同环境的部署策略；流量从蓝色（当前）切换到绿色（新版）

**English**: A deployment strategy with two identical environments; traffic switches from blue (current) to green (new)

**提示**: Blue-Green = two identical envs, switch traffic. '蓝绿部署'. Instant rollback by switching back.

**示例**: "用蓝绿部署，方便回滚" → 同时维护新旧两套环境，切换流量即可回滚

---

### Canary Release
**中文**: 在全量部署前，先将新版本逐步推送给一小部分用户

**English**: Gradually rolling out a new version to a small subset of users before full deployment

**提示**: Canary release = gradual rollout to subset of users. '灰度发布'. Detect issues before full deployment.

**示例**: "先灰度 10% 的用户" → 新版本先给 10% 的用户使用，观察无问题后再全量

---

### API Gateway
**中文**: 所有 API 请求的统一入口，处理路由、认证、限流等

**English**: A single entry point for all API requests, handling routing, authentication, rate limiting, etc.

**提示**: API Gateway = single entry point for all APIs. 'API 网关'. Handles auth, rate limiting, routing. Key in microservices.

**示例**: "在前面加个 API 网关" → 统一入口处理认证、限流、路由等横切关注点

---

### Webhook
**中文**: 由一个系统的事件触发的 HTTP 回调，向另一个系统的 URL 发送数据

**English**: An HTTP callback triggered by an event in one system, sending data to another system's URL

**提示**: Webhook = HTTP callback on event. '回调'/'钩子'. Push-based, not pull. Like a reverse API call.

**示例**: "配个 webhook 通知我们" → 当事件发生时，对方系统会向我们的 URL 发送 HTTP 请求通知

---

### gRPC
**中文**: 使用 Protocol Buffers 序列化和 HTTP/2 传输的高性能 RPC 框架

**English**: A high-performance RPC framework using Protocol Buffers for serialization and HTTP/2 for transport

**提示**: gRPC = high-performance RPC with protobuf. Google's framework. Fast, typed, bidirectional streaming.

**示例**: "内部服务间用 gRPC 通信" → 微服务之间用 gRPC 进行高性能的远程过程调用

---

### GraphQL
**中文**: 一种 API 查询语言，让客户端精确请求所需的数据

**English**: A query language for APIs that lets clients request exactly the data they need

**提示**: GraphQL = query exactly what you need. Alternative to REST. Client specifies fields. Avoids over/under-fetching.

**示例**: "用 GraphQL 替代 REST API" → 客户端可以精确指定需要哪些字段，避免过度获取或不足获取

---

### REST
**中文**: 使用标准 HTTP 方法（GET、POST、PUT、DELETE）和基于资源的 URL 的 API 架构风格

**English**: An architectural style for APIs using standard HTTP methods (GET, POST, PUT, DELETE) and resource-based URLs

**提示**: REST = HTTP-based API style. Resources + HTTP methods. GET=read, POST=create, PUT=update, DELETE=delete.

**示例**: "用 REST 风格设计 API" → 用 HTTP 方法映射 CRUD 操作，URL 表示资源

---

### WebSocket
**中文**: 在单个 TCP 连接上提供全双工通信通道的协议

**English**: A protocol providing full-duplex communication channels over a single TCP connection

**提示**: WebSocket = persistent bidirectional connection. '长连接'. For real-time: chat, live data, gaming. vs HTTP polling.

**示例**: "用 WebSocket 做实时推送" → 建立长连接，服务端可以主动向客户端推送消息

---

### Polling
**中文**: 通过定期发送 HTTP 请求来反复检查更新

**English**: Repeatedly checking for updates at regular intervals by making HTTP requests

**提示**: Polling = repeatedly check for updates. '轮询'. Simple but wasteful. WebSocket/SSE better for real-time.

**示例**: "用轮询获取最新状态" → 每隔几秒发一次请求检查数据是否有更新

---

### Dead Letter Queue
**中文**: 无法成功处理的消息被发送到的队列，供后续分析

**English**: A queue where messages that cannot be processed successfully are sent for later analysis

**提示**: Dead Letter Queue = where failed messages go. '死信队列'. For debugging, retry, or manual intervention.

**示例**: "失败消息发到死信队列" → 处理失败的消息不要丢弃，放到 DLQ 后续排查

---

### Rate Limiting
**中文**: 控制客户端在一段时间内可以发送的请求数量

**English**: Controlling the number of requests a client can make within a time period

**提示**: Rate Limiting = cap requests per time period. '限流'. Algorithms: token bucket, sliding window. Return 429 when exceeded.

**示例**: "接口加个限流" → 限制每个用户每分钟最多调用多少次，防止滥用

---

### Graceful Degradation
**中文**: 系统在部分组件故障时仍能以降级功能继续运行的能力

**English**: A system's ability to continue operating with reduced functionality when some components fail

**提示**: Graceful Degradation = reduced functionality rather than total failure. '优雅降级'. Return cached/default data when service is down.

**示例**: "服务挂了就降级返回默认值" → 依赖服务不可用时，返回缓存数据或默认值而不是报错

---

### Chaos Engineering
**中文**: 故意向系统注入故障以测试其韧性并发现弱点

**English**: Intentionally injecting failures into a system to test its resilience and identify weaknesses

**提示**: Chaos Engineering = break things on purpose to find weaknesses. '混沌工程'. Tool: Chaos Monkey. Proactive resilience testing.

**示例**: "做混沌工程演练" → 故意模拟服务器宕机、网络延迟等故障，验证系统是否能正常应对

---

### SRE
**中文**: 将软件工程实践应用于基础设施和运维问题的学科

**English**: A discipline that applies software engineering practices to infrastructure and operations problems

**提示**: SRE = software engineering approach to operations. '站点可靠性工程'. Google's approach. Error budgets, toil reduction.

**示例**: "用 SRE 的方式管理服务" → 用软件工程的方法论来解决运维问题，关注可靠性指标

