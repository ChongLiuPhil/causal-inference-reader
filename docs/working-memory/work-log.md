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
- PR #4 已补充自动 gh-pages bootstrap，并在 PR 级 governance 与完整 Quarto HTML 检查中通过。
