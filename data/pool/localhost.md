---
slug: localhost
name: Localhost
builder: xuxueli
category: ''
summary_zh: ''
inspiration: ''
summary_en: ''
inspiration_en: ''
priority_review: false
project_type: new_application
industries: []
industries_en: []
jobs: []
jobs_en: []
regions: []
regions_en: []
open_source: false
url: http://localhost:3000`，默认账号
canonical_url: https://localhost
summary: "> 一套仓库，三种模式；一行 SQL ，全栈生成； AI 加持，开箱即用。\r\n\r\n\r\n本版本是一次承前启后的重大升级，围绕「**前端工程全面 TypeScript 化**」「**React\
  \ 全新前端版本交付**」「**AI + SKILL 驱动开发**」三大核心亮点展开，让中后台业务开发从此进入 AI 辅助时代。\r\n\r\n***\r\n\r\n## 一、Release Notes\
  \ （ v2.1.0 · 2026-08-30 ）\r\n\r\n*   1 、 [新增] **React 前端版本发布**：React + Vite + AntDesign + TypeScript\
  \ 前端工程正式交付，与 Vue 模式共享统一后端 API ，随生产构建并行发布；\r\n*   2 、 [新增] **Vue 前端版本升级 TypeScript**：Vue3 与 React 前端模块全面升级\
  \ TypeScript ，类型约束更严谨、IDE 提示更完善；\r\n*   3 、 [新增] **AI + SKILL 驱动开发**：仓库内置 `xxl-boot-monolith / xxl-boot-vue\
  \ / xxl-boot-react` 三大开发 SKILL ，AI 编程助手可自动识别并加载，按平台规范直生业务代码、自动落位并附校验清单，加速业务开发；\r\n*   4 、 [新增] **前端规范增强**：Vue\
  \ 模块引入 ESLint + Prettier ，React 模块引入 Biome ，提升代码规范性与可维护性；\r\n*   5 、 [新增] **代码生成器兼容 TypeScript**：生成器支持前端\
  \ `type/types` 文件，并内置 vue3/react 前端模板（ types/api/view ），前后端分离（ Vue/React ）模式可一键生成前端代码；\r\n*   6 、 [新增]\
  \ **“新增业务模块”支持三方式**：传统手工、内置代码生成器、AI + SKILL 驱动，均输出等价代码与菜单权限 SQL ，可混合切换；\r\n*   7 、 [文档] **官方文档重构**：快速入门按\
  \ 单体 / Vue / React 三种模式分述；操作指南改为“能力总览 + 分章节详解”总分结构；新增“新增业务模块”三方式详解；总体设计完善（新增 三种运行模式、统一响应规范、业务扩展与菜单零路由、AI\
  \ + Skill 辅助开发设计）等章节；\r\n*   8 、 [升级] 升级多项依赖至较新版本。\r\n\r\n***\r\n\r\n## 二、三大亮点速览\r\n\r\n### 亮点一：前端工程全面\
  \ TypeScript 化\r\n\r\nVue3 与 React 双前端模块均完成 TypeScript 升级，配合 Vite 构建工具，类型约束更严谨、IDE 智能提示更完善，从编译期即可发现大量隐患，让团队协作与长期维护更加可靠。\r\
  \n\r\n### 亮点二：React 全新前端版本正式交付\r\n\r\nv2.1.0 正式发布 React 前端版本（ xxl-boot-ui-react ），采用 React + Vite +\
  \ AntDesign + TypeScript 技术栈，与 Vue 模式共享同一套后端 API ，三种模式如同一套「前后端骨架」，按团队技术栈自由选型。\r\n\r\n### 亮点三：AI + SKILL\
  \ 驱动开发\r\n\r\n仓库内置 `xxl-boot-monolith / xxl-boot-vue / xxl-boot-react` 三大开发 SKILL 。接入 AI 编程助手（如 opencode\
  \ ）后，只需描述业务诉求，AI 便会自动加载对应 SKILL ，按平台规范直生业务代码、自动落位并附校验清单，业务开发正式进入 AI 辅助时代。\r\n\r\n***\r\n\r\n## 三、Docker\
  \ Compose 快速部署\r\n\r\nv2.1.0 延续并强化了 Docker Compose 一键部署能力，内置 **三种运行模式** 的编排配置，均可一条命令拉起整套环境：\r\n\r\n\
  | 运行模式          | Docker 编排目录            | 前端技术栈                 | 端口          |\r\n| -------------\
  \ | ---------------------- | --------------------- | ----------- |\r\n| A 、单体模式        | `docker/monolith`\
  \      | AdminLTE + FreeMarker | 8080        |\r\n| B 、前后端分离 Vue   | `docker/modular-vue`   | Vue3 +\
  \ ElementPlus    | 8090 + 3000 |\r\n| C 、前后端分离 React | `docker/modular-react` | React + AntDesign  \
  \   | 8090 + 4000 |\r\n\r\n以 **前后端分离 Vue 模式** 为例，一键部署步骤如下：\r\n\r\n    // 第一步：前往仓库目录，并构建项目\r\n    cd\
  \ ./xxl-boot\r\n    mvn clean package -Dmaven.test.skip=true\r\n\r\n    // 第二步：进入 docker/modular-vue\
  \ 目录，自定义 .env 配置\r\n    // 如修改 MYSQL_PATH / REDIS_PATH 设置数据持久化目录、MYSQL_ROOT_PASSWORD 数据库密码等\r\n    cd\
  \ ./docker/modular-vue/\r\n    cat .env\r\n\r\n    // 第三步：启动项目（停止使用 docker compose down ）\r\n    docker\
  \ compose up -d\r\n\r\n> 说明：\r\n>\r\n> *   编排会自动拉起 **MySQL （ xxl\\_boot 库）**、**Redis**、**xxl-boot-api**\
  \ 与 **xxl-boot-ui-vue** 四个容器；\r\n> *   数据库初始化脚本（`tables_xxl_boot.sql` + `tables_xxl_boot_modular_vue.sql`）已挂载至\
  \ MySQL 首次启动目录，**数据库首启会自动建表初始化**，开箱即用；\r\n> *   访问地址：前端 `http://localhost:3000`，默认账号 `admin / 123456`；\r\
  \n> *   单体模式 / React 模式仅编排目录与前端镜像不同，操作流程完全一致。\r\n\r\n***\r\n\r\n## 四、新增业务模块：三方式任选\r\n\r\nv2.1.0 将「新增一个带列表、增删改查的业务模块」沉淀为三种标准化方式，产出可无缝切换：\r\
  \n\r\n| 方式              | 适用场景             | 特点                    | 产出物                          |\r\
  \n| --------------- | ---------------- | --------------------- | ---------------------------- |\r\n\
  | A 、传统手工方式        | 字段特殊、深度定制        | 可控性最强                 | 手工全套后端 + 前端代码                |\r\n|\
  \ B 、内置代码生成器       | 标准化 CRUD 模块      | 一行 SQL 全栈生成、含菜单 SQL   | 后端 6 件套 + 前端 3 文件 + init SQL |\r\n|\
  \ C 、AI + SKILL 方式 | 已接入 AI 助手、追求极致效率 | 全自动编排直生 + 自动落位 + 校验清单 | 与生成器等价的全套代码 + SQL            |\r\n\r\
  \n**代码生成**：只需在后台「工具-代码生成」录入一条建表 SQL ，即可自动生成后端 `controller/service/mapper&xml/entity` 与前端 `types/api/view`\
  \ 全套代码，并附带「菜单 + 按钮 + 授权」初始化 SQL — 从数据库到可运行页面一键打通。\r\n\r\n**AI + SKILL**：打开 AI 编程助手（如 opencode ）打开仓库，通过\
  \ `/xxl-boot-vue` 等前缀调用对应 SKILL 并描述诉求，AI 会依次完成「需求澄清 → 数据建模 → 后端 → 前端 → 菜单权限 → 联调验证」，全自动落位交付。\r\n\r\n\
  ***\r\n\r\n## 五、关于 XXL-BOOT\r\n\r\nXXL-BOOT 是一个**易学易用、AI 驱动、开箱即用**的快速开发平台，内置安全登录、RBAC 权限管控、端到端代码生成、AI\
  \ + SKILL 加速开发、响应式 UI 等能力，整合流行前后端技术，致力为中小企业与个人开发者打造开箱即用的中后台解决方案。\r\n\r\n### 一套仓库，三种模式\r\n\r\n采用 Monorepo\
  \ 统一托管三种工程形态 —— 单体（`xxl-boot-admin`）、前后端分离 Vue （`xxl-boot-api` + `xxl-boot-ui-vue`）、前后端分离 React （`xxl-boot-api`\
  \ + `xxl-boot-ui-react`）。按业务诉求三选一，统一版本管理、一键构建、按需部署，切换成本极低。\r\n\r\n### 核心特性\r\n\r\n*   **快速开发**：Monorepo\
  \ 三种模式、AI + SKILL 驱动、代码生成、表单构建；\r\n*   **账号与安全**：XXL-SSO 安全登录、RBAC 权限管控、审计日志、异常防护；\r\n*   **系统管理**：用户\
  \ / 角色 / 资源 / 组织 / 字典 / 配置中心 / 站内消息 / 在线用户 / 系统监控；\r\n*   **研发与架构**：响应式 UI 、国际化（中英双语言）、标准分层研发规范、丰富分布式扩展能力。\r\
  \n\r\n***\r\n\r\n## 六、功能界面一览\r\n\r\n略\r\n\r\n***\r\n\r\n\r\n## 七、资料\r\n\r\n*   中文文档：<https://www.xuxueli.com/xxl-boot/>\r\
  \n*   GitHub：<https://github.com/xuxueli/xxl-boot>"
first_seen: '2026-08-30T15:50:25Z'
last_seen: '2026-08-31T00:37:15Z'
status: pending_filter
sources:
- v2ex
sightings:
- source: v2ex
  url: http://localhost:3000`，默认账号
  seen_at: '2026-08-31T00:37:15Z'
  metrics:
    comments: 1
  kind: product
---

# Localhost

> 一套仓库，三种模式；一行 SQL ，全栈生成； AI 加持，开箱即用。


本版本是一次承前启后的重大升级，围绕「**前端工程全面 TypeScript 化**」「**React 全新前端版本交付**」「**AI + SKILL 驱动开发**」三大核心亮点展开，让中后台业务开发从此进入 AI 辅助时代。

***

## 一、Release Notes （ v2.1.0 · 2026-08-30 ）

*   1 、 [新增] **React 前端版本发布**：React + Vite + AntDesign + TypeScript 前端工程正式交付，与 Vue 模式共享统一后端 API ，随生产构建并行发布；
*   2 、 [新增] **Vue 前端版本升级 TypeScript**：Vue3 与 React 前端模块全面升级 TypeScript ，类型约束更严谨、IDE 提示更完善；
*   3 、 [新增] **AI + SKILL 驱动开发**：仓库内置 `xxl-boot-monolith / xxl-boot-vue / xxl-boot-react` 三大开发 SKILL ，AI 编程助手可自动识别并加载，按平台规范直生业务代码、自动落位并附校验清单，加速业务开发；
*   4 、 [新增] **前端规范增强**：Vue 模块引入 ESLint + Prettier ，React 模块引入 Biome ，提升代码规范性与可维护性；
*   5 、 [新增] **代码生成器兼容 TypeScript**：生成器支持前端 `type/types` 文件，并内置 vue3/react 前端模板（ types/api/view ），前后端分离（ Vue/React ）模式可一键生成前端代码；
*   6 、 [新增] **“新增业务模块”支持三方式**：传统手工、内置代码生成器、AI + SKILL 驱动，均输出等价代码与菜单权限 SQL ，可混合切换；
*   7 、 [文档] **官方文档重构**：快速入门按 单体 / Vue / React 三种模式分述；操作指南改为“能力总览 + 分章节详解”总分结构；新增“新增业务模块”三方式详解；总体设计完善（新增 三种运行模式、统一响应规范、业务扩展与菜单零路由、AI + Skill 辅助开发设计）等章节；
*   8 、 [升级] 升级多项依赖至较新版本。

***

## 二、三大亮点速览

### 亮点一：前端工程全面 TypeScript 化

Vue3 与 React 双前端模块均完成 TypeScript 升级，配合 Vite 构建工具，类型约束更严谨、IDE 智能提示更完善，从编译期即可发现大量隐患，让团队协作与长期维护更加可靠。

### 亮点二：React 全新前端版本正式交付

v2.1.0 正式发布 React 前端版本（ xxl-boot-ui-react ），采用 React + Vite + AntDesign + TypeScript 技术栈，与 Vue 模式共享同一套后端 API ，三种模式如同一套「前后端骨架」，按团队技术栈自由选型。

### 亮点三：AI + SKILL 驱动开发

仓库内置 `xxl-boot-monolith / xxl-boot-vue / xxl-boot-react` 三大开发 SKILL 。接入 AI 编程助手（如 opencode ）后，只需描述业务诉求，AI 便会自动加载对应 SKILL ，按平台规范直生业务代码、自动落位并附校验清单，业务开发正式进入 AI 辅助时代。

***

## 三、Docker Compose 快速部署

v2.1.0 延续并强化了 Docker Compose 一键部署能力，内置 **三种运行模式** 的编排配置，均可一条命令拉起整套环境：

| 运行模式          | Docker 编排目录            | 前端技术栈                 | 端口          |
| ------------- | ---------------------- | --------------------- | ----------- |
| A 、单体模式        | `docker/monolith`      | AdminLTE + FreeMarker | 8080        |
| B 、前后端分离 Vue   | `docker/modular-vue`   | Vue3 + ElementPlus    | 8090 + 3000 |
| C 、前后端分离 React | `docker/modular-react` | React + AntDesign     | 8090 + 4000 |

以 **前后端分离 Vue 模式** 为例，一键部署步骤如下：

    // 第一步：前往仓库目录，并构建项目
    cd ./xxl-boot
    mvn clean package -Dmaven.test.skip=true

    // 第二步：进入 docker/modular-vue 目录，自定义 .env 配置
    // 如修改 MYSQL_PATH / REDIS_PATH 设置数据持久化目录、MYSQL_ROOT_PASSWORD 数据库密码等
    cd ./docker/modular-vue/
    cat .env

    // 第三步：启动项目（停止使用 docker compose down ）
    docker compose up -d

> 说明：
>
> *   编排会自动拉起 **MySQL （ xxl\_boot 库）**、**Redis**、**xxl-boot-api** 与 **xxl-boot-ui-vue** 四个容器；
> *   数据库初始化脚本（`tables_xxl_boot.sql` + `tables_xxl_boot_modular_vue.sql`）已挂载至 MySQL 首次启动目录，**数据库首启会自动建表初始化**，开箱即用；
> *   访问地址：前端 `http://localhost:3000`，默认账号 `admin / 123456`；
> *   单体模式 / React 模式仅编排目录与前端镜像不同，操作流程完全一致。

***

## 四、新增业务模块：三方式任选

v2.1.0 将「新增一个带列表、增删改查的业务模块」沉淀为三种标准化方式，产出可无缝切换：

| 方式              | 适用场景             | 特点                    | 产出物                          |
| --------------- | ---------------- | --------------------- | ---------------------------- |
| A 、传统手工方式        | 字段特殊、深度定制        | 可控性最强                 | 手工全套后端 + 前端代码                |
| B 、内置代码生成器       | 标准化 CRUD 模块      | 一行 SQL 全栈生成、含菜单 SQL   | 后端 6 件套 + 前端 3 文件 + init SQL |
| C 、AI + SKILL 方式 | 已接入 AI 助手、追求极致效率 | 全自动编排直生 + 自动落位 + 校验清单 | 与生成器等价的全套代码 + SQL            |

**代码生成**：只需在后台「工具-代码生成」录入一条建表 SQL ，即可自动生成后端 `controller/service/mapper&xml/entity` 与前端 `types/api/view` 全套代码，并附带「菜单 + 按钮 + 授权」初始化 SQL — 从数据库到可运行页面一键打通。

**AI + SKILL**：打开 AI 编程助手（如 opencode ）打开仓库，通过 `/xxl-boot-vue` 等前缀调用对应 SKILL 并描述诉求，AI 会依次完成「需求澄清 → 数据建模 → 后端 → 前端 → 菜单权限 → 联调验证」，全自动落位交付。

***

## 五、关于 XXL-BOOT

XXL-BOOT 是一个**易学易用、AI 驱动、开箱即用**的快速开发平台，内置安全登录、RBAC 权限管控、端到端代码生成、AI + SKILL 加速开发、响应式 UI 等能力，整合流行前后端技术，致力为中小企业与个人开发者打造开箱即用的中后台解决方案。

### 一套仓库，三种模式

采用 Monorepo 统一托管三种工程形态 —— 单体（`xxl-boot-admin`）、前后端分离 Vue （`xxl-boot-api` + `xxl-boot-ui-vue`）、前后端分离 React （`xxl-boot-api` + `xxl-boot-ui-react`）。按业务诉求三选一，统一版本管理、一键构建、按需部署，切换成本极低。

### 核心特性

*   **快速开发**：Monorepo 三种模式、AI + SKILL 驱动、代码生成、表单构建；
*   **账号与安全**：XXL-SSO 安全登录、RBAC 权限管控、审计日志、异常防护；
*   **系统管理**：用户 / 角色 / 资源 / 组织 / 字典 / 配置中心 / 站内消息 / 在线用户 / 系统监控；
*   **研发与架构**：响应式 UI 、国际化（中英双语言）、标准分层研发规范、丰富分布式扩展能力。

***

## 六、功能界面一览

略

***


## 七、资料

*   中文文档：<https://www.xuxueli.com/xxl-boot/>
*   GitHub：<https://github.com/xuxueli/xxl-boot>

## 笔记


