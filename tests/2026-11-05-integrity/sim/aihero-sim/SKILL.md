---
name: aihero-sim
description: 测试用副本，结构同 aihero，仅用于验证"路由表引用了不存在的 skill"时的行为。不供日常使用。
---

# aihero-sim（测试副本）

## 路由表

| 意图信号 | Skill | 调用方式 |
|---|---|---|
| 帮我做个高级设计 | super-designer-pro（本地不存在，用于测试） | ✅ 直接调 |
| 美化页面 | frontend-design（本地存在，对照组） | ✅ 直接调 |

## 规则（摘自 aihero）

1. 行动前**读目标 SKILL.md 全文**
2. 意图清晰唯一 → 按表处理；Skill 工具拒绝 🔒 skill 时请用户输入 `/<名称>`，或直接 Read 本地 SKILL.md 照做（兜底路径，始终可用）
6. 用户明确要装新 skill 时才装：`npx skills add <owner/repo> --skill <name> -g -y`
8. 兜底：请求非琐碎但表中无匹配 → 说明"无匹配 skill，正常直接执行"后继续，不硬套、不再追问
