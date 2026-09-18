# 因果推理深度读本

这是一个 Quarto 在线书项目。正文、协作状态和发布流程都以 GitHub 仓库中的 canonical 文件为准。

## 在线版

https://chongliuphil.github.io/causal-inference-reader/

## Canonical source

- `manuscript/*.qmd`：唯一正文源。
- `references.bib`：书目数据库。
- `assets/`：静态资源。
- `_quarto.yml`：全书顺序和 Quarto book 配置。
- `book.css`：当前 HTML 样式。

当前只构建 HTML。未来如增加 EPUB、PDF 或 DOCX，也必须从完全相同的 QMD 正文生成，不维护第二份正文。

## 协作接管

任何新的协作者或 AI Agent 应先阅读：

1. `START_HERE.md`
2. `HARC_MANIFEST.yaml`
3. `HARC_CONTEXT_INTERFACE.yaml`
4. `AGENTS.md`
5. `docs/working-memory/current-focus.md`
6. `docs/working-memory/task-plan.md`

本项目参考 [Human–AI Research Collaboration Protocol](https://github.com/ChongLiuPhil/Human-AI-Research-Collaboration-Protocol) 建立项目适配的 HARC-lite 协作层；它用于持久化决定、当前状态和交接规则，不复制第二套正文，也不宣称完整 HARC conformance。

## 本地检查与构建

```sh
make check
make html
```

本地预览：

```sh
make preview
```

## CI 与生产发布

- Pull request：执行项目状态检查、canonical source 检查和完整 HTML render，但不发布生产站点。
- `main`：合并或 push 后完整构建 `_book/` 并部署 GitHub Pages。
- 生产内容修改只有在 `main` CI green、部署完成且公共网站实际验证后才视为完成。

贡献规则见 `CONTRIBUTING.md`；稳定内容/形式决定见 `core/`；当前任务和 blocker 见 `docs/working-memory/`。
