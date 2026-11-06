# -*- coding: utf-8 -*-
"""冒烟测试模板（福市集 80 断言实战提炼）。

用法：拷到项目根目录改名 smoke_test.py，替换 PAGE 与断言，随工单递增。
运行：python -I smoke_test.py（退出码 0=全过）
纪律：
  1. 只测页面对外契约（DOM 结构/数据标记），不测实现细节
  2. 字符串断言必须配 --dump-dom 渲染节点计数兜底（防 JS 错误静默）
  3. 每张工单交付时递增断言，不让测试落后于功能
"""
import re
import sys
from datetime import datetime
from pathlib import Path

PAGE = Path(__file__).resolve().parent / "index.html"  # ← 改成被测页面

failures = []


def check(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" —— {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(name)


html = PAGE.read_text(encoding="utf-8")

# ── 第一层：页面身份 ─────────────────────────────
check("标题含品牌", "你的品牌" in html.split("</title>")[0])
check("viewport / UTF-8 / lang", 'name="viewport"' in html and 'charset="UTF-8"' in html)

# ── 第二层：区块契约（data-section 逐个断言）────
for sec in ["hero", "footer"]:  # ← 按项目补全
    check(f"data-section={sec}", f'data-section="{sec}"' in html)

# ── 第三层：数据层（数量/字段/图片键）───────────
items = re.findall(r"\['[^']+',\s*[\d.]+", html)  # ← 按数据结构调正则
check("数据条数达标", len(items) >= 40, f"实际 {len(items)}")
check("图片显式尺寸", 'width="' in html)

# ── 第四层：动效与降级 ──────────────────────────
check("prefers-reduced-motion 存在", "prefers-reduced-motion: reduce" in html)
check("动效引擎存在", "IntersectionObserver" in html)

# ── 第五层：无障碍与工程 ────────────────────────
check("跳转链接", "skip-link" in html)
check("无外部资源（离线单文件）", not re.findall(r'(?:src|href)="https?://', html))

print()
if failures:
    print(f"结果：{len(failures)} 项失败 -> {failures}")
    sys.exit(1)
print("结果：全部通过")
