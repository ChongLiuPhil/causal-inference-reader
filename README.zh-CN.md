# 因果推理深度读本

[English](README.md) | [中文](README.zh-CN.md)

本项目是一部中文因果推理深度自学型读本，主线贯通因果哲学、潜在结果、结构因果模型、因果发现、可迁移性与因果机器学习；中国哲学、自由意志和量子因果作为比较性专题附录处理。

仓库采用 Quarto 和 repository-backed 协作方式：正文、长期决定、当前工作状态和发布规则都有明确的 canonical 位置。

## 在线版

https://chongliuphil.github.io/causal-inference-reader/

## Canonical source

- `manuscript/*.qmd`：唯一正文源。
- `references.bib`：书目数据库。
- `assets/`：静态资源。
- `_quarto.yml`：全书顺序和 Quarto 配置。
- `book.css`：当前 HTML 样式。

当前只构建 HTML。未来如增加 EPUB、PDF 或 DOCX，也必须由同一套 QMD 正文生成。

## 协作接管

新的协作者或 AI Agent 应依次阅读：

1. `START_HERE.md`
2. `HARC_MANIFEST.yaml`
3. `HARC_CONTEXT_INTERFACE.yaml`
4. `AGENTS.md`
5. `docs/working-memory/current-focus.md`
6. `docs/working-memory/task-plan.md`

本项目参考 [Human–AI Research Collaboration Protocol](https://github.com/ChongLiuPhil/Human-AI-Research-Collaboration-Protocol) 建立项目适配的 HARC-lite 协作层，用于持久化决定和交接状态，不复制第二套正文，也不宣称完整 HARC conformance。

## 检查与构建

```sh
make check
make html
```

本地预览：

```sh
make preview
```

## CI 与生产发布

Pull request 会验证治理状态、canonical source 和完整 HTML book，但不会发布生产站点。合并或 push 到 `main` 后完整渲染 `_book/` 并发布 GitHub Pages。

生产内容修改只有在 `main` workflow 成功且公共 Pages 实际验证后才视为完成。

贡献规则见 `CONTRIBUTING.md`；稳定项目决定见 `core/`；当前目标和 blocker 见 `docs/working-memory/`。

## 成品范围

当前读本不以可执行程序代码为中心。公式用于说明目标量、识别逻辑、假设和推理边界。比较性附录不被表述为现代因果推断主线的历史先声。
