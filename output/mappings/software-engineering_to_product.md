---
source: software-engineering
target: product
tags: [glossary, mapping]
---

# software-engineering → product

跨领域术语映射关系

## [[software-engineering/CI-CD|CI/CD]] → [[product/Roadmap|Roadmap]]

📌 持续交付支撑路线图落地

**CI/CD**: 将代码变更频繁集成到共享仓库的实践，通过自动化构建、测试和部署来快速交付软件

**Roadmap**: 产品愿景和方向的高级可视化概览

## [[software-engineering/Technical-Debt|Technical Debt]] → [[product/Prioritization|Prioritization]]

📌 技术债影响优先级排序

**Technical Debt**: 由于当前选择了简单/快速的方案而非更优但耗时更长的方案，而导致未来需要额外返工的隐性成本

**Prioritization**: 根据价值、工作量和紧迫度决定功能或任务的开发顺序

## [[software-engineering/API|API]] → [[product/User-Story|User Story]]

📌 接口服务于用户故事

**API**: 一组规则和协议，允许不同的软件组件之间相互通信

**User Story**: 从最终用户角度描述功能的简短叙述（作为[用户]，我想要[目标]，以便[获得价值]）

## [[software-engineering/Latency|Latency]] → [[product/Bounce-Rate|Bounce Rate]]

📌 延迟高导致跳出率高

**Latency**: 从发起请求到收到响应之间的时间延迟，通常以毫秒为单位

**Bounce Rate**: 只浏览一个页面就离开网站的访客百分比

## [[software-engineering/Caching|Caching]] → [[product/Retention|Retention]]

📌 缓存提升性能从而提高留存

**Caching**: 将频繁访问的数据存储在更快的存储层中，以减少访问时间和后端负载

**Retention**: 在给定时间段内继续使用产品的用户百分比

## [[software-engineering/Decoupling|Decoupling]] → [[product/Scoping|Scoping]]

📌 解耦让范围界定更灵活

**Decoupling**: 减少组件之间的依赖关系，使其可以独立变更、部署或扩展

**Scoping**: 定义项目或发布中包含和不包含内容的边界

## [[software-engineering/Rollback|Rollback]] → [[product/Churn|Churn]]

📌 快速回滚减少用户流失

**Rollback**: 将系统或部署恢复到之前已知正常的状态

**Churn**: 在给定时间段内停止使用产品的用户百分比

## [[software-engineering/Scaffold|Scaffold]] → [[product/MVP|MVP]]

📌 脚手架用于快速搭建 MVP

**Scaffold**: 预配置的项目结构和模板代码，用于快速启动开发

**MVP**: 产品最简单的版本，可以发布以测试核心假设并收集用户反馈

## [[software-engineering/Feature-Flag|Feature Flag]] → [[product/AB-Testing|AB Testing]]

📌 功能开关是 A/B 测试的技术实现

**Feature Flag**: 在运行时启用或禁用功能的机制，无需部署新代码

**AB Testing**: 对比两个版本（A 和 B）以确定哪个在特定指标上表现更好的实验

## [[software-engineering/Observability|Observability]] → [[product/Funnel|Funnel]]

📌 可观测性支撑漏斗分析

**Observability**: 通过系统的外部输出（日志、指标、链路追踪）来理解系统内部状态的能力

**Funnel**: 描述用户从认知到转化各阶段的模型，每个阶段都有用户流失

## [[software-engineering/E2E-Testing|E2E Testing]] → [[product/NPS|NPS]]

📌 端到端测试保障用户体验

**E2E Testing**: 从头到尾测试整个应用流程，模拟真实用户场景

**NPS**: 基于用户推荐意愿（0-10 分）衡量客户忠诚度的指标

## [[software-engineering/Unit-Test|Unit Test]] → [[product/Pain-Point|Pain Point]]

📌 单元测试预防痛点（bug）

**Unit Test**: 单独测试各个函数或方法以验证其正确性

**Pain Point**: 用户遇到的具体问题或挫败感，代表了产品解决方案的机会

## [[software-engineering/Circuit-Breaker|Circuit Breaker]] → [[product/Churn|Churn]]

📌 熔断防止系统崩溃导致用户流失

**Circuit Breaker**: 通过停止调用故障服务并返回降级响应来防止级联失败的模式

**Churn**: 在给定时间段内停止使用产品的用户百分比

## [[software-engineering/Webhook|Webhook]] → [[product/Viral-Loop|Viral Loop]]

📌 回调通知支撑病毒传播机制

**Webhook**: 由一个系统的事件触发的 HTTP 回调，向另一个系统的 URL 发送数据

**Viral Loop**: 现有用户自然邀请新用户的机制，产生指数级增长

## [[software-engineering/Rate-Limiting|Rate Limiting]] → [[product/Conversion-Rate|Conversion Rate]]

📌 限流保障服务稳定，维护转化率

**Rate Limiting**: 控制客户端在一段时间内可以发送的请求数量

**Conversion Rate**: 完成期望操作（购买、注册等）的用户占总访问者的百分比

---

已映射: 15 | 未映射: 67