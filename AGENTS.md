# 项目上下文

## 稳定背景与技术栈

- Li-Lazenca-Qiuqi 同仓管理 GitHub Profile README 与独立个人网站；目录名称不代表 GitHub 用户名已确认。
- Profile README 使用 Markdown、GitHub 支持的 HTML 与 SVG；本地预览使用原生 HTML、CSS 和 JavaScript。个人网站放在 `site/`，使用 React、TypeScript 与 Vite。
- 使用 WSL Ubuntu-E 内的工具链；Python 通过 uv 运行，素材生成器仅依赖标准库；独立预览脚本使用固定版本的 Markdown 渲染依赖。
- README.md 是 GitHub Profile 的交付物，这是相对通用安装说明规则的项目特例；不承载内部项目记忆。独立网站在 `site/`，预览、维护说明放在 doc/。

## 目录地图与阅读顺序

1. [产品现状](doc/PRODUCT.md)：定位、已有能力、关键流程、支持范围与限制。
2. [当前待办](doc/TODO.md)：唯一活动任务清单。
3. [路线规划](doc/Roadmap.md)：阶段目标。
4. [Profile README 产品需求](doc/PRD/github-profile.md)：需求与正式验收条件。
5. [个人网站需求草案](doc/PRD/personal-site.md)：同仓网站的范围与待确认内容。
6. [Profile README 技术路线](doc/decisions/001-profile-readme.md)与[个人网站技术路线](doc/decisions/002-personal-site.md)：两个交付物的选型及约束。
7. [来源依据](doc/note/chat-source.md)：原 Profile README 需求来源与证据边界。
8. [README Demo 预览与维护](doc/note/demo-preview.md)：操作方法和带日期的检查记录。
9. [个人网站预览与维护](doc/note/site-preview.md)：网站本地操作与检查记录。
10. [文档约定](doc/AGENTS.md)：文档职责与维护规则。
11. doc/archive/：历史归档，按追溯需要读取。
12. assets/：Profile README 的 SVG 资源；demo/：README 本地预览壳；site/：个人网站；scripts/：README 内容与资源生成器。

## 长期约定

- 开始工作前按任务范围读取上述文档及可用的 Git 状态和近期记录。
- 文档和注释使用简体中文；代码标识符、路径、图中文字及专业术语使用英语；新增内容不使用 Emoji。
- 区分用户明确要求、聊天建议和工作假设；不得编造履历、科研成果、联系方式或账号数据。
- Profile README 与个人网站分别维护；`demo/` 是 README 预览，`site/` 是独立网站源码。网站首版平衡研究、开发和游戏玩家身份，不将气象意象作为整站主视觉。
- 重建素材时使用 scripts/build_demo.py；它覆盖 README 和受管理的 SVG，运行前保留人工修改。仅更新预览时使用 scripts/build_preview.py，它读取当前 README，只生成预览 HTML。
- Git 提交、版本更新分别需要用户明确要求；CHANGELOG.md 仅在明确更新版本时创建或修改。
- 删除已有文件或用户数据前列清单并取得确认，优先移入回收站。本次代理创建的临时文件及可再生成的构建中间产物，核实路径且确认不含用户数据或交付成果后可直接清理；归属或影响不明时须确认。
- 不使用 LAST_RUN.md。阶段进度记录在 TODO、Roadmap 和 PRODUCT，历史过程按主题归档。
