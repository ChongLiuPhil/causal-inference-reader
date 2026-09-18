# Causal Inference Reader

[English](README.md) | [中文](README.zh-CN.md)

This project is an advanced Chinese-language self-study reader for senior undergraduates and master's students. Its main line connects the philosophy of causation, potential outcomes, structural causal models, causal discovery, transportability, and causal machine learning; Chinese philosophy, free will, and quantum causation are treated as comparative thematic appendices.

The book uses a structure of **3 main parts, 11 core chapters, and 4 appendices**. Chapter 11 serves as the synthesis and conclusion following Part III rather than forming a separate one-chapter part. Each chapter is organized around three to four large argumentative units and links concepts, identification, estimation, and application into an auditable analytical process through worked examples, failure diagnosis, figures, learning objectives, and end-of-chapter self-tests. The appendices additionally include reference analyses for 20 integrated exercises, a close-reading guide to major primary sources, terminology and learning pathways, followed by references and a subject index. `main.tex` is the single authoritative entry point.

## Build requirements

- TeX Live 2026 or a compatible version
- XeLaTeX, latexmk, Biber, MakeIndex
- `ctex`, `biblatex-gb7714-2015`, TikZ, `tcolorbox`
- The acceptance scripts use only system-provided tools such as perl, grep, awk, and comm; no extra dependency such as ripgrep is required.

## Build

```sh
make pdf
```

The final file is generated as `因果推理深度读本.pdf`. Run `make watch` for incremental rebuilding when source files change. Run `make check` to reconfirm that the final artifact exists; that the book contains 120,000–135,000 Chinese characters overall and 90,000–110,000 Chinese characters in the core chapters; that the main text contains exactly 11 chapters with at least 6,500 Chinese characters per chapter; and that the hierarchy remains within 30–40 first-level sections and 90–115 second-level sections, with at least 1,200 Chinese characters per first-level section and at least 500 per second-level section.

The book currently cites 220 independent sources. Automated reference acceptance requires at least 210 sources overall and at least 17 per chapter, while ensuring one-to-one closure between in-text citations and bibliography entries. The checks also cover bibliography fields, unresolved citations, missing glyphs, control characters, damaged formulas, special Unicode dashes, and typesetting overflow. In addition, `make check` verifies cross-reference closure (all `\label` values unique and all `\ref`/`\cref` references resolvable) and index consistency (`\term`/`\index` entries contain no unescaped special characters and the same term is not indexed under multiple spellings). Running `make clean` removes intermediate build files, temporary check files, and miscellaneous logs while preserving the accepted final PDF.

## Project structure

- `main.tex`: the single compilation entry point and the authoritative book order.
- `bookstyle.tex`: layout, fonts, pedagogical boxes, figures, citations, and index settings.
- `chapters/`: the book manuscript; the `frontmatter-`, `chapter-`, and `appendix-` prefixes identify front matter, the 11 core chapters, and the 4 appendices.
- `references.bib`: the single bibliography database.
- `因果推理深度读本.pdf`: the accepted final artifact, reproducible with `make pdf`.

## Editing conventions

- `main.tex` is the only entry point; all manuscript text lives in `chapters/`, named by content type and chapter number.
- References are maintained only in `references.bib`; the text uses `\textcite` and `\parencite`.
- Use `\term{term}` when a new term first appears so that it enters the subject index.
- For core factual claims, prefer original works, formal publications, publishers, or author/institutional archives; contested evaluations must clearly identify their argumentative status.

## Scope of the final artifact

The book contains no programming code. Formulas are used to explain estimands and identification logic rather than to replace statistical proofs. The cross-cultural, free-will, and quantum-causation appendices are comparative studies and are not presented as historical precursors of the modern causal-inference tradition.
