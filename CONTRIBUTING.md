# Contributing — 因果推理深度读本

## 开始之前

先阅读 `START_HERE.md` 与 `AGENTS.md`。正文贡献必须建立在 `manuscript/*.qmd` 上，不接受第二套正文源。

## 贡献类型

PR 请标明一个或多个类别：

- `CONTENT` — 正文、论点、定义、章节组织。
- `SOURCE` — 文献、引文、BibTeX、事实核验。
- `FORM` — Quarto、CSS、导航、输出格式。
- `PROTOCOL` — CI、发布、协作治理、项目状态。

## 正文与来源

- 实质性事实/历史/方法学修改应提供可核验来源。
- 优先使用原始论文、原著、出版社、正式机构或作者存档。
- 新增 citation 必须在 `references.bib` 有对应 key。
- 不要把争议性解释写成无争议事实。
- 不要通过修改正文规避相反证据；应明确呈现证据边界。

## 构建

```sh
make check
make html
```

`make check` 执行项目治理和 canonical source 检查；`make html` 在此基础上完整渲染 HTML book。

## PR 完成条件

PR 至少应说明：

- 改了什么以及属于哪类变更；
- 影响哪些章节/来源/构建行为；
- 是否改变事实性主张或引用；
- 是否改变 canonical/source/publish 规则；
- 运行了哪些验证。

PR 不发布生产站点。生产变更只有合并到 `main`、发布成功并验证公共 Pages 后才完成。
