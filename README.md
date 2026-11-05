# aihero

Agent skill 路由器：识别意图 → 从精选的高质量本地 skill 中选一个 → 按其指示执行。适用于 ZCode / Claude Code / Codex 等支持 SKILL.md 的 agent。

## 特性

- **主流程链**：grill-me → to-spec → to-tickets → implement → code-review → pr
- **UI 链**：frontend-design / ui-ux-pro-max（定方向）→ design-taste-frontend（落地页）→ web-design-guidelines / anti-ui-slop（收尾审计）
- **UI 推荐/灵感**：按页面内容给 2-3 个设计方向 + 参考网站，只推荐不动手
- **链式编排**：多意图请求先排整条 skill 执行链，一次确认后依序自动执行
- **兜底**：无匹配 skill 时说明一句后直接正常执行，不硬套

## 安装

```bash
npx skills add shiyu1991/aihero -g -y
```

## 依赖

路由目标 skill 需另行安装，见 SKILL.md 路由表：mattpocock/skills（grill-me、to-spec、implement 等）、anthropics/skills（frontend-design）、nextlevelbuilder/ui-ux-pro-max-skill、leonxlnx/taste-skill、vercel-labs/agent-skills、github/awesome-copilot（anti-ui-slop）。
