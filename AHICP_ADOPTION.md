# Current AHICP / Inquiry Publishing Stack Adoption — 因果推理深度读本

本项目保留 HARC-lite 作为 project-native 历史治理层，并采用 current AHICP 作为当前协议入口。

## Current Stack revisions

Stack v2 separates stable composition/template revisions from the semantic framework revisions adopted by this project.

- AHICP template: `02d0b3c02ca23073c760b6e0f761a468e0235a1c`; project adopted: `ed5a60b1016497472072db108072ace59bcdb65d`
- PPF template: `9a6005de85f032095e36eea03fda317e73126538`; project adopted: `e660b48fb216c28c8faa1f0fe2d0816401e1de2c`
- Vault template: `592c6e2e938f995b7b3e7df07a72f7f1e2c50c5a`; project adopted: `79d64b12275a5cc7c09236b144bf4213fa7afc5e`
- Starter source revision: `05857086e240cbd269eae91af8419ea0921c01fa`

## Functional mapping

| Stack role | Project-local authority |
| --- | --- |
| Content Core | `core/CONTENT_CORE.md` |
| Form Core | `core/FORM_CORE.md` |
| Decision Log | `core/DECISION_LOG.md` |
| Working Memory | `docs/working-memory/` |
| Canonical manuscript | `manuscript/*.qmd` |
| Bibliography | `references.bib` |
| Source policy | `evidence/source-policy.md` |

不创建仅为形式对称服务的 Framework Status / Argument Map。

## Publication mapping

PPF 现在只把现有 GitHub Pages 生命周期写成机器合同：

- public Web Edition：已授权；
- repository：public；
- provider：GitHub Pages；
- `gh-pages` branch publishing：repository workflow 已验证；
- provider-side Pages source/binding：仍未完成最终验收；
- target URL：`https://chongliuphil.github.io/causal-inference-reader/`；
- 本次升级不切换 provider，不改变公开授权，不改变正文。
