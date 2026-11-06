---
name: aihero
description: Meta-router & UI playbook — use ONLY when the user explicitly invokes it (/aihero or $aihero attachment). Contains entry gate (idea-first: any "build X" request routes to discussion before UI), skill routing table, asset-research rules (three-source assets, embedded imagery), and the 10-item UI generation doctrine (bright-default palette, layout craft, motion checklist). Trigger ONLY on explicit invocation, never automatically. 识别意图 → 选用精选 skill → 按其指示执行。
---

# AI Hero Skills

精选索引：只路由下表所列 skill（本地均已装在 `~/.agents/skills`，ZCode 可直接发现；部分经 `~/.zcode/skills` 软链接可见）。**表外的一律不主动路由**——更多不等于更好；用户点名 `/命令` 时照常支持。

**按需加载（2026-11-07 结构重构）**：重内容已搬离本文件——规则 11/12 全文与两级交付 Checklist 在 `references/ui-doctrine.md`（**动 UI 前必读**），决策记录在 `references/decision-log.md`（**改守则/路由前查最近条目**），工具模板在 `assets/templates/`（image_pipeline / smoke_test 模板 / overflow_probe，新项目直接取用）。

## 第 0 步：入口判定（2026-11-06 用户定，先于路由表）

任何请求先判一类：**是要"创造什么"，还是"明确的专项操作"？** 思考讨论永远先于执行，UI 永远不抢跑。

1. **创建类**——做一个 X：项目/网站/App/模块/小功能，凡从无到有 → 一律先聊透想法：grill-me（🔒 先确认）→ to-spec → to-tickets → implement。**UI 链不作为入口**，只到 implement 动手做界面前才介入；守则 12-⓪ 是 UI 动工前的设定确认，不是项目第一步
2. **UI 类**——仅当用户明确点名 UI 话题（美化/优化界面/视觉风格/找设计参考）才进 UI 链；且动手前仍先沟通：弹窗问清用户想要什么样的（1-3 个方向题），确认后再改，不闷头执行
3. **专项类**——审查/修 bug/交接/调研/写 PR 等 → 按路由表对应行直走
4. **琐碎类**——一句话小改、单条查询、纯闲聊 → 直接做，不套流程

口诀：**"做一个 X"= 先思考讨论；点名 UI = 进 UI 链但先沟通；改/查/审/聊 = 按表直走；琐碎 = 直接做。**

## 路由表

| 意图信号 | Skill | 调用方式 |
|---|---|---|
| 创建任何新东西（项目/网站/模块/小功能）要先聊透——见第 0 步 | grill-me | 🔒 一句确认后调 |
| 有决策自己答不了，要让用户/干系人填问卷收集 | to-questionnaire | 🔒 一句确认后调 |
| 聊定了 → 写正式规格 | to-spec | 🔒 一句确认后调 |
| 规格/讨论中理清领域概念：统一术语（GLOSSARY.md）、记架构决策（ADR） | domain-modeling | ✅ 直接调 |
| 规格 → 拆工单 | to-tickets | 🔒 一句确认后调 |
| 超大项目（一个会话装不下）：决策工单化，逐个解决直到路线清晰 | wayfinder | 🔒 一句确认后调 |
| 按规格/工单实现（测试优先） | implement | 🔒 一句确认后调 |
| 新 repo 首次接入这套流程 | setup-matt-pocock-skills | 🔒 确认后跑，会写文件 |
| 长会话交接/换会话 | handoff | 🔒 一句确认后调 |
| 任务/会话结束后复盘整个编码过程 | retro | 🔒 一句确认后调 |
| 审查 diff/分支/PR | code-review | ✅ 直接调 |
| 全库架构审查：扫改进点出 HTML 报告，选中一个深挖 | improve-codebase-architecture | 🔒 一句确认后调 |
| 写 PR 描述 | pr | ✅ 直接调 |
| 难 bug（一眼看不出原因） | diagnosing-bugs | ✅ 直接调 |
| 设计/选型问题需要可运行验证 | prototype | ✅ 直接调 |
| 美化页面/界面、新做 UI、前端视觉方向（含找组件库/设计参考） | frontend-design | ✅ 直接调 |
| 配色/字体/风格选型、UX/可访问性审查、组件与图表规范 | ui-ux-pro-max | ✅ 直接调 |
| 落地页/公司/产品官网从零建或重做，页面被嫌"AI 味/模板脸" | design-taste-frontend（即 tasteskill，leonxlnx） | ✅ 直接调 |
| 交付前 UI 代码审计：按 Vercel Web Interface Guidelines 100+ 条规则出 file:line 报告 | web-design-guidelines（Vercel Labs） | ✅ 直接调 |
| 产品级 UI 精修：对照 80 万+ 真实截图定设计契约，跑 finish gate 后再交付 | anti-ui-slop（UIZZE） | ✅ 直接调 |
| 做动效/找动效机会/动效打磨与性能（该不该动、动什么属性、曲线时长、帧预算、术语定名） | emilkowalski 包：animate / find-animation-opportunities / improve-animations / animation-performance / animation-vocabulary | ✅ 直接调 |
| 交付前动效专项终审（高标准评审，默认挑刺、认可要挣得） | review-animations（emilkowalski） | 🔒 一句确认后调 |
| 真浏览器交互走查/回归测试（模拟点击、滚动、输入并断言行为；与多断点截图配合） | browser-use:web-gui-tester | ✅ 直接调 |
| 静态站部署出预览/分享 URL（手机直接验收、扫码即看） | zcode-site:site-deploy | ✅ 直接调 |
| 推荐好看的 UI / 要设计灵感、参考网站（按页面内容给方向和站点，不动手改） | ui-ux-pro-max（按规则 10 展开） | ✅ 直接调 |
| 需要带引用的背景调研 | research | ✅ 直接调 |
| 写测试 / 红绿重构 | tdd | ✅ 自动生效，无需路由 |

🔒 = SKILL.md 带 `disable-model-invocation: true`，先一句话确认；✅ = 无锁。

## 规则

1. 行动前**读目标 SKILL.md 全文**——上表只做定位，摘要可能过时
2. 意图清晰唯一 → 按表处理。Skill 工具拒绝时：🔒 skill → 请用户输入 `/<名称>`，或直接 Read 本地 SKILL.md 照做（兜底路径，始终可用）；**本地未装/Read 不到 → 明说"该 skill 未安装"，按规则 6 给安装命令或问是否改用相近 skill，不静默失败、不硬造内容**（2026-11-05 测试补）
3. 意图模糊 → 列 2-3 个候选 + 一句话理由让用户选
4. 主流程边界主动建议下一步（grill-me → to-spec → to-tickets → implement → code-review → pr → retro），不在用户专注时打断；UI 流程同理（frontend-design / ui-ux-pro-max 起手定方向 → design-taste-frontend 做落地页 → 实现阶段动效编排可串 emilkowalski 动画包 → web-design-guidelines / anti-ui-slop 收尾审计 → 多断点截图与交互走查（见 12-⑪）→ site-deploy 出 URL 交付）。**UI 链执行原则（2026-11-06 A/B 测试实证）：skill 只管"皮"（配色/字体/结构语汇），内容密度与功能完备由模型基线负责、不得因 skill 清单削减；多 skill 按阶段串行调用，不同时全载**
5. **表外 skill**（grilling、wayfinder、teach、domain-modeling、ask-matt 等）：不主动路由、不主动安装。ask-matt 的路由职能已由本 skill 取代
6. 用户明确要装新 skill 时才装：`npx skills add <owner/repo> --skill <name> -g -y`（来源见上表括号；装不上=代理没开，提醒用户；或在线读内容照做不落盘）
7. 输出语言跟随用户（默认中文），即使 skill 原文是英文
8. 兜底（2026-11-05 用户定）：请求非琐碎但表中无匹配 → 说明"无匹配 skill，正常直接执行"后继续，不硬套、不再追问
9. 链式编排（2026-11-05 用户定）：请求含多个意图，或用户点名要端到端流程时启用，与规则 4 的单步建议互补——
   - 先分解意图，按流水线排出 skill 执行链（可混合主流程与 UI 流程），每步标注输入与产物
   - 展示整链让用户一次性确认/砍步；链确认后 🔒 skill 视为已放行（Skill 工具仍拒绝时按规则 2 兜底：直接 Read 本地 SKILL.md 照做）
   - 依序执行：每步完成用一行汇报产物（路径/文件名），自动衔接下一步；某步产物为空或失败即停下说明，不硬走完
   - 中途冒出新需求 → 重新排链再继续，不在原地即兴插步骤
10. UI 推荐/灵感（2026-11-05 用户定）："帮我推荐一个好看的 UI / 给点设计灵感 / 找参考网站"类请求，只给方向不动手改（用户要改再走 frontend-design / design-taste-frontend）：
    - 先弄清页面内容：读工作区现有代码/页面；没有就问一句产品类型与受众
    - 调 ui-ux-pro-max 按 style / product / typography / color 域查询，给 2-3 个设计方向（每个一句话理由 + 配色/字体要点）
    - 附参考网站：灵感站 awwwards.com、godly.website、land-book.com、onepagelove.com、mobbin.com（App 界面）、saaslandingpage.com；组件参考 shadcn/ui、Aceternity、Magic UI；有 image-search 工具时可搜真实截图佐证
11. **素材与竞品调研**（UI/产品类动手前必跑，一句话小改可跳过）：素材四源（竞品实站 / GitHub 免费站 / ui-ux-pro-max 风格库 / SVG 插画）+ 配图食材级内嵌——**全文见 references/ui-doctrine.md 规则 11 节**
12. **UI 生成守则**（总纲：素材必寻必用、配图是要素、布局大气高利用率、高保真、高交互、题材动效；缺项即不合格）：子项 ⓪新项目拷问 / ①明亮默认 / ②PM 调研 / ③内容密度 / ④编辑 / ⑤动效 / ⑥转化 / ⑦工程底线 / ⑧交付纪律 / ⑨版式工艺 / ⑩风格推荐（含品牌规范源）/ ⑪验证与交付①-⑧（断点截图·交互走查·dump-dom·部署URL·环境坑·SEO·溢出双验·性能）/ ⑫状态完备性 / 条件增强项（SEO·主题切换·国际化）——**全文与两级交付 Checklist 见 references/ui-doctrine.md，动 UI 前必读**
13. 交互式提问适配（2026-11-06 用户点破）：凡向用户提问、给选项、要确认——包括 grill-me/grilling 的每一轮拷问、规则 3 的候选选择、规则 9 的整链确认、规则 12-⓪ 的新项目拷问——**一律用 AskUserQuestion 弹窗呈现，不贴纯文本问题**。每批 ≤4 题、每题 2-4 选项、推荐项排第一并在标签尾标"（推荐）"、用户自由输入走"Other"；超过 4 题分批弹。grilling 的 markdown 格式只是问题设计规范，交付载体是弹窗。**弹窗未作答≈用户不在场（2026-11-07 用户定）**：原样重发一次，再未答即降级文字推进流程，不反复弹、不建议报 bug。

## 决策记录

全文见 `references/decision-log.md`（2026-11-05 起 17 条，改守则/路由前先查最近条目）。
