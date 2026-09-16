from __future__ import annotations

from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "chapters"
GENERATED_DIR = ROOT / "web-manuscript"
MANUSCRIPT_DIR = ROOT / "manuscript"

SOURCES = [
    ("frontmatter-preface", "frontmatter-preface"),
    ("frontmatter-guide", "frontmatter-guide"),
    ("chapter-01-questions", "01-questions"),
    ("chapter-02-history", "02-history"),
    ("chapter-03-philosophies", "03-philosophies"),
    ("chapter-04-potential-outcomes-identification", "04-potential-outcomes-identification"),
    ("chapter-05-scm-graphs", "05-scm-graphs"),
    ("chapter-06-identification-calculus", "06-identification-calculus"),
    ("chapter-07-design-estimation", "07-design-estimation"),
    ("chapter-08-discovery", "08-discovery"),
    ("chapter-09-transportability", "09-transportability"),
    ("chapter-10-causal-ml-applications", "10-causal-ml-applications"),
    ("chapter-11-synthesis-open-problems", "11-synthesis-open-problems"),
    ("appendix-A-comparative-topics", "appendix-A-comparative-topics"),
    ("appendix-B-glossary-learning", "appendix-B-glossary-learning"),
    ("appendix-C-exercises", "appendix-C-exercises"),
    ("appendix-D-primary-reading", "appendix-D-primary-reading"),
]


def cjk_count(text: str) -> int:
    return len(re.findall(r"[\u3400-\u4dbf\u4e00-\u9fff]", text))


def verify_conversion() -> None:
    missing: list[str] = []
    losses: list[str] = []
    for source_stem, output_stem in SOURCES:
        source = SOURCE_DIR / f"{source_stem}.tex"
        target = GENERATED_DIR / f"{output_stem}.qmd"
        if not source.exists() or not target.exists():
            missing.append(f"{source_stem} -> {output_stem}")
            continue
        source_n = cjk_count(source.read_text(encoding="utf-8"))
        target_n = cjk_count(target.read_text(encoding="utf-8"))
        if source_n and target_n / source_n < 0.94:
            losses.append(
                f"{source_stem}: {target_n}/{source_n} ({target_n / source_n:.1%})"
            )
    if missing:
        raise SystemExit("Missing converted QMD files:\n" + "\n".join(missing))
    if losses:
        raise SystemExit("Possible text loss after conversion:\n" + "\n".join(losses))


def install_manuscript() -> None:
    if MANUSCRIPT_DIR.exists():
        shutil.rmtree(MANUSCRIPT_DIR)
    GENERATED_DIR.rename(MANUSCRIPT_DIR)

    for qmd in MANUSCRIPT_DIR.glob("*.qmd"):
        text = qmd.read_text(encoding="utf-8")
        text = text.replace("../web-assets/", "../assets/")
        qmd.write_text(text, encoding="utf-8")

    web_assets = ROOT / "web-assets"
    assets = ROOT / "assets"
    if assets.exists():
        shutil.rmtree(assets)
    if web_assets.exists():
        web_assets.rename(assets)
    else:
        assets.mkdir(parents=True, exist_ok=True)


def write_quarto_config() -> None:
    content = '''project:
  type: book
  output-dir: _book
  resources:
    - assets/**

book:
  title: "因果推理深度读本"
  subtitle: "从哲学问题到现代形式方法"
  author: "ChongLiuPhil"
  site-url: https://chongliuphil.github.io/causal-inference-reader/
  repo-url: https://github.com/ChongLiuPhil/causal-inference-reader
  repo-branch: main
  repo-actions: [edit, issue, source]
  search: true
  page-navigation: true
  chapters:
    - index.qmd
    - manuscript/frontmatter-preface.qmd
    - manuscript/frontmatter-guide.qmd
    - part: "第一部　问题、历史与哲学"
      chapters:
        - manuscript/01-questions.qmd
        - manuscript/02-history.qmd
        - manuscript/03-philosophies.qmd
    - part: "第二部　识别、结构与估计"
      chapters:
        - manuscript/04-potential-outcomes-identification.qmd
        - manuscript/05-scm-graphs.qmd
        - manuscript/06-identification-calculus.qmd
        - manuscript/07-design-estimation.qmd
    - part: "第三部　发现、迁移与应用"
      chapters:
        - manuscript/08-discovery.qmd
        - manuscript/09-transportability.qmd
        - manuscript/10-causal-ml-applications.qmd
        - manuscript/11-synthesis-open-problems.qmd
    - references.qmd
  appendices:
    - manuscript/appendix-A-comparative-topics.qmd
    - manuscript/appendix-B-glossary-learning.qmd
    - manuscript/appendix-C-exercises.qmd
    - manuscript/appendix-D-primary-reading.qmd
  page-footer:
    left: "因果推理深度读本"
    right: "Built with Quarto"

bibliography: references.bib
lang: zh-CN

crossref:
  appendix-title: "附录"
  appendix-delim: "："

format:
  html:
    theme: cosmo
    css: book.css
    toc: true
    toc-depth: 3
    number-sections: true
    number-depth: 3
    citations-hover: true
    footnotes-hover: true
    html-math-method: mathjax
    link-external-newwindow: true
'''
    (ROOT / "_quarto.yml").write_text(content, encoding="utf-8")


def write_index() -> None:
    content = '''# 因果推理深度读本 {.unnumbered}

## 从哲学问题到现代形式方法 {.unnumbered}

这是一部面向高年级本科生与硕士生的中文深度自学型读本。主线从因果概念与哲学问题出发，进入潜在结果、结构因果模型、图形识别与研究设计，再延伸到因果发现、可迁移性、因果机器学习和跨学科应用。

本网站与未来其他输出格式都以仓库中的 `manuscript/*.qmd` 为唯一正文源；引用数据来自 `references.bib`，图片资源位于 `assets/`，网页样式位于 `book.css`。

[开始阅读前言](manuscript/frontmatter-preface.qmd) · [如何使用本书](manuscript/frontmatter-guide.qmd) · [GitHub 源码](https://github.com/ChongLiuPhil/causal-inference-reader)

### 三条阅读路径 {.unnumbered}

**哲学路径**：第1至第3章与第11章。重点关注因果概念、反事实、机制、干预与解释。

**统计与社会科学路径**：第1章、第4至第7章、第9章与第10章。重点关注估计目标、识别、研究设计、估计和迁移。

**计算机与人工智能路径**：第1、5、6、8、9、10、11章。重点关注图模型、因果发现、分布变化、因果机器学习与部署边界。
'''
    (ROOT / "index.qmd").write_text(content, encoding="utf-8")


def write_readme() -> None:
    content = '''# 因果推理深度读本

这是一个 Quarto 在线书项目。`manuscript/*.qmd` 是唯一 canonical 正文源；`references.bib`、`assets/`、`book.css` 与 QMD 共同组成书籍源文件。

- 在线版：https://chongliuphil.github.io/causal-inference-reader/
- 本地 HTML 构建：`quarto render --to html`
- 本地预览：`quarto preview`

当前 CI 只构建 HTML。Pull request 会验证完整 HTML 构建但不会部署正式网站；合并或 push 到 `main` 后由 GitHub Actions 构建完整 `_book/` 并部署 GitHub Pages。

未来如增加 EPUB、PDF 或 DOCX，也必须从完全相同的 `manuscript/*.qmd` 正文生成，不维护第二份正文。
'''
    (ROOT / "README.md").write_text(content, encoding="utf-8")


def write_checker() -> None:
    content = r'''from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
manuscript = root / "manuscript"
expected = [
    "frontmatter-preface.qmd",
    "frontmatter-guide.qmd",
    "01-questions.qmd",
    "02-history.qmd",
    "03-philosophies.qmd",
    "04-potential-outcomes-identification.qmd",
    "05-scm-graphs.qmd",
    "06-identification-calculus.qmd",
    "07-design-estimation.qmd",
    "08-discovery.qmd",
    "09-transportability.qmd",
    "10-causal-ml-applications.qmd",
    "11-synthesis-open-problems.qmd",
    "appendix-A-comparative-topics.qmd",
    "appendix-B-glossary-learning.qmd",
    "appendix-C-exercises.qmd",
    "appendix-D-primary-reading.qmd",
]
errors = []
missing = [name for name in expected if not (manuscript / name).is_file()]
if missing:
    errors.append("missing manuscript files: " + ", ".join(missing))

files = [manuscript / name for name in expected if (manuscript / name).is_file()]
text = "\n".join(p.read_text(encoding="utf-8") for p in files)
placeholder = re.compile(
    r"(?mi)^\s*(?:TODO|TBD|FIXME|待补|待写|占位)(?:\s*[:：-].*)?\s*$"
)
for match in placeholder.finditer(text):
    errors.append(f"placeholder line remains: {match.group(0).strip()}")

for pattern in (
    r"\\chapter\{", r"\\section\{", r"\\subsection\{",
    r"\\textcite\{", r"\\parencite\{", r"\\begin\{document\}",
    r"WEBTABLE\d+", r"WEBTIKZ\d+", r"web-assets/",
):
    if re.search(pattern, text):
        errors.append(f"legacy migration markup remains: {pattern}")

bib = (root / "references.bib").read_text(encoding="utf-8")
bibkeys = set(re.findall(r"@[A-Za-z]+\s*\{\s*([^,\s]+)", bib))
# Validate unambiguous Pandoc bracket citations only. Bare @tokens can be ordinary
# handles/usernames in prose or code; Quarto/Pandoc remains responsible for
# interpreting narrative citations during the full render.
citation_groups = re.findall(r"\[[^\]\n]*@[^\]\n]+\]", text)
cited = {
    key
    for group in citation_groups
    for key in re.findall(r"(?<![\w@])@([A-Za-z0-9_:.+-]+)", group)
}
missing_keys = sorted(key for key in cited if key not in bibkeys)
if missing_keys:
    errors.append("missing bibliography keys: " + ", ".join(missing_keys[:30]))

asset_refs = set(re.findall(r"\.\./assets/([^\s\"')>]+)", text))
for rel in sorted(asset_refs):
    if not (root / "assets" / rel).exists():
        errors.append(f"missing asset: assets/{rel}")

if errors:
    print("Quarto source validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)
print(f"Validated {len(files)} manuscript files and {len(cited)} bracket citation keys.")
'''
    scripts = ROOT / "scripts"
    scripts.mkdir(exist_ok=True)
    (scripts / "check_quarto_source.py").write_text(content, encoding="utf-8")


def update_gitignore() -> None:
    path = ROOT / ".gitignore"
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    lines = [line for line in existing.splitlines() if line not in {"web-manuscript/", "web-assets/"}]
    for item in ("_book/", ".quarto/", "tmp/"):
        if item not in lines:
            lines.append(item)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def remove_legacy() -> None:
    if SOURCE_DIR.exists():
        shutil.rmtree(SOURCE_DIR)
    for relative in (
        "main.tex",
        "bookstyle.tex",
        "project.yaml",
        "website.yaml",
        "epub.css",
        "scripts/build_web_source.py",
        "scripts/migrate_to_quarto.py",
        ".github/workflows/quarto-first.yml",
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

    verify_conversion()
    install_manuscript()
    write_quarto_config()
    write_index()
    write_readme()
    write_checker()
    update_gitignore()
    remove_legacy()
    print(f"Migrated {len(SOURCES)} source files to canonical manuscript/*.qmd.")


if __name__ == "__main__":
    main()
