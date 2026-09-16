#!/usr/bin/env python3
"""Generate Quarto-readable chapters from the canonical LaTeX manuscript.

The LaTeX files remain the sole manuscript source of truth. This script creates
web-manuscript/*.qmd and SVG copies of TikZ figures for the HTML reader.
Generated files are intentionally not committed.
"""

from __future__ import annotations

import html
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "web-manuscript"
ASSETS = ROOT / "web-assets" / "tikz"
TMP = ROOT / "tmp" / "web-tikz"


@dataclass(frozen=True)
class Source:
    source: str
    output: str
    display_ref: str | None = None
    unnumbered: bool = False


SOURCES = [
    Source("chapters/frontmatter-preface.tex", "frontmatter-preface.qmd", unnumbered=True),
    Source("chapters/frontmatter-guide.tex", "frontmatter-guide.qmd", unnumbered=True),
    Source("chapters/chapter-01-questions.tex", "01-questions.qmd", "1"),
    Source("chapters/chapter-02-history.tex", "02-history.qmd", "2"),
    Source("chapters/chapter-03-philosophies.tex", "03-philosophies.qmd", "3"),
    Source("chapters/chapter-04-potential-outcomes-identification.tex", "04-potential-outcomes-identification.qmd", "4"),
    Source("chapters/chapter-05-scm-graphs.tex", "05-scm-graphs.qmd", "5"),
    Source("chapters/chapter-06-identification-calculus.tex", "06-identification-calculus.qmd", "6"),
    Source("chapters/chapter-07-design-estimation.tex", "07-design-estimation.qmd", "7"),
    Source("chapters/chapter-08-discovery.tex", "08-discovery.qmd", "8"),
    Source("chapters/chapter-09-transportability.tex", "09-transportability.qmd", "9"),
    Source("chapters/chapter-10-causal-ml-applications.tex", "10-causal-ml-applications.qmd", "10"),
    Source("chapters/chapter-11-synthesis-open-problems.tex", "11-synthesis-open-problems.qmd", "11"),
    Source("chapters/appendix-A-comparative-topics.tex", "appendix-A-comparative-topics.qmd", "A"),
    Source("chapters/appendix-B-glossary-learning.tex", "appendix-B-glossary-learning.qmd", "B"),
    Source("chapters/appendix-C-exercises.tex", "appendix-C-exercises.qmd", "C"),
    Source("chapters/appendix-D-primary-reading.tex", "appendix-D-primary-reading.qmd", "D"),
]


BOXES = {
    "learninggoals": "学习目标",
    "keypoint": "关键辨析",
    "chapterreview": "本章小结",
    "selfcheck": "自测与研讨",
}


def run(cmd: list[str], *, cwd: Path | None = None, input_text: str | None = None) -> str:
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        joined = " ".join(cmd)
        raise RuntimeError(f"Command failed: {joined}\n{proc.stdout}\n{proc.stderr}")
    return proc.stdout


def replace_balanced_command(text: str, command: str, replacement_prefix: str) -> str:
    token = f"\\{command}{{"
    while token in text:
        start = text.index(token)
        content_start = start + len(token)
        depth = 1
        i = content_start
        while i < len(text) and depth:
            ch = text[i]
            escaped = i > 0 and text[i - 1] == "\\"
            if not escaped:
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
            i += 1
        if depth:
            raise ValueError(f"Unbalanced \\{command} in manuscript")
        inner = text[content_start : i - 1]
        replacement = replacement_prefix + inner + "\n"
        text = text[:start] + replacement + text[i:]
    return text


def build_label_map() -> dict[str, tuple[str, str]]:
    mapping: dict[str, tuple[str, str]] = {}
    for item in SOURCES:
        if item.display_ref is None:
            continue
        content = (ROOT / item.source).read_text(encoding="utf-8")
        for label in re.findall(r"\\label\{([^}]+)\}", content):
            if label.startswith("ch:") or label.startswith("app:"):
                mapping[label] = (item.output, item.display_ref)
    return mapping


def replace_crossrefs(text: str, label_map: dict[str, tuple[str, str]]) -> str:
    for label, (target, display) in label_map.items():
        # Keep the surrounding Chinese classifier in the prose and link only the number/letter.
        link = f"\\href{{{target}}}{{{display}}}"
        text = text.replace(f"\\ref{{{label}}}", link)
        text = text.replace(f"\\cref{{{label}}}", link)
        text = text.replace(f"\\autoref{{{label}}}", link)
    return text


def normalize_citations(text: str) -> str:
    def citation(kind: str, match: re.Match[str]) -> str:
        note = match.group(1)
        keys = match.group(2)
        if note:
            return f"\\{kind}[{note}]{{{keys}}}"
        return f"\\{kind}{{{keys}}}"

    text = re.sub(
        r"\\parencite(?:\[([^\]]*)\])?\{([^}]+)\}",
        lambda m: citation("citep", m),
        text,
    )
    text = re.sub(
        r"\\textcite(?:\[([^\]]*)\])?\{([^}]+)\}",
        lambda m: citation("citet", m),
        text,
    )
    return text


def normalize_boxes(text: str) -> str:
    for env, title in BOXES.items():
        text = text.replace(
            f"\\begin{{{env}}}",
            f"\\begin{{quote}}\n\\textbf{{{title}}}\\par\n",
        )
        text = text.replace(f"\\end{{{env}}}", "\\end{quote}")

    def titled_box(env: str, prefix: str, value: str) -> str:
        pattern = re.compile(rf"\\begin\{{{env}\}}(?:\[([^\]]*)\])?")

        def repl(match: re.Match[str]) -> str:
            title = match.group(1) or ""
            heading = prefix if not title else f"{prefix}：{title}"
            return f"\\begin{{quote}}\n\\textbf{{{heading}}}\\par\n"

        value = pattern.sub(repl, value)
        return value.replace(f"\\end{{{env}}}", "\\end{quote}")

    text = titled_box("workedexample", "完整算例", text)
    text = titled_box("failurecheck", "失败诊断", text)
    return text


def clean_table_cell(cell: str) -> str:
    cell = cell.strip()
    cell = re.sub(r"\\multicolumn\{[^}]+\}\{[^}]+\}\{([^{}]*)\}", r"\1", cell)
    cell = re.sub(r"\\multirow(?:\[[^\]]*\])?\{[^}]+\}\{[^}]+\}\{([^{}]*)\}", r"\1", cell)
    for _ in range(3):
        cell = re.sub(r"\\(?:textbf|textit|emph|term|eng)\{([^{}]*)\}", r"\1", cell)
    cell = re.sub(
        r"\\(?:parencite|textcite|citep|citet)(?:\[[^\]]*\])?\{([^}]+)\}",
        lambda m: "[" + ", ".join(k.strip() for k in m.group(1).split(",")) + "]",
        cell,
    )
    cell = cell.replace("WEBBR", "\n")
    cell = cell.replace(r"\%", "%").replace(r"\&", "&").replace("~", " ")
    cell = re.sub(r"\\(?:small|normalsize|raggedright|centering)\b", "", cell)
    cell = re.sub(r"\s+", " ", cell).strip()
    escaped = html.escape(cell, quote=False)
    return escaped.replace("\n", "<br>")


def table_to_html(body: str) -> str:
    shortstack = re.compile(r"\\shortstack(?:\[[^\]]*\])?\{([^{}]*)\}")
    body = shortstack.sub(lambda m: m.group(1).replace("\\\\", "WEBBR"), body)

    if r"\endfirsthead" in body and r"\endhead" in body:
        before, remainder = body.split(r"\endfirsthead", 1)
        _, after = remainder.split(r"\endhead", 1)
        body = before + after

    caption_match = re.search(r"\\caption\{([^{}]*)\}", body)
    caption = clean_table_cell(caption_match.group(1)) if caption_match else ""
    body = re.sub(r"\\caption\{[^{}]*\}", "", body)
    body = re.sub(r"\\(?:toprule|midrule|bottomrule|endfirsthead|endhead)\b", "", body)
    body = re.sub(r"\\addlinespace(?:\[[^\]]*\])?", "", body)

    raw_rows = re.split(r"(?<!\\)\\\\(?!\\)", body)
    rows: list[list[str]] = []
    for raw in raw_rows:
        raw = raw.strip()
        if not raw or raw.startswith("%"):
            continue
        cells = [clean_table_cell(c) for c in re.split(r"(?<!\\)&", raw)]
        if cells and any(c for c in cells):
            rows.append(cells)

    if not rows:
        return ""

    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    header = rows[0]
    data = rows[1:]

    parts = ['<div class="table-responsive web-table">', '<table class="table">']
    if caption:
        parts.append(f"<caption>{caption}</caption>")
    parts.append("<thead><tr>" + "".join(f"<th>{c}</th>" for c in header) + "</tr></thead>")
    parts.append("<tbody>")
    for row in data:
        parts.append("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>")
    parts.extend(["</tbody>", "</table>", "</div>"])
    return "\n".join(parts)


def extract_tables(text: str) -> tuple[str, dict[str, str]]:
    replacements: dict[str, str] = {}
    pattern = re.compile(
        r"\\begin\{(longtable|tabularx|tabular)\}[^\n]*\n(.*?)\\end\{\1\}",
        re.DOTALL,
    )

    def repl(match: re.Match[str]) -> str:
        marker = f"WEBTABLE{len(replacements):04d}"
        replacements[marker] = table_to_html(match.group(2))
        return "\n" + marker + "\n"

    return pattern.sub(repl, text), replacements


def tikz_document(block: str) -> str:
    return r"""\documentclass[border=6pt]{standalone}
\usepackage[UTF8,fontset=fandol]{ctex}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\definecolor{deepblue}{HTML}{173B57}
\definecolor{warmgray}{HTML}{F3F1EC}
\definecolor{accent}{HTML}{9A5A36}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,fit,calc,shapes.geometric}
\tikzset{
  causalnode/.style={draw=deepblue,thick,circle,minimum size=8mm,inner sep=1pt},
  causalbox/.style={draw=deepblue,rounded corners,align=center,minimum height=8mm,fill=blue!3},
  causalarrow/.style={-{Latex[length=2mm]},thick,deepblue}
}
\newcommand{\doop}{\operatorname{do}}
\newcommand{\indep}{\mathrel{\perp\!\!\!\perp}}
\begin{document}
""" + block + "\n\\end{document}\n"


def render_tikz(block: str, name: str) -> str:
    if shutil.which("xelatex") is None or shutil.which("dvisvgm") is None:
        raise RuntimeError("Web figure rendering requires xelatex and dvisvgm.")

    work = TMP / name
    work.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    tex = work / "figure.tex"
    tex.write_text(tikz_document(block), encoding="utf-8")
    run(["xelatex", "-no-pdf", "-interaction=nonstopmode", "-halt-on-error", "figure.tex"], cwd=work)
    xdv = work / "figure.xdv"
    svg = ASSETS / f"{name}.svg"
    run(["dvisvgm", "--no-fonts", "--output", str(svg), str(xdv)], cwd=work)
    return f'\n<figure><img class="web-tikz" src="../web-assets/tikz/{name}.svg" alt="因果结构示意图"></figure>\n'


def extract_tikz(text: str, slug: str) -> tuple[str, dict[str, str]]:
    replacements: dict[str, str] = {}
    pattern = re.compile(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", re.DOTALL)

    def repl(match: re.Match[str]) -> str:
        marker = f"WEBTIKZ{len(replacements):04d}"
        name = f"{slug}-{len(replacements) + 1:02d}"
        replacements[marker] = render_tikz(match.group(0), name)
        return "\n" + marker + "\n"

    return pattern.sub(repl, text), replacements


def preprocess(text: str, label_map: dict[str, tuple[str, str]], slug: str) -> tuple[str, dict[str, str]]:
    text = replace_balanced_command(text, "chapterreadings", "\\section*{延伸阅读}\n")
    text = replace_crossrefs(text, label_map)
    text = normalize_citations(text)
    text = text.replace(r"\term{", r"\textbf{")
    text = text.replace(r"\eng{", r"\textit{")
    text = text.replace(r"\doop", r"\operatorname{do}")
    text = text.replace(r"\indep", r"\perp\!\!\!\perp")
    text = re.sub(r"\\index\{[^{}]*\}", "", text)

    text, tables = extract_tables(text)
    text, figures = extract_tikz(text, slug)
    replacements = {**tables, **figures}

    text = normalize_boxes(text)
    text = text.replace(r"\begin{center}", "").replace(r"\end{center}", "")
    text = text.replace(r"\begin{sloppypar}", "").replace(r"\end{sloppypar}", "")
    text = re.sub(r"\\(?:small|normalsize|cleardoublepage|phantomsection)\b", "", text)
    text = re.sub(r"\\addcontentsline\{[^{}]*\}\{[^{}]*\}\{[^{}]*\}", "", text)
    return text, replacements


def pandoc_latex_to_markdown(text: str) -> str:
    if shutil.which("quarto") is None:
        raise RuntimeError("Quarto is required to build the web manuscript.")
    return run(
        ["quarto", "pandoc", "--from=latex", "--to=markdown", "--wrap=none"],
        input_text=text,
    )


def postprocess(markdown: str, replacements: dict[str, str], *, unnumbered: bool) -> str:
    for marker, replacement in replacements.items():
        markdown = markdown.replace(marker, replacement)

    if unnumbered:
        markdown = re.sub(
            r"^# (.+)$",
            lambda m: m.group(0) if "{.unnumbered}" in m.group(0) else f"# {m.group(1)} {{.unnumbered}}",
            markdown,
            count=1,
            flags=re.MULTILINE,
        )

    markdown = re.sub(r"\n{4,}", "\n\n\n", markdown)
    return "<!-- Generated from canonical LaTeX. Do not edit this file directly. -->\n\n" + markdown.strip() + "\n"


def validate(markdown: str, source: Source) -> None:
    if not re.search(r"^#\s+", markdown, flags=re.MULTILINE):
        raise ValueError(f"Generated chapter has no level-one heading: {source.source}")
    leftovers = [token for token in ("WEBTABLE", "WEBTIKZ", r"\begin{tikzpicture}") if token in markdown]
    if leftovers:
        raise ValueError(f"Unconverted web markers in {source.source}: {leftovers}")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)

    label_map = build_label_map()
    generated = 0
    figure_count_before = len(list(ASSETS.glob("*.svg")))

    for item in SOURCES:
        source_path = ROOT / item.source
        text = source_path.read_text(encoding="utf-8")
        slug = Path(item.output).stem
        prepared, replacements = preprocess(text, label_map, slug)
        markdown = pandoc_latex_to_markdown(prepared)
        markdown = postprocess(markdown, replacements, unnumbered=item.unnumbered)
        validate(markdown, item)
        (OUT / item.output).write_text(markdown, encoding="utf-8")
        generated += 1

    figure_count_after = len(list(ASSETS.glob("*.svg")))
    print(f"Generated {generated} web chapters in {OUT.relative_to(ROOT)}")
    print(f"Rendered {max(0, figure_count_after - figure_count_before)} new TikZ SVG figures")


if __name__ == "__main__":
    main()
