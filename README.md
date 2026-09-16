# 因果推理深度读本

本项目是一部面向高年级本科生与硕士生的中文深度自学型读本。主线贯通因果哲学、潜在结果、结构因果模型、因果发现、可迁移性与因果机器学习；中国哲学、自由意志和量子因果作为比较性专题附录处理。

本书采用“3个主部、11章正文、4个附录”的结构。第11章作为全书综合与结论接续第三部分，不再单独占用一个只有一章的主部。每章围绕3至4个大型论证单元展开，并以完整算例、失败诊断、图表、学习目标和章末自测把概念、识别、估计与应用连成可复核的分析过程。附录另收20组综合练习参考分析、核心原始文献精读指南、术语与学习路径，书末提供参考文献和主题索引。`main.tex` 是唯一权威入口。

## 在线阅读

本项目同时提供 Quarto Book 网页阅读层，结构与 [What Remains Human](https://github.com/ChongLiuPhil/What-Remains-Human-Epistemic-Agency-and-Human-Value-in-the-Age-of-AI) 项目的在线书籍模式一致：章节侧栏、页面目录、前后章跳转、悬停引文、响应式公式与移动端阅读由 Quarto 负责。

网页正文不维护第二份手稿。`scripts/build_web_source.py` 每次构建时从权威的 `chapters/*.tex` 自动生成 `web-manuscript/*.qmd`，把 TikZ 图转换为 SVG，并继续使用同一个 `references.bib`。生成目录均被 `.gitignore` 忽略，因此 LaTeX/PDF 与网页不会产生两套需要人工同步的正文。

本地构建网页需要 Quarto、XeLaTeX 与 `dvisvgm`：

```sh
python3 scripts/build_web_source.py
quarto render --to html
```

HTML 输出位于 `_book/`。合并到 `main` 后，`.github/workflows/publish-book.yml` 会重新生成网页源、验证 HTML，并将成品发布到 `gh-pages`；计划阅读地址为 <https://chongliuphil.github.io/causal-inference-reader/>。Pull Request 阶段只验证和上传 HTML artifact，不会公开部署。

## 构建要求

- TeX Live 2026 或兼容版本
- XeLaTeX、latexmk、Biber、MakeIndex
- `ctex`、`biblatex-gb7714-2015`、TikZ、`tcolorbox`
- 网页构建另需 Quarto 与 `dvisvgm`
- 验收脚本只使用系统自带的 perl、grep、awk、comm 等工具，无需额外安装 ripgrep 之类的外部依赖

## 构建

```sh
make pdf
```

最终文件生成在 `因果推理深度读本.pdf`。运行 `make watch` 可在源文件变化时自动增量重编译。运行 `make check` 会重新确认成品存在、全书位于12万至13.5万汉字、主线正文位于9万至11万汉字，主线恰有11章且每章不少于6,500汉字，并把正文层级控制在30至40个一级节和90至115个二级节；每个一级节不少于1,200汉字，每个二级节不少于500汉字。全书实际引用220条独立来源；自动文献验收要求全书不少于210条、每章不少于17条，并保证正文引文与书目一一闭合。检查还覆盖书目字段、未解析引用、缺字、控制字符、损坏公式、Unicode特殊横线和排版溢出。此外，`make check` 校验交叉引用闭合（所有 `\label` 唯一、`\ref`/`\cref` 均能解析）与索引一致性（`\term`/`\index` 条目不含未转义特殊字符、同一术语不存在多种索引写法）。运行 `make clean` 会删除中间构建文件、临时检查文件和零散日志，但保留已验收的成品PDF。

## 项目结构

- `main.tex`：唯一编译入口与全书顺序。
- `bookstyle.tex`：版式、字体、教学框、图形、引文与索引设置。
- `chapters/`：全书文稿；`frontmatter-`、`chapter-`、`appendix-` 前缀分别标识前置页、11章主线正文和4个附录。
- `references.bib`：唯一书目数据库。
- `_quarto.yml`、`index.qmd`、`book.css`：在线阅读版的结构与屏幕排版。
- `scripts/build_web_source.py`：从 LaTeX 自动生成 Quarto 网页源与 SVG 图形。
- `.github/workflows/publish-book.yml`：验证网页并在 `main` 上发布 GitHub Pages。
- `因果推理深度读本.pdf`：通过验收的最终成品，可由 `make pdf` 重新生成。

## 编辑约定

- `main.tex` 是唯一入口；全部文稿位于 `chapters/`，并以内容类别和章节编号命名。
- 文献只在 `references.bib` 中维护，正文采用 `\textcite`、`\parencite`。
- 新术语首次出现时使用 `\term{术语}`，以便生成主题索引。
- 核心事实优先引用原著、正式论文、出版社或作者机构存档；争议性评价必须标明其论证身份。
- `web-manuscript/` 与 `web-assets/tikz/` 是构建产物，不应直接编辑或提交；网页问题应回到 LaTeX 源或转换脚本修复。

## 成品范围

本书不包含程序代码。公式用于说明估计目标与识别逻辑，而不是替代统计学证明。附录中的跨文化、自由意志和量子因果内容属于比较研究，不被表述为现代因果推断主线的历史先声。
