# Form Core

本文件保存全书稳定的形式、构建和发布决定。实现细节仍以 `_quarto.yml`、`book.css` 和 workflows 为准。

## 成果类型

- HUMAN-CONFIRMED — Quarto Book。
- HUMAN-CONFIRMED — 当前正式输出仅为 HTML。
- HUMAN-CONFIRMED — 未来如增加 EPUB、PDF 或 DOCX，必须由同一套 QMD 正文生成。

## Canonical source

- HUMAN-CONFIRMED — `manuscript/*.qmd` 是唯一 canonical 正文源。
- HUMAN-CONFIRMED — `references.bib`、`assets/`、`book.css`、`_quarto.yml` 与 QMD 共同组成书籍项目源。
- HUMAN-CONFIRMED — 不维护第二套 LaTeX、Word 或其他正文。
- HUMAN-CONFIRMED — 一次性 LaTeX→QMD 迁移完成后，长期仓库删除 LaTeX/TinyTeX/TikZ/dvisvgm 迁移层。

## 发布与验证

- HUMAN-CONFIRMED — `main` 是正式 source branch。
- HUMAN-CONFIRMED — PR 可以完整渲染和验证全书，但不得覆盖生产站点。
- HUMAN-CONFIRMED — 合并或 push 到 `main` 后自动完整渲染 `_book/` 并发布 GitHub Pages。
- HUMAN-CONFIRMED — 内容改动只有在公共 GitHub Pages 更新并实际检查后才视为完成。
- Production URL: https://chongliuphil.github.io/causal-inference-reader/

## 当前实现默认值

以下是当前实现，不自动等于永久作者偏好：

- TEMPORARY-DEFAULT — Quarto theme: `cosmo`。
- TEMPORARY-DEFAULT — HTML math: MathJax。
- TEMPORARY-DEFAULT — 章节导航、搜索、hover citations/footnotes 由 Quarto 当前配置提供。

## 治理

改变 canonical source、正式输出类型、发布分支、生产完成定义或长期构建技术栈属于 FORM/PROTOCOL 高影响变更，必须记录到 `core/DECISION_LOG.md`。
