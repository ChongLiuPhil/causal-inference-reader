# Causal Inference Reader

[English](README.md) | [中文](README.zh-CN.md)

This project is an advanced Chinese-language self-study reader connecting the philosophy of causation, potential outcomes, structural causal models, causal discovery, transportability, and causal machine learning. Chinese philosophy, free will, and quantum causation are treated as comparative thematic appendices.

The repository uses Quarto and a repository-backed collaboration model. Book content, project decisions, current work state, and publishing rules all have explicit canonical locations.

## Online book

https://chongliuphil.github.io/causal-inference-reader/

## Canonical source

- `manuscript/*.qmd`: the only canonical body source.
- `references.bib`: bibliography.
- `assets/`: static assets.
- `_quarto.yml`: book order and Quarto configuration.
- `book.css`: current HTML styling.

The project currently builds HTML only. Any future EPUB, PDF, or DOCX output must be rendered from the same QMD body.

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
