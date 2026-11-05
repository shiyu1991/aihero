---
name: aihero
description: Identify the user's intent, pick the relevant skill from a curated high-quality set, and follow its instructions. Trigger on workflow-shaped requests — new idea or feature, sharpen a plan, write a spec, split tickets, implement, review code, write a PR, debug a hard bug, handoff a session, cited research, throwaway prototype — AND on UI/visual requests (beautify or restyle a page, build UI, frontend design, pick colors/fonts/styles, recommend a good-looking UI, find design inspiration or reference sites). Also the DEFAULT FIRST STOP for any non-trivial work request, even vague or casual ones (帮我美化一下 / 做个页面 / 优化一下) with no matching keyword: invoke aihero to route; if nothing in the table fits, say so and proceed directly. 识别意图 → 选用精选 skill → 按其指示执行。
---

# AI Hero Skills

精选索引：只路由下表所列 skill（本地均已装在 `~/.agents/skills`，ZCode 可直接发现；部分经 `~/.zcode/skills` 软链接可见）。**表外的一律不主动路由**——更多不等于更好；用户点名 `/命令` 时照常支持。

## 路由表

| 意图信号 | Skill | 调用方式 |
|---|---|---|
| 新想法/功能要先聊透（一律用 grill-me，2026-11-05 用户定：grill-me 已覆盖 grill-with-docs 的场景，不再主动用 grill-with-docs） | grill-me | 🔒 一句确认后调 |
| 聊定了 → 写正式规格 | to-spec | 🔒 一句确认后调 |
| 规格 → 拆工单 | to-tickets | 🔒 一句确认后调 |
| 按规格/工单实现（测试优先） | implement | 🔒 一句确认后调 |
| 新 repo 首次接入这套流程 | setup-matt-pocock-skills | 🔒 确认后跑，会写文件 |
| 长会话交接/换会话 | handoff | 🔒 一句确认后调 |
| 审查 diff/分支/PR | code-review | ✅ 直接调 |
| 写 PR 描述 | pr | ✅ 直接调 |
| 难 bug（一眼看不出原因） | diagnosing-bugs | ✅ 直接调 |
| 设计/选型问题需要可运行验证 | prototype | ✅ 直接调 |
| 美化页面/界面、新做 UI、前端视觉方向（含找组件库/设计参考） | frontend-design | ✅ 直接调 |
| 配色/字体/风格选型、UX/可访问性审查、组件与图表规范 | ui-ux-pro-max | ✅ 直接调 |
| 落地页/公司/产品官网从零建或重做，页面被嫌"AI 味/模板脸" | design-taste-frontend（即 tasteskill 2.5.0，leonxlnx） | ✅ 直接调 |
| 交付前 UI 代码审计：按 Vercel Web Interface Guidelines 100+ 条规则出 file:line 报告 | web-design-guidelines（Vercel Labs） | ✅ 直接调 |
| 产品级 UI 精修：对照 80 万+ 真实截图定设计契约，跑 finish gate 后再交付 | anti-ui-slop（UIZZE） | ✅ 直接调 |
| 推荐好看的 UI / 要设计灵感、参考网站（按页面内容给方向和站点，不动手改） | ui-ux-pro-max（按规则 10 展开） | ✅ 直接调 |
| 需要带引用的背景调研 | research | ✅ 直接调 |
| 写测试 / 红绿重构 | tdd | ✅ 自动生效，无需路由 |

🔒 = SKILL.md 带 `disable-model-invocation: true`，先一句话确认；✅ = 无锁。

## 规则

1. 行动前**读目标 SKILL.md 全文**——上表只做定位，摘要可能过时
2. 意图清晰唯一 → 按表处理；Skill 工具拒绝 🔒 skill 时请用户输入 `/<名称>`，或直接 Read 本地 SKILL.md 照做（兜底路径，始终可用）
3. 意图模糊 → 列 2-3 个候选 + 一句话理由让用户选
4. 主流程边界主动建议下一步（grill-me → to-spec → to-tickets → implement → code-review → pr），不在用户专注时打断；UI 流程同理（frontend-design / ui-ux-pro-max 起手定方向 → design-taste-frontend 做落地页 → web-design-guidelines / anti-ui-slop 收尾审计）
5. **表外 skill**（grilling、wayfinder、teach、domain-modeling、ask-matt 等）：不主动路由、不主动安装。ask-matt 的路由职能已由本 skill 取代
6. 用户明确要装新 skill 时才装：`npx skills add mattpocock/skills --skill <name> -g -y`（装不上=代理没开，提醒用户；或在线读内容照做不落盘）
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
