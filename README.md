# Causal Inference Reader

[English](README.md) | [中文](README.zh-CN.md)

This project is an advanced Chinese-language self-study reader for senior undergraduates and master's students. Its main line connects the philosophy of causation, potential outcomes, structural causal models, causal discovery, transportability, and causal machine learning; Chinese philosophy, free will, and quantum causation are treated as comparative thematic appendices.

The book uses **3 main parts, 11 core chapters, and 4 appendices**. Chapter 11 serves as the synthesis and conclusion following Part III. The text emphasizes auditable links among concepts, estimands, identification assumptions, estimation, failure diagnosis, and application.

## Canonical source

- `manuscript/*.qmd`: the only canonical body source.
- `references.bib`: the bibliography database.
- `assets/`: static book assets.
- `_quarto.yml`: book order and Quarto configuration.
- `book.css`: current HTML styling.

The project currently builds HTML only. Any future EPUB, PDF, or DOCX output must be rendered from the same QMD body rather than from a second manuscript.

## Build

```sh
quarto render --to html
```

Local preview:

```sh
quarto preview
```

## CI and publishing

Pull requests render and validate the complete HTML book but do not publish the production site. Merge or push to `main` renders the complete `_book/` and publishes GitHub Pages.

Production URL: https://chongliuphil.github.io/causal-inference-reader/

A production content change is complete only after the `main` workflow succeeds and the public Pages site is verified.

## Editing conventions

- Edit book body text only in `manuscript/*.qmd`.
- Maintain references only in `references.bib`.
- Prefer primary works, formal publications, publishers, or author/institutional archives for core factual claims.
- Identify contested evaluations as interpretations rather than presenting them as settled facts.
- Do not reintroduce the one-time LaTeX/TinyTeX/TikZ/dvisvgm migration toolchain as a long-term build path.

## Scope

The current book does not center on executable programming code. Formulas are used to clarify estimands, identification logic, assumptions, and inferential boundaries rather than to replace statistical proofs. The cross-cultural, free-will, and quantum-causation appendices are comparative studies and are not presented as historical precursors of the modern causal-inference tradition.
