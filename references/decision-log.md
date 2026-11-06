# 决策记录（按需加载）

> SKILL.md 只留指针；改动守则/路由表前先查最近条目，避免与旧决策冲突。


- 2026-11-05：grill-me 已覆盖 grill-with-docs 的场景，不再主动用 grill-with-docs
- 2026-11-05：新增 UI 链（frontend-design / ui-ux-pro-max / design-taste-frontend / web-design-guidelines / anti-ui-slop）、兜底（规则 8）、链式编排（规则 9）、UI 推荐（规则 10）；锁定标记已实测核对
- 2026-11-06：路由表补 retro（任务复盘）与 improve-codebase-architecture（架构审查），主流程链延伸到 retro
- 2026-11-06：产品从 0 到 1 链补齐：to-questionnaire（问卷收集）、domain-modeling（领域建模，无锁）、wayfinder（超大项目规划）
- 2026-11-06：A/B 测试实证（A<B<A2）后写入 UI 链执行原则：skill 管皮、基线管内容密度、多 skill 串行不同载
- 2026-11-06：新增第 0 步入口判定（年货网站测试实证）：创建类请求（项目/模块/小功能）先思考讨论再谈实现；UI 链仅用户点名 UI 时进入、动手前仍先沟通方向
- 2026-11-07：接入 emilkowalski/skills（GitHub ★54k，动画向 9 技；效果实证于福市集年货站工单 07——animation-vocabulary 用于动效设计词汇）：路由表加 2 行（✅ 动效包一行 + 🔒 review-animations 终审一行），规则 4 UI 链补"实现阶段可串动画包"；animate-expo（RN 专用）、emil-design-eng、remove-animations 不入表，按需手动 `/名字` 调用
- 2026-11-07：完整流程 v2（用户批）：规则 12 新增 ⑪ 验证与交付（多断点截图 / web-gui-tester 交互走查 / dump-dom 执行兜底 / site-deploy URL 交付）；web-gui-tester 与 site-deploy 入表（实测无锁 ✅）；产品级增强项（SEO/埋点/安全/i18n/暗色）标注"演示跳过、产品必补"。实证：福市集年货站补测 375/768 断点全画通过
- 2026-11-07：web-gui-tester 首跑实证（福市集真 375 走查，4/4 过）：抓出并修复 toTop 按钮 DOM 时序静默失效 bug（脚本先于按钮解析，getElementById 返 null）；三条环境结论入 12-⑪⑤（CLI 最小窗宽假溢出 / IAB 底缘指针死区与长页卡顿 / 字符串存在≠行为绑定）
- 2026-11-07：SEO/分享卡入 12-⑪⑥（用户批）：条件触发（部署公网 URL 且需分享/收录）+ 清单式落地（canonical/og/twitter/JSON-LD/sitemap/hreflang），不装新 skill——清单属基线职责；离线单文件阶段不做，og:image 等部署后再填
- 2026-11-07：溢出检查入 12-⑪⑦（用户批）：双验法=真视口只读几何探测（元素 rect 主判据，防 overflow-clip 下 scrollWidth 失真）+分区截图佐证；福市集全档收官——375/768/1440 三档溢出均为 0px、超宽元素 0 个
- 2026-11-07：状态完备性入 12-⑫（用户补）：异步数据五态必齐（Loading/骨架屏/空态/错误/成功禁用），内联数据免做；补齐 Vercel guidelines 与 anti-ui-slop audit 中 states 检查的守则侧空白
- 2026-11-07：品牌规范源入 12-⑩（用户批，"Design MD Collection"帖实证）：awesome-design-md（★126k）按需取 DESIGN.md 做 grounding + google-labs design.md 格式规范沉淀自有 DESIGN.md；不克隆不装 skill；同帖其余项核验——Impeccable 小众与现有重叠不入、shadcn 已在规则 10、Taste Skill 星数注水已有替代
- 2026-11-07：SVG 插画守则入规则 11④（用户定）：插画位优先成熟 SVG 矢量库（unDraw/Open Doodles/Humaaans/DrawKit/Storyset/papercut 六源已验证），自绘仅兜底，**光栅插画不选**（用户：好坏难判）；素材源升级为"四源"；年货站灯笼保持自绘 SVG（题材定制协调，光栅候选已验货放弃）
- 2026-11-07：SEO 专门 skill 实测入 ⑥ 候选池（用户批，挂候选不预装）：claude-seo（★27k 深度审计）/marketingskills（★59k Corey Haines）/geo-seo（★11.5k AI 搜索向）/open-seo-mcp（★8.9k 需 API）——演示走清单、产品按需装，修正"SEO 无 skill 可装"的旧判断
- 2026-11-07：用户重选更正（前次手机误触）：悬空三项全补——⑪⑧ 性能预算（条件触发 Lighthouse）、⑪① 补真机走查（android/ios 模拟器插件）、规则 13 补弹窗降级（未作答≈不在场：重发一次→文字）；手机适配两项全做：品类导航横滚+渐隐已验（412>360 可滑）、吸底年货篮条落地（与返回顶部错位 76px，12-⑨ 错位条款首次完整落地）

- 2026-11-07：结构重构（用户批 A+B+C+D）：SKILL.md 瘦身（规则 11/12 全文与决策记录搬 references/ 按需加载），新增交付两级 Checklist、工具模板库 assets/templates/（image_pipeline / smoke_test 模板 / overflow_probe）、⑤补交互走查执行配方、⑧挂 axe-core；路由与规则骨架保持完整
- 2026-11-07：主题切换与国际化入「条件增强项」（用户定，产品级可选）：主题=CSS 变量双主题+prefers-color-scheme 跟随+记忆+暗色对比度重查（12-① 默认明亮仍优先）；i18n=文案外置+lang/hreflang/Intl/RTL 逻辑属性；均基线职责不装 skill；埋点/安全维持跳过清单语义
- 2026-11-07：技术选型拷问入册（用户批，references/tech-selection.md + 第 0 步挂钩）：创建类请求在 grill 产品想法后、to-spec 前必过选型轮（形态/前端栈/后端数据/部署/约束矩阵/演示最简栈/复用资产七维）；三铁律=用户点名技术免拷问、结论必入 SPEC Implementation Decisions、单分歧点免弹窗
