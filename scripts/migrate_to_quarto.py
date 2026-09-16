from __future__ import annotations

from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "chapters"
GENERATED_DIR = ROOT / "web-manuscript"
MANUSCRIPT_DIR = ROOT / "manuscript"


def cjk_count(text: str) -> int:
    return len(re.findall(r"[\u3400-\u4dbf\u4e00-\u9fff]", text))


def ordered_source_names() -> list[str]:
    main = (ROOT / "main.tex").read_text(encoding="utf-8")
    inputs = re.findall(r"\\(?:input|include)\{chapters/([^}]+)\}", main)
    if not inputs:
        raise SystemExit("Could not recover chapter order from main.tex")
    return [Path(p if p.endswith(".tex") else p + ".tex").stem for p in inputs]


def verify_conversion(names: list[str]) -> None:
    qmds = {p.stem: p for p in GENERATED_DIR.glob("*.qmd")}
    missing = [name for name in names if name not in qmds]
    if missing:
        raise SystemExit(f"Missing converted QMD files: {missing}")

    weak: list[str] = []
    for name in names:
        source = SOURCE_DIR / f"{name}.tex"
        target = qmds[name]
        if not source.exists():
            raise SystemExit(f"Missing source file: {source}")
        source_n = cjk_count(source.read_text(encoding="utf-8"))
        target_n = cjk_count(target.read_text(encoding="utf-8"))
        if source_n:
            ratio = target_n / source_n
            if ratio < 0.94 or ratio > 1.08:
                weak.append(f"{name}: {target_n}/{source_n} ({ratio:.1%})")
    if weak:
        raise SystemExit("Suspicious text retention after conversion:\n" + "\n".join(weak))


def install_manuscript() -> None:
    if MANUSCRIPT_DIR.exists():
        shutil.rmtree(MANUSCRIPT_DIR)
    GENERATED_DIR.rename(MANUSCRIPT_DIR)
    web_assets = ROOT / "web-assets"
    if web_assets.exists():
        assets = ROOT / "assets"
        if assets.exists():
            shutil.rmtree(assets)
        web_assets.rename(assets)


def build_quarto_config(names: list[str]) -> None:
    prelim = [
        n for n in names
        if not n.startswith("chapter-") and not n.startswith("appendix-")
    ]
    numbered: list[tuple[int, str]] = []
    appendices: list[str] = []
    for name in names:
        match = re.match(r"chapter-(\d+)-", name)
        if match:
            numbered.append((int(match.group(1)), name))
        elif name.startswith("appendix-"):
            appendices.append(name)
    numbered.sort()

    parts = [
        ("第一部　问题、历史与哲学", [n for i, n in numbered if 1 <= i <= 3]),
        ("第二部　识别、结构与估计", [n for i, n in numbered if 4 <= i <= 7]),
        ("第三部　发现、迁移与应用", [n for i, n in numbered if 8 <= i <= 11]),
    ]

    lines = [
        "project:",
        "  type: book",
        "  output-dir: _book",
        "",
        "book:",
        '  title: "因果推理深度读本"',
        '  subtitle: "从哲学、潜在结果与结构因果模型到发现、迁移与因果机器学习"',
        '  author: "ChongLiuPhil"',
        "  site-url: https://chongliuphil.github.io/causal-inference-reader/",
        "  repo-url: https://github.com/ChongLiuPhil/causal-inference-reader",
        "  repo-branch: main",
        "  repo-actions: [edit, issue, source]",
        "  search: true",
        "  page-navigation: true",
        "  downloads: [epub]",
        "  chapters:",
        "    - index.qmd",
    ]
    for name in prelim:
        lines.append(f"    - manuscript/{name}.qmd")
    for title, chapter_names in parts:
        lines.append(f'    - part: "{title}"')
        lines.append("      chapters:")
        for name in chapter_names:
            lines.append(f"        - manuscript/{name}.qmd")
    lines.append("    - references.qmd")
    if appendices:
        lines.append("  appendices:")
        for name in appendices:
            lines.append(f"    - manuscript/{name}.qmd")
    lines.extend([
        "  page-footer:",
        '    left: "因果推理深度读本"',
        '    right: "Built with Quarto"',
        "",
        "bibliography: references.bib",
        "lang: zh-CN",
        "",
        "crossref:",
        '  appendix-title: "附录"',
        '  appendix-delim: "："',
        "",
        "format:",
        "  html:",
        "    theme: cosmo",
        "    css: book.css",
        "    toc: true",
        "    toc-depth: 3",
        "    number-sections: true",
        "    citations-hover: true",
        "    footnotes-hover: true",
        "    link-external-newwindow: true",
        "  epub:",
        "    toc: true",
        "    css: epub.css",
        "    epub-chapter-level: 1",
        "",
    ])
    (ROOT / "_quarto.yml").write_text("\n".join(lines), encoding="utf-8")


def write_support_files() -> None:
    (ROOT / "epub.css").write_text(
        """body { font-family: serif; line-height: 1.7; }\n"
        "h1, h2, h3 { line-height: 1.3; }\n"
        "img, svg { max-width: 100%; height: auto; }\n"
        "table { width: 100%; border-collapse: collapse; }\n"
        "th, td { padding: 0.35em 0.5em; vertical-align: top; }\n"
        ".callout { margin: 1em 0; padding: 0.8em 1em; border-left: 0.25em solid #5b7894; }\n"
        "code { white-space: pre-wrap; }\n""",
        encoding="utf-8",
    )

    (ROOT / "README.md").write_text(
        """# 因果推理深度读本

这是一本以 **Quarto** 为唯一权威源的中文因果推理进阶读本。项目同时面向在线阅读与电子书流通。

## 阅读与输出

- 在线版：<https://chongliuphil.github.io/causal-inference-reader/>
- HTML：`quarto render --to html`
- EPUB：`quarto render --to epub`
- 全部格式：`quarto render`
- 本地预览：`quarto preview`

正文位于 `manuscript/*.qmd`，章节结构由 `_quarto.yml` 统一管理，引用继续使用 `references.bib`。不再维护 LaTeX 版正文，也不维护 LaTeX→QMD 的同步层。

## 编辑原则

- `manuscript/*.qmd` 是唯一正文源。
- 数学公式使用 Quarto/Pandoc Markdown 中的数学标记（如 `$...$` 与 `$$...$$`）；这不意味着项目仍以 LaTeX 文档为源。
- 引用使用 Pandoc/Quarto citation 语法，并统一指向 `references.bib`。
- 网页阅读样式位于 `book.css`，EPUB 样式位于 `epub.css`。
- 修改后运行 `make check`，同时验证 HTML 与 EPUB。

## 结构

全书保持 3 个部分、11 章和 4 个附录。GitHub Actions 会在 pull request 上验证构建；合并到 `main` 后发布 HTML 到 GitHub Pages，并保留 EPUB 构建产物。
""",
        encoding="utf-8",
    )

    (ROOT / "Makefile").write_text(
        """.PHONY: preview html epub render check clean

preview:
\tquarto preview

html:
\tquarto render --to html

epub:
\tquarto render --to epub

render:
\tquarto render

check:
\tpython scripts/check_quarto_source.py
\tquarto render --to html
\tquarto render --to epub
\ttest -f _book/index.html
\ttest -n \"$$(find _book -maxdepth 1 -name '*.epub' -print -quit)\"

clean:
\trm -rf _book .quarto
""",
        encoding="utf-8",
    )

    checker = '''from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
manuscript = root / "manuscript"
files = sorted(manuscript.glob("*.qmd"))
chapters = sorted(manuscript.glob("chapter-*.qmd"))
appendices = sorted(manuscript.glob("appendix-*.qmd"))
errors = []

if len(chapters) != 11:
    errors.append(f"expected 11 chapters, found {len(chapters)}")
if len(appendices) != 4:
    errors.append(f"expected 4 appendices, found {len(appendices)}")
if len(files) < 17:
    errors.append(f"expected at least 17 manuscript QMD files, found {len(files)}")

text = "\\n".join(p.read_text(encoding="utf-8") for p in files)
for token in ("TODO", "TBD", "FIXME", "待补", "待写", "占位"):
    if token in text:
        errors.append(f"placeholder token remains: {token}")

legacy = [
    r"\\\\chapter\\{", r"\\\\section\\{", r"\\\\subsection\\{",
    r"\\\\textcite\\{", r"\\\\parencite\\{", r"\\\\begin\\{document\\}",
    r"\\\\term\\{",
]
for pattern in legacy:
    if re.search(pattern, text):
        errors.append(f"legacy document-level LaTeX remains: {pattern}")

bib = (root / "references.bib").read_text(encoding="utf-8")
bibkeys = set(re.findall(r"@[A-Za-z]+\\s*\\{\\s*([^,\\s]+)", bib))
cited = set(re.findall(r"(?<![\\w@])@([A-Za-z0-9_:.+-]+)", text))
missing = sorted(k for k in cited if k not in bibkeys)
if missing:
    errors.append("missing bibliography keys: " + ", ".join(missing[:20]))

if errors:
    print("Quarto source validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)
print(f"Validated {len(chapters)} chapters, {len(appendices)} appendices, {len(cited)} cited keys.")
'''
    scripts = ROOT / "scripts"
    scripts.mkdir(exist_ok=True)
    (scripts / "check_quarto_source.py").write_text(checker, encoding="utf-8")

    gitignore_path = ROOT / ".gitignore"
    gitignore = gitignore_path.read_text(encoding="utf-8") if gitignore_path.exists() else ""
    lines = gitignore.splitlines()
    for item in ("_book/", ".quarto/", "web-manuscript/", "web-assets/"):
        if item not in lines:
            lines.append(item)
    gitignore_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def remove_legacy_files() -> None:
    if SOURCE_DIR.exists():
        shutil.rmtree(SOURCE_DIR)
    for relative in (
        "main.tex",
        "bookstyle.tex",
        "project.yaml",
        "website.yaml",
        "因果推理深度读本.pdf",
        "scripts/build_web_source.py",
        ".github/workflows/publish-book.yml",
    ):
        path = ROOT / relative
        if path.exists():
            path.unlink()


def main() -> None:
    if not (ROOT / "main.tex").exists():
        print("Repository is already Quarto-first; nothing to migrate.")
        return
    if not GENERATED_DIR.exists():
        raise SystemExit("Run scripts/build_web_source.py before this migration script.")
    names = ordered_source_names()
    verify_conversion(names)
    install_manuscript()
    build_quarto_config(names)
    write_support_files()
    remove_legacy_files()
    print(f"Migrated {len(names)} manuscript files to canonical Quarto sources.")


if __name__ == "__main__":
    main()
