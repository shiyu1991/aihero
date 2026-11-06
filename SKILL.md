---
name: aihero
description: Intent router — pick the right skill from a curated set and follow it. Trigger on workflow requests (new idea/feature, sharpen a plan, write a spec, split tickets, implement, code review, PR, hard bug, session handoff, cited research) and UI/visual requests (beautify or restyle a page, build UI, frontend design, pick colors/fonts, recommend a good-looking UI, design inspiration, reference sites). DEFAULT FIRST STOP for any non-trivial request, even vague ones (帮我美化一下 / 做个页面 / 优化一下) — route here; no fit in table → say so and proceed directly. 识别意图 → 选用精选 skill → 按其指示执行。
---

# AI Hero Skills

精选索引：只路由下表所列 skill（本地均已装在 `~/.agents/skills`，ZCode 可直接发现；部分经 `~/.zcode/skills` 软链接可见）。**表外的一律不主动路由**——更多不等于更好；用户点名 `/命令` 时照常支持。

## 路由表

| 意图信号 | Skill | 调用方式 |
|---|---|---|
| 新想法/功能要先聊透 | grill-me | 🔒 一句确认后调 |
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
| 推荐好看的 UI / 要设计灵感、参考网站（按页面内容给方向和站点，不动手改） | ui-ux-pro-max（按规则 10 展开） | ✅ 直接调 |
| 需要带引用的背景调研 | research | ✅ 直接调 |
| 写测试 / 红绿重构 | tdd | ✅ 自动生效，无需路由 |

🔒 = SKILL.md 带 `disable-model-invocation: true`，先一句话确认；✅ = 无锁。

## 规则

1. 行动前**读目标 SKILL.md 全文**——上表只做定位，摘要可能过时
2. 意图清晰唯一 → 按表处理。Skill 工具拒绝时：🔒 skill → 请用户输入 `/<名称>`，或直接 Read 本地 SKILL.md 照做（兜底路径，始终可用）；**本地未装/Read 不到 → 明说"该 skill 未安装"，按规则 6 给安装命令或问是否改用相近 skill，不静默失败、不硬造内容**（2026-11-05 测试补）
3. 意图模糊 → 列 2-3 个候选 + 一句话理由让用户选
4. 主流程边界主动建议下一步（grill-me → to-spec → to-tickets → implement → code-review → pr → retro），不在用户专注时打断；UI 流程同理（**先按规则 11 调研** → frontend-design / ui-ux-pro-max 起手定方向 → design-taste-frontend 做落地页 → web-design-guidelines / anti-ui-slop 收尾审计）。**UI 链执行原则（2026-11-06 A/B 测试实证）：skill 只管"皮"（配色/字体/结构语汇），内容密度与功能完备由模型基线负责、不得因 skill 清单削减；多 skill 按阶段串行调用，不同时全载**
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
11. 素材与竞品调研（2026-11-06 用户定，UI/产品类请求动手前必跑，一句话小改可跳过）：像产品经理一样先调研再创作——
    - 竞品：找 2-3 个该品类头部产品，提炼信息架构与功能清单；用户见过的成熟模式优先于自创
    - 素材：GitHub/开源社区找可复用资产（图标库、数据结构、开源实现），优先 MIT/免费许可，**核查许可并在产物中注明来源**；离线单文件场景下，用真实产品的数据结构组织演示数据（如 Open-Meteo 字段）
    - 产出调研结论（找到了什么/借了什么/为什么）写进产物说明，供用户检验

## 决策记录

- 2026-11-05：grill-me 已覆盖 grill-with-docs 的场景，不再主动用 grill-with-docs
- 2026-11-05：新增 UI 链（frontend-design / ui-ux-pro-max / design-taste-frontend / web-design-guidelines / anti-ui-slop）、兜底（规则 8）、链式编排（规则 9）、UI 推荐（规则 10）；锁定标记已实测核对
- 2026-11-06：路由表补 retro（任务复盘）与 improve-codebase-architecture（架构审查），主流程链延伸到 retro
- 2026-11-06：产品从 0 到 1 链补齐：to-questionnaire（问卷收集）、domain-modeling（领域建模，无锁）、wayfinder（超大项目规划）
- 2026-11-06：A/B 测试实证（A<B<A2）后写入 UI 链执行原则：skill 管皮、基线管内容密度、多 skill 串行不同载
