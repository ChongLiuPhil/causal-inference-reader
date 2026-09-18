# Causal Inference Reader

[English](README.md) | [中文](README.zh-CN.md)

This project is an advanced Chinese-language self-study reader connecting the philosophy of causation, potential outcomes, structural causal models, causal discovery, transportability, and causal machine learning. Chinese philosophy, free will, and quantum causation are treated as comparative thematic appendices.

## Project character

The book is primarily a structured record of continued learning, synthesis, and problem-driven organization rather than an attempt to present every part as an original authorial theory. Its authorial contribution lies especially in problem selection, organization of materials, conceptual distinctions, interpretive emphasis, and final judgment.

AI can assist with retrieval, verification, synthesis, argument reconstruction, drafting, and technical maintenance. The book's central questions, interpretive weighting, philosophical judgments, and final public version remain subject to the author's review.

The project also adopts a problem-driven view of philosophy. Philosophical research is not identical with studying what earlier philosophers thought. History of philosophy, intellectual history, history of ideas, and direct philosophical inquiry can inform one another, but they perform different tasks. Historical material is used to clarify questions, reconstruct arguments, compare conceptual frameworks, and test answers rather than to substitute the study of figures for philosophy itself.

## Online book

https://chongliuphil.github.io/causal-inference-reader/

## Canonical source

- `manuscript/*.qmd`: the only canonical body source.
- `references.bib`: bibliography.
- `assets/`: static assets.
- `_quarto.yml`: book order and Quarto configuration.
- `book.css`: current HTML styling.

The project currently builds HTML only. Any future EPUB, PDF, or DOCX output must be rendered from the same QMD body.

## Reading and publication form

The Web Edition and future electronic publication formats take design cues from the author's other Quarto book projects, especially `What-Remains-Human-Epistemic-Agency-and-Human-Value-in-the-Age-of-AI` and `epistemology-textbook`.

The shared principles are a single QMD source, book-level and chapter-level navigation, stable long-form reading width, responsive math/tables/figures, inspectable citations, and future multi-format consistency. Project-specific private deployment, commenting, or governance systems are not copied automatically.

## Collaboration onboarding

A new human collaborator or AI Agent should begin with:

1. `START_HERE.md`
2. `HARC_MANIFEST.yaml`
3. `HARC_CONTEXT_INTERFACE.yaml`
4. `AGENTS.md`
5. `docs/working-memory/current-focus.md`
6. `docs/working-memory/task-plan.md`

The collaboration layer is a project-specific HARC-lite adaptation inspired by [Human–AI Research Collaboration Protocol](https://github.com/ChongLiuPhil/Human-AI-Research-Collaboration-Protocol). It persists decisions and handoff state without duplicating the book manuscript and does not claim full HARC conformance.

## Build and check

```sh
make check
make html
```

Preview:

```sh
make preview
```

## CI and publishing

Pull requests validate governance, canonical sources, and the complete HTML book without publishing production. Merge or push to `main` renders the complete `_book/` and publishes GitHub Pages.

A production content change is complete only after the `main` workflow succeeds and the public Pages site is verified.

See `CONTRIBUTING.md` for contribution rules, `core/` for stable project decisions, and `docs/working-memory/` for the current objective and blockers.

## Scope

The current book does not center on executable programming code. Formulas clarify estimands, identification logic, assumptions, and inferential boundaries. Comparative appendices are not presented as historical precursors of the modern causal-inference tradition.
