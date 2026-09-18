# START HERE — 因果推理深度读本协作入口

本文件用于任何从零上下文接手本项目的人类协作者或 AI Agent。

## 第一原则

仓库是项目状态的权威来源。不要依赖旧聊天、平台记忆或未写入仓库的摘要来判断当前项目状态。

## 强制读取顺序

在进行实质性正文、结构、构建或发布修改前，依次读取：

1. `HARC_MANIFEST.yaml`
2. `HARC_CONTEXT_INTERFACE.yaml`
3. `AGENTS.md`
4. `docs/working-memory/current-focus.md`
5. `docs/working-memory/task-plan.md`
6. 与当前任务相关的 `core/CONTENT_CORE.md`、`core/FORM_CORE.md`、`core/DECISION_LOG.md`
7. `_quarto.yml`
8. 与任务直接相关的 `manuscript/*.qmd`、`references.bib`、`assets/` 或 workflow

## 当前不可违反的结构约束

- `manuscript/*.qmd` 是唯一 canonical 正文源。
- 不维护第二套 LaTeX、Word、Markdown 或其他正文副本。
- `references.bib` 是书目源；`assets/` 是静态资源源；`book.css` 与 `_quarto.yml` 管理当前 HTML 呈现。
- 当前正式输出仅为 HTML。
- 未来 EPUB/PDF/DOCX 如启用，必须从同一套 QMD 生成。
- PR 可以完整构建和验证全书，但不得发布生产站点。
- `main` 是正式发布源；合并或 push 到 `main` 后由 CI 完整渲染并发布。
- 内容改动只有在生产 GitHub Pages 更新并实际验证后才视为完成。
- 长期仓库不得恢复 LaTeX/TinyTeX/TikZ/dvisvgm 迁移链。

## 接管时先回答

开始修改前，应能从仓库回答：

- 当前阶段和最重要目标是什么？
- 当前 blocker 是什么？
- 哪些决定已经固定，哪些仍未决定？
- 本次请求属于 CONTENT、FORM、PROTOCOL、SOURCE 还是多标签？
- 本次修改应验证哪些章节、引文、资源或发布行为？

如果这些问题无法从仓库回答，先修复项目状态记录，不要靠猜测继续。
