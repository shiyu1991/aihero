# -*- coding: utf-8 -*-
"""福市集配图管线（工单 03）：download / optimize / inject 三段式。

用法（均以 -I 隔离运行，路径作参数传入）：
  python -I image_pipeline.py download  <manifest.json> <raw_dir>
  python -I image_pipeline.py optimize  <raw_dir> <out_dir> <hero_dir_list...>
  python -I image_pipeline.py inject    <html_path> <out_dir>

manifest.json 结构：{"key": {"url": ..., "source": ..., "role": "hero|cover|product|story"}, ...}
optimize 规则：hero/cover 宽 960 q60；product/story 宽 480 q52；输出 JPEG；报告总体积与预算。
inject 规则：把 html 中 {{IMG:key}} 替换为 data URI（图片数据不经模型上下文）。
"""
import base64
import json
import mimetypes
import sys
import urllib.request
from pathlib import Path

BUDGET_BYTES = 600 * 1024  # 二进制总量预算（base64 后约 800KB）


def cmd_download(manifest_path: str, raw_dir: str):
    raw = Path(raw_dir)
    raw.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    ok, fail = [], []
    for key, meta in manifest.items():
        url = meta["url"]
        ext = Path(url.split("?")[0]).suffix or ".jpg"
        dest = raw / f"{key}{ext}"
        if dest.exists() and dest.stat().st_size > 1000:
            ok.append((key, dest.stat().st_size, "cached"))
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            if len(data) < 2000:
                raise ValueError(f"too small: {len(data)}B")
            dest.write_bytes(data)
            ok.append((key, len(data), "new"))
        except Exception as e:  # noqa: BLE001
            fail.append((key, str(e)[:80]))
    for key, size, state in ok:
        print(f"  OK  {key:<12} {size:>8}B {state}")
    for key, err in fail:
        print(f"  FAIL {key:<12} {err}")
    print(f"下载完成：成功 {len(ok)} / 失败 {len(fail)}")
    return 1 if fail else 0


def cmd_optimize(raw_dir: str, out_dir: str):
    from PIL import Image  # 延迟导入，仅 optimize 需要

    src, dst = Path(raw_dir), Path(out_dir)
    dst.mkdir(parents=True, exist_ok=True)
    total = 0
    report = []
    for f in sorted(src.iterdir()):
        if f.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
            continue
        key = f.stem
        role = "hero" if key.startswith(("hero", "cover")) else "product"
        max_w = 720 if role == "hero" else 320
        quality = 52 if role == "hero" else 45
        try:
            im = Image.open(f)
            im.load()
            if im.mode in ("RGBA", "P", "LA"):
                bg = Image.new("RGB", im.size, (255, 255, 255))
                im = im.convert("RGBA")
                bg.paste(im, mask=im.split()[-1])
                im = bg
            elif im.mode != "RGB":
                im = im.convert("RGB")
            if im.width > max_w:
                im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
            dest = dst / f"{key}.jpg"
            im.save(dest, "JPEG", quality=quality, optimize=True, progressive=True)
            size = dest.stat().st_size
            total += size
            report.append((key, im.width, im.height, size))
        except Exception as e:  # noqa: BLE001
            print(f"  FAIL {key}: {e}")
    for key, w, h, size in report:
        print(f"  {key:<14} {w}x{h:<5} {size:>7}B")
    print(f"优化完成：{len(report)} 张，合计 {total}B ({total/1024:.0f}KB) / 预算 {BUDGET_BYTES//1024}KB")
    (dst / "_total.txt").write_text(str(total), encoding="utf-8")
    return 0 if total <= BUDGET_BYTES else 2


def cmd_inject(html_path: str, out_dir: str):
    """把优化图打包成 IMG_DATA 映射注入 /*__IMG_DATA__*/ 占位（幂等：已注入则跳过）。"""
    page = Path(html_path)
    html = page.read_text(encoding="utf-8")
    token = "/*__IMG_DATA__*/"
    if token not in html:
        print("注入跳过：占位符不存在（可能已注入）")
        return 0
    dst = Path(out_dir)
    entries = []
    total = 0
    for f in sorted(dst.glob("*.jpg")):
        uri = "data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode("ascii")
        entries.append(f'"{f.stem}":"{uri}"')
        total += f.stat().st_size
    js = "var IMG_DATA = {" + ",".join(entries) + "};"
    html = html.replace(token, js)
    page.write_text(html, encoding="utf-8")
    print(f"注入完成：IMG_DATA 含 {len(entries)} 张图，数据体积 {total/1024:.0f}KB")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(64)
    cmd, args = sys.argv[1], sys.argv[2:]
    sys.exit(globals()[f"cmd_{cmd}"](*args))
