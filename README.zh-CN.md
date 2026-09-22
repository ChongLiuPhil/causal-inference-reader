# 因果推理深度读本

[English](README.md) | [中文](README.zh-CN.md)

本项目是一部中文因果推理深度自学型读本，主线贯通因果哲学、潜在结果、结构因果模型、因果发现、可迁移性与因果机器学习；中国哲学、自由意志和量子因果作为比较性专题附录处理。

## 项目定位

这首先是一个持续学习、整合和梳理的读本项目，而不是为了把全书包装成一套必须由作者原创的完整理论。作者性的主要部分在于问题选择、材料组织、概念区分、解释重心和最终判断：哪些材料应放在一起，哪些相似只是表面相似，哪些争论需要保留张力，哪些结论的强度应当被限制。

因此，AI 可以参与检索、核验、综合、论证重构、起草和技术维护，但全书的问题设置、判断视角和最终公开版本仍需要作者审核和承担。

本书同时强调问题导向的哲学学习。哲学研究并不等于研究前代哲学家的思想；哲学史、思想史、思想研究与直接回答哲学问题彼此相关，却不是同一种任务。人物和历史材料进入本书，是为了帮助澄清问题、重构论证、比较概念和检验答案，而不是以人物罗列代替哲学思考。这一方向与作者的 `epistemology-textbook` 项目保持一致。

仓库采用 Quarto 和 repository-backed 协作方式：正文、长期决定、当前工作状态和发布规则都有明确的 canonical 位置。

## 在线版状态

**公网访问仍待验收。** 预期 GitHub Pages 地址为 `https://chongliuphil.github.io/causal-inference-reader/`；2026-09-22 的独立检查返回 HTTP 404，目前不能把它作为已验证可用的在线阅读链接。

公开 Web Edition 已获授权，但 provider 侧 Pages 发布源绑定及公网验证仍待完成，具体状态见 [website.yaml](website.yaml)。完整构建通过或成功推送至 `gh-pages` 分支，并不单独证明公共网站已经可用。

目前可浏览[正文源文件](manuscript/)，或使用下方命令在本地预览。本次状态修正不改变书稿、公开发布授权或交付平台。

## Canonical source

- `manuscript/*.qmd`：唯一正文源。
- `references.bib`：书目数据库。
- `assets/`：静态资源。
- `_quarto.yml`：全书顺序和 Quarto 配置。
- `book.css`：当前 HTML 样式。

当前只构建 HTML。未来如增加 EPUB、PDF 或 DOCX，也必须由同一套 QMD 正文生成。

## 阅读与出版形式

本项目的 Web Edition 和未来电子出版形式参考作者的其他 Quarto book 项目，尤其是：

- `What-Remains-Human-Epistemic-Agency-and-Human-Value-in-the-Age-of-AI`
- `epistemology-textbook`

参考的是整体出版原则：同一 QMD 源、左侧全书目录、右侧本章目录、长文阅读宽度、公式/表格/图片的响应式排版、引文可核查性和未来多格式一致性。其他项目特有的私有部署、评论系统或专用治理不会自动复制到这里。

## 协作接管

新的协作者或 AI Agent 应依次阅读：

1. `START_HERE.md`
2. `AHICP_MANIFEST.yaml`
3. `AHICP_CONTEXT_INTERFACE.yaml`
4. `AGENTS.md`
5. `docs/working-memory/current-focus.md`
6. `docs/working-memory/task-plan.md`

本项目保留 HARC-lite 作为 project-native 历史治理层，并使用 current AHICP 作为当前协议入口；functional mapping 用于持久化决定和交接状态，不复制第二套正文。

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

书籍验证工作流会对符合 pull-request 路径过滤条件的修改验证治理状态、canonical source 和完整 HTML book，但不会发布生产站点。合并或 push 到 `main` 后完整渲染 `_book/`，并将验证后的 HTML 发布到 `gh-pages` 分支。公共网站是否可访问，还取决于 provider 侧 Pages 发布源绑定及实际公网验证。

生产内容修改只有在 `main` workflow 成功且公共 Pages 实际验证后才视为完成。

贡献规则见 `CONTRIBUTING.md`；稳定项目决定见 `core/`；当前目标和 blocker 见 `docs/working-memory/`。

## 成品范围

当前读本不以可执行程序代码为中心。公式用于说明目标量、识别逻辑、假设和推理边界。比较性附录不被表述为现代因果推断主线的历史先声。
