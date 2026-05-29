---
source: product
target: software-engineering
tags: [glossary, mapping]
---

# product → software-engineering

跨领域术语映射关系

## [[product/MVP|MVP]] → [[software-engineering/Scaffold|Scaffold]]

📌 快速搭建可运行的最小版本

**MVP**: 产品最简单的版本，可以发布以测试核心假设并收集用户反馈

**Scaffold**: 预配置的项目结构和模板代码，用于快速启动开发

## [[product/User-Story|User Story]] → [[software-engineering/API|API]]

📌 用户故事最终落实为接口设计

**User Story**: 从最终用户角度描述功能的简短叙述（作为[用户]，我想要[目标]，以便[获得价值]）

**API**: 一组规则和协议，允许不同的软件组件之间相互通信

## [[product/Scoping|Scoping]] → [[software-engineering/Scaffold|Scaffold]]

📌 范围界定后用脚手架快速启动

**Scoping**: 定义项目或发布中包含和不包含内容的边界

**Scaffold**: 预配置的项目结构和模板代码，用于快速启动开发

## [[product/AB-Testing|AB Testing]] → [[software-engineering/Feature-Flag|Feature Flag]]

📌 功能开关是实现 A/B 测试的技术手段

**AB Testing**: 对比两个版本（A 和 B）以确定哪个在特定指标上表现更好的实验

**Feature Flag**: 在运行时启用或禁用功能的机制，无需部署新代码

## [[product/Conversion-Rate|Conversion Rate]] → [[software-engineering/Feature-Flag|Feature Flag]]

📌 通过功能开关做 A/B 测试优化转化率

**Conversion Rate**: 完成期望操作（购买、注册等）的用户占总访问者的百分比

**Feature Flag**: 在运行时启用或禁用功能的机制，无需部署新代码

## [[product/Pain-Point|Pain Point]] → [[software-engineering/API|API]]

📌 痛点通常通过技术方案（接口/服务）来解决

**Pain Point**: 用户遇到的具体问题或挫败感，代表了产品解决方案的机会

**API**: 一组规则和协议，允许不同的软件组件之间相互通信

## [[product/Funnel|Funnel]] → [[software-engineering/Observability|Observability]]

📌 漏斗分析需要可观测性支持

**Funnel**: 描述用户从认知到转化各阶段的模型，每个阶段都有用户流失

**Observability**: 通过系统的外部输出（日志、指标、链路追踪）来理解系统内部状态的能力

## [[product/Growth-Hacking|Growth Hacking]] → [[software-engineering/Feature-Flag|Feature Flag]]

📌 增长实验依赖功能开关

**Growth Hacking**: 通过在营销渠道和产品开发上快速实验，找到最有效增长方式的策略

**Feature Flag**: 在运行时启用或禁用功能的机制，无需部署新代码

## [[product/Retention|Retention]] → [[software-engineering/Caching|Caching]]

📌 缓存提升性能从而提高留存

**Retention**: 在给定时间段内继续使用产品的用户百分比

**Caching**: 将频繁访问的数据存储在更快的存储层中，以减少访问时间和后端负载

## [[product/Churn|Churn]] → [[software-engineering/Caching|Caching]]

📌 降低流失需要缓存优化性能

**Churn**: 在给定时间段内停止使用产品的用户百分比

**Caching**: 将频繁访问的数据存储在更快的存储层中，以减少访问时间和后端负载

## [[product/Backlog|Backlog]] → [[software-engineering/CI-CD|CI/CD]]

📌 待办事项通过 CI/CD 流程交付

**Backlog**: 由产品负责人维护的、按优先级排列的功能、缺陷和任务列表

**CI/CD**: 将代码变更频繁集成到共享仓库的实践，通过自动化构建、测试和部署来快速交付软件

## [[product/Prioritization|Prioritization]] → [[software-engineering/Technical-Debt|Technical Debt]]

📌 优先级排序需要权衡技术债

**Prioritization**: 根据价值、工作量和紧迫度决定功能或任务的开发顺序

**Technical Debt**: 由于当前选择了简单/快速的方案而非更优但耗时更长的方案，而导致未来需要额外返工的隐性成本

## [[product/Roadmap|Roadmap]] → [[software-engineering/CI-CD|CI/CD]]

📌 路线图通过持续交付来实现

**Roadmap**: 产品愿景和方向的高级可视化概览

**CI/CD**: 将代码变更频繁集成到共享仓库的实践，通过自动化构建、测试和部署来快速交付软件

## [[product/NPS|NPS]] → [[software-engineering/E2E-Testing|E2E Testing]]

📌 NPS 反映端到端体验质量

**NPS**: 基于用户推荐意愿（0-10 分）衡量客户忠诚度的指标

**E2E Testing**: 从头到尾测试整个应用流程，模拟真实用户场景

## [[product/Bounce-Rate|Bounce Rate]] → [[software-engineering/Latency|Latency]]

📌 跳出率高通常与延迟有关

**Bounce Rate**: 只浏览一个页面就离开网站的访客百分比

**Latency**: 从发起请求到收到响应之间的时间延迟，通常以毫秒为单位

## [[product/Onboarding|Onboarding]] → [[software-engineering/Scaffold|Scaffold]]

📌 新手引导需要脚手架搭建的原型

**Onboarding**: 引导新用户理解并从产品中获得价值的过程

**Scaffold**: 预配置的项目结构和模板代码，用于快速启动开发

## [[product/Viral-Loop|Viral Loop]] → [[software-engineering/Webhook|Webhook]]

📌 病毒传播需要回调通知机制

**Viral Loop**: 现有用户自然邀请新用户的机制，产生指数级增长

**Webhook**: 由一个系统的事件触发的 HTTP 回调，向另一个系统的 URL 发送数据

## [[product/Product-Led-Growth|Product-Led Growth]] → [[software-engineering/Observability|Observability]]

📌 产品驱动增长需要可观测性来追踪指标

**Product-Led Growth**: 由产品本身驱动获客、转化和扩展的增长策略

**Observability**: 通过系统的外部输出（日志、指标、链路追踪）来理解系统内部状态的能力

## [[product/Freemium|Freemium]] → [[software-engineering/Feature-Flag|Feature Flag]]

📌 功能开关控制免费/付费功能边界

**Freemium**: 基础功能免费、高级功能付费的定价模型

**Feature Flag**: 在运行时启用或禁用功能的机制，无需部署新代码

---

已映射: 19 | 未映射: 20