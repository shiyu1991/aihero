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
4. 主流程边界主动建议下一步（grill-me → to-spec → to-tickets → implement → code-review → pr → retro），不在用户专注时打断；UI 流程同理（frontend-design / ui-ux-pro-max 起手定方向 → design-taste-frontend 做落地页 → web-design-guidelines / anti-ui-slop 收尾审计）。**UI 链执行原则（2026-11-06 A/B 测试实证）：skill 只管"皮"（配色/字体/结构语汇），内容密度与功能完备由模型基线负责、不得因 skill 清单削减；多 skill 按阶段串行调用，不同时全载**
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
    - **素材三源，必须真寻、真参考、真使用（只看不用于不算）**：①竞品实站（>UI 画廊，人家已打磨完善；用画廊必须进其品类相关内容页，不做关键词泛查）②GitHub 等免费站（UI 组件/图标/插画/模板库，MIT/免费许可优先）③ui-ux-pro-max 风格库
    - **配图是食材级要素（2026-11-06 西餐厅页教训）：离线单文件也必须内嵌真实图像——image-search 找图 → 下载 → PIL 压缩（宽≤960、q≈52、总≤800KB）→ base64 data-URI 注入（占位符+脚本替换，不经上下文）；"零外部依赖"不是无图借口**；图片来源与许可写进页脚铭牌
    - 离线单文件场景下，用真实产品的数据结构组织演示数据；**内容与动效趋势都要调研**（动效优先 hero、滚动编排、微交互、材质层次）
12. UI 生成守则（2026-11-06 多轮 A/B 实证后用户定总纲：**素材必寻必用（UI 素材/竞品实站/GitHub 免费库）、配图是要素、布局实用美观大气（高空间利用率，拒绝挤压、层叠、超出无法滚动）、高保真、高交互体验、符合场景的动效/插图/背景/配图。UI/产品任务在拆解（规则 9 或单任务）时必须整体注入，逐项对照执行，缺项即不合格**）：
    - ① 风格判断：工具/信息类页面走品类正统（用户期待 > 新颖，如天气页就要天空渐变+毛玻璃+大温度）；品牌/门面类页面才追求差异化。**配色基调默认开朗光明（2026-11-06 用户定，依人的心理喜好）：整体主题尽可能选明亮底色，不做阴暗选择；深色仅在用户点名要求、或题材强需求（如夜间酒吧/恐怖题材）时采用，且须在交付说明里讲清为什么用深色；深色可以作局部点缀（照片节/页脚/对比带），不当整页基调**
    - ② PM 调研（规则 11 三源素材 + 配图）
    - ③ 内容密度与高保真：信息饱满、题材专属素材、真实数据质感（细节完整可推敲）；"安静"指装饰克制 ≠ 内容单薄
    - ④ 编辑：去重合并，不平行罗列
    - ⑤ 动效与交互（执行深度 = 高级感，**无动效直接判不合格**）：入场编排、滚动错峰、背景氛围动效（雨/云/光粒子按题材）、数字滚动、条形生长、路径描边、悬停微交互、动效回答操作、可点击组件（灯箱/展开/切换）
    - ⑥ 转化机制（有行动目标时）：倒计时/余量/信任标记
    - ⑦ 工程底线：reduced-motion 全覆盖、动态内容容器定高防 CLS、审计清单过一遍
    - ⑧ 交付纪律：改被批评的**原文件**（用户刷新即见），不写新文件名；skill/规则改动须用户认可效果后再入库推送
    - ⑨ 版式工艺：**拒绝挤压**（窄屏断点降列不压扁、文字不硬折行）；**拒绝错误层叠**（装饰不盖信息、高亮不遮数据）；**拒绝超出无法滚动**（横向内容必须可滚或有断点收纳）；贴边要有暗示（横滑区渐隐提示）；滚动决策（关键信息吸顶随行）；**高空间利用率**（宽屏并排减竖向占用）
    - ⑩ 风格分类推荐（2026-11-06 用户补）：动手前从需求分析风格分类——用 ui-ux-pro-max 风格库检索（查询词=品类+平台+气质，2~5 词，一种主导意图；如"weather consumer app glass translucent"→Liquid Glass/Apple 系），**给用户看：推荐风格+一句理由+2 个备选，且每条必须附至少一个可打开的参考地址**（官方规范优先，其次案例画廊）；用户点名风格时绝对优先；检索不中就明说"无验证命中"再给通用建议，不硬凑。注意：查询词决定命中质量（"apple ios minimal"会带偏去瑞士极简，"glass translucent"才命中 Apple Liquid Glass）
      - 参考地址锚点（已验证可达；无映射时现场搜索验证再给，找不到就明说）：Liquid Glass/Apple 系→ developer.apple.com/design/human-interface-guidelines/materials；Brutalism→ brutalistwebsites.com；Bento Grid→ bento.me；通用灵感→ godly.website / awwwards.com / land-book.com / mobbin.com（App 界面）

## 决策记录

- 2026-11-05：grill-me 已覆盖 grill-with-docs 的场景，不再主动用 grill-with-docs
- 2026-11-05：新增 UI 链（frontend-design / ui-ux-pro-max / design-taste-frontend / web-design-guidelines / anti-ui-slop）、兜底（规则 8）、链式编排（规则 9）、UI 推荐（规则 10）；锁定标记已实测核对
- 2026-11-06：路由表补 retro（任务复盘）与 improve-codebase-architecture（架构审查），主流程链延伸到 retro
- 2026-11-06：产品从 0 到 1 链补齐：to-questionnaire（问卷收集）、domain-modeling（领域建模，无锁）、wayfinder（超大项目规划）
- 2026-11-06：A/B 测试实证（A<B<A2）后写入 UI 链执行原则：skill 管皮、基线管内容密度、多 skill 串行不同载
