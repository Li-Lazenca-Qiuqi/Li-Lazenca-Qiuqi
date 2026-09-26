# Demo 预览与维护

Demo 与检查日期：2026-09-12。文档更新日期：2026-09-15。

## 交付与边界

用户要求“先给我做个 demo”。现已提供 README 演示稿、19 个 SVG 资源和本地预览壳。配色为气象青绿与深蓝灰，包含等压线意象 Banner、个人介绍、四类技术内容、统计占位和静态贡献贪吃蛇。

个人定位来自用户规则；具体文案与工具清单仍供审阅。统计卡片无实际数值，贡献网格为确定性合成示例，页面与图内均有标识。未连接 GitHub 账号、未创建 Actions 或远程仓库，也未进行 Git 提交与发布。

## 当前预览方式

预览从磁盘读取 README，经 markdown-it-py 3.0.0 转换和 nh3 0.2.21 过滤后生成 HTML。正文使用 github-markdown-css 5.8.1，来源与 MIT 许可位于 demo/vendor/。已移除独立内容模板中的编号、右侧说明和定制介绍布局。

## 打开预览

在 WSL Ubuntu-E 的项目根目录先生成预览：

    uv run --script scripts/build_preview.py

然后启动本地服务：

```bash
uv run --no-project python -m http.server 8765 --bind 0.0.0.0
```

打开 http://localhost:8765/demo/ 。2026-09-12 的 Demo 任务曾启动该服务，此记录不表示服务目前仍在运行。再次使用时先检查是否可访问；若端口已被占用，先确认已有服务是否为本预览，不必重复启动。服务停止后可重新运行，也可直接用浏览器打开 demo/index.html。

页面顶部提供深浅主题切换、375 px 窄屏预览和 README 源文件入口。这些控件仅属于本地预览；GitHub 上的 README 使用 picture 根据主题选择资源。

## 文件与修改方式

- README_.md：暂时不在 GitHub 资料页展示的演示草稿；定稿后可改回 README.md。
- assets/：Banner、统计占位、贡献示例的深浅主题 SVG。
- assets/badges/：13 个统一徽章，使用文字缩写而非官方品牌图形。
- demo/index.html：当前 README 的渲染快照，修改 README 后需重新生成并刷新。
- demo/style.css、demo/preview.js：本地预览样式与控件。
- scripts/build_demo.py：标准库素材与 README 生成器。
- scripts/build_preview.py：读取 README 的独立预览渲染器，依赖通过 uv 安装。
- demo/vendor/：固定版本的 Markdown 深浅主题 CSS 与许可。

仅预览 README 时运行 build_preview.py；需要重建内容或 SVG 时才修改素材生成器并运行：

```bash
uv run --no-project python scripts/build_demo.py
```

该命令覆盖 README_.md 及其管理的 SVG，不再生成预览 HTML；运行前核对人工修改。随后单独运行 build_preview.py，它只读取该草稿，并按项目根目录解析资源路径。

## 本地检查结果（2026-09-12）

- Python AST 与 JavaScript 语法检查通过。
- 19 个 SVG 均可解析，包含可访问标题，不含脚本。
- README 与预览页中的本地资源链接有效，图片均有替代文字。
- 使用 Codex 浏览器的 Playwright 接口与截图检查深浅主题、1280 px 桌面和 375 px 手机布局。
- 检查时无横向溢出，图片加载完成后无破图，控制台无警告或错误。
- 宽度按钮切换为 375 px，主题按钮同步更新图片，检查结束时恢复了完整深色预览；不表示之后打开页面时的状态。

这仅证明本地 Demo 可审阅，不代表 PRD 的 GitHub 正式验收完成；动画生成、统计服务、调度及发布仍未实施。

## README 预览改造检查（2026-09-15）

- README 的内容摘要在生成前后保持一致，预览正文等于该文件的直接渲染结果。
- 6 个二级标题、16 张图片、3 组 picture 均保留；资源及文档链接检查通过。
- 脚本、事件属性、内联样式和危险 URL 的过滤检查通过。
- Python 与 JavaScript 语法检查通过，本地 HTTP 返回新版预览。
- 内置浏览器连接失败，本轮未完成截图、深浅主题与窄屏的浏览器验收；2026-09-12 的视觉结果仅属于旧版 Demo。

需补验：刷新页面后检查标题与分段、主题图片切换、窄屏换行。上游 CSS 为开源近似，不代表 GitHub 官方渲染结果；当前账号与线上验收仍未完成。
