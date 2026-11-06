# aihero 路由 skill 测试报告（2026-11-05）

环境：ZCode / Windows / Git Bash。原则：不改任何第三方 skill 内容；aihero 为自有 skill，测试发现的缺口直接修补。
测试标的：`index.html`（无样式落地页，供后续真实美化测试用）；`sim/aihero-sim/`（含不存在 skill 引用的路由表副本）。

## T1 路由表完整性：表内 skill 本地是否都存在

- 方法：解析 SKILL.md 路由表的 Skill 列，逐一检查 `~/.agents/skills` 与 `~/.zcode/skills`
- 结果：**17/17 全部 EXISTS** ✅
- 插曲：首跑全部误报 MISSING，根因是 SKILL.md 为 CRLF 行尾，grep 提取的名字尾部带 `\r`——测试脚本 bug，非 skill 问题

## T2 Skill 工具调用路径（本会话中途新装的 skill）

- 方法：直接 `Skill(design-taste-frontend)`（该 skill 在本会话开始后才安装）
- 结果：**✅ 成功加载全文**，经 `~/.zcode/skills/design-taste-frontend` 符号链接（npx 安装器自动创建）
- 结论：新装 skill 不必等下个会话，安装器已同步建好 .zcode 侧链接

## T3 引用不存在的 skill 时怎么办（核心测试）

- 场景：路由表指向 `super-designer-pro`（本地不存在）
- 实测链路：
  1. Skill 工具调用 → 拒绝（不在会话技能列表）
  2. 规则 2 兜底：Read `~/.agents/skills/super-designer-pro/SKILL.md` → **File does not exist**
- 原规则覆盖：规则 2 只写了"🔒 被拒 → 用户敲 `/命令` 或 Read 兜底"；规则 8 只写了"表中无匹配"。**"表中有匹配但本地未装"两条都不覆盖 → 缺口**
- 修补（已应用到 aihero 规则 2）：本地未装/Read 不到 → 明说"该 skill 未安装"，按规则 6 给安装命令或问是否改用相近 skill，**不静默失败、不硬造内容**

## T4 路由推演（按 SKILL.md 逻辑推演，未实际执行）

| 用户说 | 预期路由 | 依据 |
|---|---|---|
| 帮我美化这个页面 | frontend-design ✅ 直调 | 表行"美化页面/界面" |
| 帮我推荐一个好看的 UI | 规则 10：ui-ux-pro-max 查方向 + 参考站清单 | 表行"推荐好看的 UI" |
| 这个 bug 查了半天没头绪 | diagnosing-bugs ✅ | 表行"难 bug" |
| 我有个新想法：做个 xxx | grill-me 🔒 先一句确认再调 | 表行"新想法" |
| 做个落地页再帮我审一下 | 规则 9 排链：design-taste-frontend → web-design-guidelines | 多意图触发链式编排 |
| 现在几点了 | 跳过路由（琐碎请求） | 全局 AGENTS.md 约定 |

## 结论

1. 路由表 17 个目标全部可解析、本地齐全；✅ 直调路径实测可用
2. 发现并修补 1 个行为缺口（引用未装 skill：明确报未装 + 给安装命令，不硬造）
3. 全程未改动任何第三方 skill 内容
4. 待办：aihero 改动（规则 2 增补）尚未推送 GitHub
