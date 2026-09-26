"""生成 GitHub 主页演示资源；无需第三方依赖，输出覆盖本脚本管理的文件。"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
INTRO = "我是一只奶茶鼠，也是一位气象学家。关注数值天气预报、气候模拟与高性能计算，也开发服务科研与日常生活的应用。"
GROUPS = [
    ("Atmospheric Science", "从大气过程到数值模拟", "数值天气预报 · 气候数值模拟 · 科学计算", []),
    ("Computing", "把想法写进计算", "通用分析、高性能算法与数值模式开发。", [("Python", "Py", "#4798cf"), ("C++", "C+", "#688bda"), ("Fortran", "F", "#aa83cf"), ("uv", "uv", "#a472de")]),
    ("Agent Stack", "与智能工具一起构建", "让工具参与探索，把判断留给自己。", [("Codex", ">_", "#51a69a")]),
    ("Developer Tools", "从研究工具到日常应用", "在 Linux / WSL 中开发，用版本控制保留思考轨迹。", [("VS Code", "</>", "#4798cf"), ("Git", "git", "#d27f61"), ("Linux", "sh", "#b69a62"), ("WSL", "~", "#639b93"), ("React", "R", "#539dab"), ("TypeScript", "TS", "#548cc1"), ("FastAPI", "Fa", "#489a88"), ("Tauri", "T", "#b58b58")]),
]
PALETTES = {
    "light": dict(bg="#f1f6f4", fg="#193b3d", muted="#567371", line="#b9d0c8", accent="#27786f", cell="#e0eae5"),
    "dark": dict(bg="#14262d", fg="#e2eee7", muted="#a0bcb6", line="#33564f", accent="#7bd3b4", cell="#243e43"),
}

def write(path, text):
    """输入相对路径和文本，创建父目录并以 UTF-8 写出；无返回值。"""
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")

def svg(width, height, body, title):
    """输入画布尺寸、内容和可访问标题，返回独立 SVG 字符串。"""
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><g font-family="Arial, Helvetica, sans-serif">{body}</g></svg>'

def banner(theme):
    """输入主题，返回装饰性气象 Banner；线条不表示真实气象观测。"""
    p = PALETTES[theme]
    contours = []
    for i in range(12):
        rx, ry = 42 + i * 24, 26 + i * 14
        contours.append(f'<ellipse cx="784" cy="145" rx="{rx}" ry="{ry}" transform="rotate(-28 784 145)" fill="none" stroke="{p["accent"]}" stroke-opacity="{0.56-i*0.032:.3f}" stroke-width="1"/>')
    grid = ''.join(f'<path d="M{x} 0V320" stroke="{p["line"]}" opacity=".15"/>' for x in range(0,1001,40))
    grid += ''.join(f'<path d="M0 {y}H1000" stroke="{p["line"]}" opacity=".15"/>' for y in range(0,321,40))
    body = f'<defs><linearGradient id="wash"><stop stop-color="{p["bg"]}"/><stop offset="1" stop-color="{p["bg"]}" stop-opacity=".85"/></linearGradient><clipPath id="edge"><rect width="1000" height="320" rx="12"/></clipPath></defs><g clip-path="url(#edge)"><rect width="1000" height="320" fill="{p["bg"]}"/>{grid}{"".join(contours)}<rect width="590" height="320" fill="url(#wash)"/><path d="M690 294 Q690 230 745 209T850 142T942 57" fill="none" stroke="{p["accent"]}" stroke-width="2" stroke-dasharray="3 8"/><circle cx="786" cy="146" r="5" fill="{p["accent"]}"/><circle cx="786" cy="146" r="13" fill="none" stroke="{p["accent"]}" opacity=".6"/><text x="809" y="149" fill="{p["muted"]}" font-size="11" letter-spacing="2">EXPLORE</text><text x="40" y="44" fill="{p["accent"]}" font-size="11" letter-spacing="2.2">ATMOSPHERIC SCIENCE / SOFTWARE ENGINEERING</text><text x="38" y="124" fill="{p["fg"]}" font-size="51" font-weight="700" letter-spacing="-2">Reading the sky.</text><text x="38" y="182" fill="{p["fg"]}" font-size="51" font-weight="700" letter-spacing="-2">Writing the code.</text><path d="M40 223H77" stroke="{p["accent"]}" stroke-width="2"/><text x="40" y="267" fill="{p["muted"]}" font-size="13" letter-spacing="1">CURIOSITY, FROM ATMOSPHERE TO ALGORITHMS.</text><text x="947" y="294" text-anchor="end" fill="{p["muted"]}" font-size="10" letter-spacing="2">FIELD NOTES / 01</text></g>'
    return svg(1000, 320, body, "Reading the sky. Writing the code. Decorative atmospheric contours.")

def badge(label, symbol, color):
    """输入标签、缩写和强调色，返回跨主题可读的统一徽章。"""
    width = max(88, len(label)*8+58)
    return svg(width, 34, f'<rect x=".5" y=".5" width="{width-1}" height="33" rx="6" fill="#172830" stroke="#3b5058"/><rect x="8" y="8" width="22" height="18" rx="4" fill="{color}" fill-opacity=".18"/><text x="19" y="21" text-anchor="middle" font-size="10" font-weight="700" fill="{color}">{escape(symbol)}</text><text x="39" y="22" font-size="12" fill="#edf3ef">{escape(label)}</text>', label)

def stats(theme):
    """输入主题，返回无真实数值的统计占位卡片，避免虚构账号表现。"""
    p = PALETTES[theme]
    body = f'<rect x=".5" y=".5" width="999" height="145" rx="10" fill="{p["bg"]}" stroke="{p["line"]}"/>'
    for index, name in enumerate(["PUBLIC REPOSITORIES", "TOTAL STARS", "CONTRIBUTIONS"]):
        x = 30 + index*330
        body += f'<text x="{x}" y="33" font-size="11" letter-spacing="1.5" fill="{p["muted"]}">{name}</text><text x="{x}" y="81" font-size="36" fill="{p["fg"]}">—</text><text x="{x}" y="118" font-size="12" fill="{p["muted"]}">CONNECT ACCOUNT TO DISPLAY</text>'
        if index:
            body += f'<path d="M{x-20} 27V119" stroke="{p["line"]}"/>'
    return svg(1000,146,body,"GitHub Stats demo. Account not connected. No actual statistics.")

def snake(theme):
    """输入主题，返回确定性的示例网格与静态蛇形装饰；不读取账号数据。"""
    p=PALETTES[theme]
    colors=[p["cell"], "#346e63", "#478f78", "#70b899", "#a0d3b2"]
    body=f'<rect x=".5" y=".5" width="999" height="221" rx="10" fill="{p["bg"]}" stroke="{p["line"]}"/><text x="28" y="30" font-size="11" letter-spacing="1.8" fill="{p["muted"]}">CONTRIBUTION LANDSCAPE</text><text x="972" y="30" text-anchor="end" font-size="10" letter-spacing="1" fill="{p["muted"]}">SAMPLE GRID / NOT ACCOUNT DATA</text>'
    for col in range(52):
        for row in range(7):
            value = (col*17+row*31+col*row) % 19
            level = 0 if value < 10 else (value % 4)+1
            body+=f'<rect x="{32+col*18}" y="{52+row*18}" width="13" height="13" rx="2" fill="{colors[level]}"/>'
    body+=f'<path d="M475 166H565Q578 166 578 152V128Q578 115 592 115H660Q674 115 674 101V80Q674 65 687 65H731" fill="none" stroke="{p["bg"]}" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/><path d="M475 166H565Q578 166 578 152V128Q578 115 592 115H660Q674 115 674 101V80Q674 65 687 65H731" fill="none" stroke="{p["accent"]}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><circle cx="731" cy="65" r="7" fill="{p["accent"]}"/><circle cx="734" cy="63" r="1.7" fill="{p["bg"]}"/><text x="28" y="202" font-size="11" fill="{p["muted"]}">Small steps. Lasting traces.</text><text x="972" y="202" text-anchor="end" font-size="10" fill="{p["muted"]}">STATIC PREVIEW</text>'
    return svg(1000,222,body,"Static contribution snake demo with synthetic sample cells, not real account activity.")

def slug(label):
    """输入工具名称，返回可移植的资源文件名。"""
    return label.lower().replace("++","pp").replace(" ","-")

def picture(name, alt):
    """输入资源名和替代文字，返回 GitHub README 可使用的主题图片片段。"""
    return f'<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="assets/{name}-dark.svg">\n  <img src="assets/{name}-light.svg" alt="{alt}" width="100%">\n</picture>'

def build():
    """生成主题资源、徽章与 README；无输入与返回值。"""
    for theme in PALETTES:
        for name, fn in [("banner",banner),("stats",stats),("snake",snake)]:
            write(f"assets/{name}-{theme}.svg",fn(theme))
    md=[picture("banner","Reading the sky. Writing the code. 气象主题装饰图"),"","# 奶茶鼠","","**Atmospheric Scientist & Developer**","",INTRO,"","---"]
    for name, subtitle, description, tools in GROUPS:
        badges=[]
        for label,symbol,color in tools:
            path=f"assets/badges/{slug(label)}.svg"
            write(path,badge(label,symbol,color))
            badges.append(f'<img src="{path}" alt="{escape(label)}" height="34">')
        md+=["",f"## {name}","",description,""]
        if badges:
            md+=['<p>\n'+'\n'.join(badges)+'\n</p>']
    md+=["","## GitHub Stats","","演示占位，尚未连接 GitHub 账号。","",picture("stats","统计卡片演示：尚未连接账号，无真实数值。"),"","## Contribution Snake","","示例网格与静态贪吃蛇，仅用于查看风格，不代表真实贡献记录。","",picture("snake","贡献图静态演示：合成示例数据，不代表真实贡献记录。"),"","---","","<sub>主页风格 Demo · 文案与工具清单待最终确认</sub>",""]
    write("README_.md","\n".join(md))
    print("资源与 README 草稿已生成；请另行运行 build_preview.py 更新预览。")

if __name__=="__main__":
    build()
