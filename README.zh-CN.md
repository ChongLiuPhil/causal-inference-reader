# 因果推理深度读本

[English](README.md) | [中文](README.zh-CN.md)

本项目是一部面向高年级本科生与硕士生的中文深度自学型读本。主线贯通因果哲学、潜在结果、结构因果模型、因果发现、可迁移性与因果机器学习；中国哲学、自由意志和量子因果作为比较性专题附录处理。

本书采用 **3 个主部、11 章正文、4 个附录** 的结构。第 11 章作为全书综合与结论接续第三部分。正文强调把概念、目标量、识别假设、估计、失败诊断和应用连接成可复核的分析过程。

## Canonical source

- `manuscript/*.qmd`：唯一 canonical 正文源。
- `references.bib`：书目数据库。
- `assets/`：静态资源。
- `_quarto.yml`：全书顺序和 Quarto 配置。
- `book.css`：当前 HTML 样式。

当前只构建 HTML。未来如增加 EPUB、PDF 或 DOCX，也必须由同一套 QMD 正文生成，不维护第二份正文。

## 构建

```sh
quarto render --to html
```

本地预览：

```sh
quarto preview
```

## CI 与生产发布

Pull request 会完整渲染和验证 HTML book，但不会发布正式网站。合并或 push 到 `main` 后，GitHub Actions 构建完整 `_book/` 并发布 GitHub Pages。

生产地址：https://chongliuphil.github.io/causal-inference-reader/

生产内容修改只有在 `main` workflow 成功且公共 Pages 实际验证后才视为完成。

## 编辑约定

- 正文只编辑 `manuscript/*.qmd`。
- 文献只在 `references.bib` 中维护。
- 核心事实优先引用原著、正式论文、出版社或作者/机构存档。
- 争议性评价必须明确其解释或论证身份，不写成无争议事实。
- 不得重新引入一次性 LaTeX/TinyTeX/TikZ/dvisvgm 迁移链作为长期构建路径。

## 成品范围

当前读本不以可执行程序代码为中心。公式用于说明目标量、识别逻辑、假设和推理边界，而不是替代统计学证明。附录中的跨文化、自由意志和量子因果内容属于比较研究，不被表述为现代因果推断主线的历史先声。
