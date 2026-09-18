# Form Core

本文件保存全书稳定的形式、构建和发布决定。实现细节仍以 `_quarto.yml`、`book.css` 和 workflows 为准。

## 成果类型

- HUMAN-CONFIRMED — Quarto Book。
- HUMAN-CONFIRMED — 当前正式输出仅为 HTML。
- HUMAN-CONFIRMED — 未来如增加 EPUB、PDF 或 DOCX，必须由同一套 QMD 正文生成。
- HUMAN-CONFIRMED — HTML、未来电子出版物和未来排印版应尽量共享同一套结构语义，而不是各自发展成不同版本的书。

## Canonical source

- HUMAN-CONFIRMED — `manuscript/*.qmd` 是唯一 canonical 正文源。
- HUMAN-CONFIRMED — `references.bib`、`assets/`、`book.css`、`_quarto.yml` 与 QMD 共同组成书籍项目源。
- HUMAN-CONFIRMED — 不维护第二套 LaTeX、Word 或其他正文。
- HUMAN-CONFIRMED — 一次性 LaTeX→QMD 迁移完成后，长期仓库删除 LaTeX/TinyTeX/TikZ/dvisvgm 迁移层。

## 形式参考项目

HUMAN-CONFIRMED — 本项目的电子出版、网页阅读和整体排版方式，可以向下列作者项目靠拢：

- `ChongLiuPhil/What-Remains-Human-Epistemic-Agency-and-Human-Value-in-the-Age-of-AI`
- `ChongLiuPhil/epistemology-textbook`

这里的“靠拢”指共享稳定的出版原则，而不是逐文件复制：

- 同一 canonical QMD 生成网页和未来出版格式；
- 左侧承担全书目录，右侧承担本章目录；
- 长篇阅读优先保证稳定的正文宽度、段落节奏、数学公式、表格和图形的响应式显示；
- 引文和脚注尽量不打断主线阅读，同时保持可核查性；
- 章节参考文献作为明确的收束区，而不是像正文末段的偶然延续；
- 网页样式应克制，服务阅读，不另造一套与正文结构竞争的视觉语言；
- 正式电子出版格式应从同一 QMD 生成，而不是把 HTML 或 PDF 反向当作编辑源。

参考项目中的 Cloudflare 私有预览、双作者设置、特定评论系统、专用研究治理或其他项目特有机制，不因“形式参考”自动进入本项目。

## 发布与验证

- HUMAN-CONFIRMED — `main` 是正式 source branch。
- HUMAN-CONFIRMED — PR 可以完整渲染和验证全书，但不得覆盖生产站点。
- HUMAN-CONFIRMED — 合并或 push 到 `main` 后自动完整渲染 `_book/` 并发布 GitHub Pages。
- HUMAN-CONFIRMED — 内容改动只有在公共 GitHub Pages 更新并实际检查后才视为完成。
- Production URL: https://chongliuphil.github.io/causal-inference-reader/

## 当前 Web Edition 约定

以下项目可以作为当前 Web Edition 的稳定阅读约定：

- 左侧目录明确标为“本书目录”；
- 右侧章节 TOC 明确标为“本章目录”；
- 启用 reader mode、返回顶部、页面导航、搜索和面包屑等不改变正文语义的阅读辅助；
- 章节正文采用适合长文阅读的受控宽度；
- 长公式允许横向滚动，但不得把页面整体撑宽；
- 图片、SVG、表格和长链接必须在窄屏下保持可读；
- 引文与脚注保留 Quarto 原生 hover 预览；
- 参考文献区与正文在视觉上明确分隔。

## 当前实现默认值

以下是当前实现，不自动等于永久作者偏好：

- TEMPORARY-DEFAULT — Quarto theme: `cosmo`。
- TEMPORARY-DEFAULT — HTML math: MathJax。
- TEMPORARY-DEFAULT — 字体仍采用跨平台 CJK serif/sans fallback，而不是绑定单一商用字体。
- TEMPORARY-DEFAULT — 当前不启用参考项目中的自定义 citation dialog / backlink JavaScript；除非确有读者需求，优先保持 Quarto 原生行为。

## 治理

改变 canonical source、正式输出类型、发布分支、生产完成定义或长期构建技术栈属于 FORM/PROTOCOL 高影响变更，必须记录到 `core/DECISION_LOG.md`。
