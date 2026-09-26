# 聊天来源与需求依据

## 来源

- 聊天：[GitHub主页制作方法](https://chatgpt.com/c/6a980d16-91a8-83e9-840f-f2126c8e9ffe)。
- 读取日期：2026-09-12。
- 通过任务读取工具获得一轮完整问答，返回无更多分页。
- 用户原始问题：朋友的 GitHub 主页很炫酷，希望了解制作方法。
- 朋友主页：https://github.com/makoMakoGo
- 本次新增要求：先初始化记忆系统，再根据聊天生成 PRD。

## 需求解释

| 编号 | 信息 | 性质与处理 |
| --- | --- | --- |
| S01 | 用户希望了解朋友主页的制作方式 | 历史用户明确表达；可推导为本项目的参考方向 |
| S02 | Profile README、SVG、GitHub Actions | 历史助手给出的实现解释；作为拟定技术路线 |
| S03 | 气象科研与开发者主题、气象 Banner | 历史助手建议；本 PRD 采用为可审阅提案 |
| S04 | Python、C++、Fortran、uv 等工具 | 与当前用户规则一致；具体公开徽章清单仍需确认 |
| S05 | GISS、CMAQ、WRF、Aerosol、BC 及 AI 工具清单 | 历史助手举例；不能视作用户确认的使用经历或公开资料 |
| S06 | Stats、贡献贪吃蛇、每日更新、深浅主题 | 历史助手建议；列入后续增强需求 |
| S07 | 初始化项目记忆并生成 PRD | 本次用户明确授权的交付 |

## 技术核验

2026-09-12 检索官方文档与上游 README：

- [GitHub 官方 Profile README 文档](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)：目标公开仓库需与用户名同名，根目录 README.md 非空。
- [Platane/snk 上游说明](https://github.com/Platane/snk/blob/main/README.md)：支持生成贡献图 SVG，提供 SVG 专用 Action 与深色主题用法。
- 历史聊天中的朋友仓库资产、Vercel 部署推断、统计服务当前可用性未在本次独立核验，不作为已验证事实。
- 实施时再核对上游版本、许可、权限与服务可用性；历史代码示例不直接作为冻结配置。

## 尚缺资料

GitHub 用户名、公开姓名或昵称组合、简介、研究方向清单、工具清单、视觉偏好、统计服务选择。当前目录名称仅作为项目名使用。
