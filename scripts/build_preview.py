# /// script
# dependencies = ["markdown-it-py==3.0.0", "nh3==0.2.21"]
# ///
"""从磁盘 README 生成本地近似预览；不修改 README 或视觉素材。"""
from pathlib import Path
from hashlib import sha256
from markdown_it import MarkdownIt
import nh3

ROOT = Path(__file__).resolve().parents[1]

def render_markdown(source):
    """将 Markdown 转为安全 HTML，保留图片和主题资源；不模拟 GitHub 的全部过滤规则。"""
    html = MarkdownIt("commonmark", {"html": True}).enable("table").render(source)
    tags = set(nh3.ALLOWED_TAGS) | {"picture", "source"}
    attributes = {key: set(value) for key, value in nh3.ALLOWED_ATTRIBUTES.items()}
    attributes["img"] = {"src", "alt", "title", "width", "height"}
    attributes["source"] = {"srcset", "media", "type"}
    return nh3.clean(html, tags=tags, attributes=attributes)

def build():
    """读取当前 README，以项目根为资源基准生成预览；返回源文件摘要。"""
    source = (ROOT / "README_.md").read_text(encoding="utf-8")
    digest = sha256(source.encode()).hexdigest()
    content = render_markdown(source)
    page = f'''<!doctype html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<base href="../">
<meta name="readme-sha256" content="{digest}">
<title>README · GitHub 样式预览</title>
<link rel="icon" href="data:,">
<link id="markdown-theme" rel="stylesheet" href="demo/vendor/github-markdown-light.css">
<link rel="stylesheet" href="demo/style.css">
<script src="demo/preview.js" defer></script>
</head>
<body>
<header class="preview-toolbar">
<strong>README 预览</strong>
<nav aria-label="本地预览设置">
<button id="theme-toggle" type="button" aria-pressed="false">深色预览</button>
<button id="width-toggle" type="button" aria-pressed="false">窄屏预览</button>
<a href="README_.md">查看源文件</a>
</nav>
<p>直接渲染 README_.md · GitHub 样式近似 · 不含个人主页侧栏</p>
</header>
<main id="preview-frame">
<div class="file-label">README_.md</div>
<article class="markdown-body" id="readme-content">
{content}
</article>
</main>
<p class="preview-note">上方按钮仅用于本地审阅。最终效果以 GitHub 实际渲染为准。</p>
</body>
</html>'''
    (ROOT / "demo/index.html").write_text(page, encoding="utf-8")
    return digest

if __name__ == "__main__":
    print("README preview generated: " + build())
