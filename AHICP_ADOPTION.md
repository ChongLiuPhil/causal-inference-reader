# Current AHICP / Inquiry Publishing Stack Adoption — 因果推理深度读本

本项目保留 HARC-lite 作为 project-native 历史治理层，并采用 current AHICP 作为当前协议入口。

## Current pins

- AHICP: `0.3.0-draft @ ed5a60b1016497472072db108072ace59bcdb65d`
- PPF: `0.1.1-draft @ e660b48fb216c28c8faa1f0fe2d0816401e1de2c`
- Vault Interface: `79d64b12275a5cc7c09236b144bf4213fa7afc5e`
- Starter: `4889739d448a9bf68bedb42ce3182315eda0caeb`

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
