# Working Memory — Work Log

本文件保存阶段性历史，默认不属于零上下文接管的必读链。

## 2026-09-18

- 一次性 LaTeX→QMD 迁移在 `book-reader-site` 上完成：17 个 QMD 冻结为 canonical 正文，迁移脚本/workflow 自删除。
- 迁移期间修复了 dvisvgm 调用兼容性问题。
- 开始参考 Human–AI Research Collaboration Protocol 建立项目适配的 HARC-lite 协作层。
- 协作升级明确不复制第二套正文，不把上游 HARC 的双语/完整 framework 审批结构机械套入本书。

## 2026-09-18 — QMD-first main integration

- PR #3 通过完整 HTML validation 后已 squash 合并到 `main`。
- 首次 main production run #23 的 source、render、reader-output 与 artifact 检查均成功；最终 gh-pages publish 因远端分支尚未初始化而失败。
- PR #4 补充自动 gh-pages bootstrap，并在 PR 级 governance 与完整 Quarto HTML 检查中通过。
- PR #4 已 squash 合并到 `main`，HARC-lite、Quarto-only Makefile、repository-state checker、双语 README、source policy 和治理 CI 正式进入主分支。
- main production run #29 全部成功，包括 governance、canonical source、完整 render、reader-output、artifact、首次 `gh-pages` bootstrap 和 Quarto publish。
- `gh-pages` 最新提交 `9dd013b9567fb622f5d70560ea61dee696a31eee` 为 “Built site for gh-pages”，站点树包含首页、章节 1/4/7/11、附录、references、MathJax/citation/navigation HTML 和图形资产。
- 仓库公开元数据显示 `has_pages: true`；但外部公共 URL 仍无法抓取，且未观察到 `gh-pages` Pages build/deployment 记录。当前 handoff blocker 转为仓库 Settings → Pages 的 source binding。
