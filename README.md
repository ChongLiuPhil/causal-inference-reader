# 因果推理深度读本

这是一个 Quarto 在线书项目。`manuscript/*.qmd` 是唯一 canonical 正文源；`references.bib`、`assets/`、`book.css` 与 QMD 共同组成书籍源文件。

- 在线版：https://chongliuphil.github.io/causal-inference-reader/
- 本地 HTML 构建：`quarto render --to html`
- 本地预览：`quarto preview`

当前 CI 只构建 HTML。Pull request 会验证完整 HTML 构建但不会部署正式网站；合并或 push 到 `main` 后由 GitHub Actions 构建完整 `_book/` 并部署 GitHub Pages。

未来如增加 EPUB、PDF 或 DOCX，也必须从完全相同的 `manuscript/*.qmd` 正文生成，不维护第二份正文。
