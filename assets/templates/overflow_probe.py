# -*- coding: utf-8 -*-
"""溢出探测模板（CLI 版，福市集 ⑪⑦ 实战提炼）。

原理：复制被测页 → 副本注入只读检测脚本（结果写 DOM 属性）→ headless 逐档加载 → dump-dom 读报告。
限制：CLI --window-size 有 ~500px 最小窗宽钳制，**<500px 档会得到假结果**，脚本会警告并跳过——
     手机断点必须走浏览器自动化 setViewportSize（web-gui-tester）。

用法：python -I overflow_probe.py <html_path> [宽度列表，默认 768 1440]
"""
import re
import subprocess
import sys
import tempfile
import urllib.parse
from pathlib import Path

PROBE_JS = """<script>
(function(){
  function probe(){
    try{
      var vw=document.documentElement.clientWidth;
      var bad=[];
      var els=document.querySelectorAll('body *');
      for(var i=0;i<els.length;i++){
        var r=els[i].getBoundingClientRect();
        if(r.width>0 && r.right>vw+1){
          var c=(els[i].className&&els[i].className.toString)?els[i].className.toString().slice(0,40):'';
          bad.push(els[i].tagName+'.'+c+'|right='+Math.round(r.right)+'|w='+Math.round(r.width));
          if(bad.length>=15){break;}
        }
      }
      var m=document.createElement('div');
      m.id='__ovf';
      m.setAttribute('data-vw',vw);
      m.setAttribute('data-sw',document.documentElement.scrollWidth);
      m.setAttribute('data-bad',encodeURIComponent(bad.join(' ;; ')));
      document.body.appendChild(m);
    }catch(e){}
  }
  if(document.readyState==='complete'){probe();}
  else{window.addEventListener('load',probe);}
})();
</script></head>"""

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(64)
    page = Path(sys.argv[1]).resolve()
    widths = [int(w) for w in sys.argv[2:]] or [768, 1440]
    chrome = next((c for c in CHROME_CANDIDATES if Path(c).exists()), None)
    if not chrome:
        print("未找到 Chrome/Edge，探测不可用")
        sys.exit(65)

    src = page.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as td:
        probe_path = Path(td) / "probe.html"
        probe_path.write_text(src.replace("</head>", PROBE_JS, 1), encoding="utf-8")
        url = probe_path.as_uri()
        exit_code = 0
        for w in widths:
            if w < 500:
                print(f"[{w}px] ⚠️ 低于 CLI 最小窗宽（~500px 钳制），结果不可信——请改走浏览器自动化 setViewportSize")
                exit_code = 2
                continue
            r = subprocess.run(
                [chrome, "--headless=new", "--disable-gpu", "--window-size=" + str(w) + ",900",
                 "--virtual-time-budget=8000", "--dump-dom", url],
                capture_output=True, timeout=120)
            d = r.stdout.decode("utf-8", "ignore")
            m = re.search(r'<div id="__ovf" data-vw="(\d+)" data-sw="(\d+)" data-bad="([^"]*)"', d)
            if not m:
                print(f"[{w}px] 探测失败（__ovf 未出现）")
                exit_code = 1
                continue
            vw, sw = int(m.group(1)), int(m.group(2))
            print(f"[{w}px] vw={vw} sw={sw} 溢出={sw - vw}px")
            for it in urllib.parse.unquote(m.group(3)).split(" ;; "):
                if it.strip():
                    print("   超宽:", it)
                    exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
