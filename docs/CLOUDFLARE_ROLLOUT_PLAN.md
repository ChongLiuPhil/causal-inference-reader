# Cloudflare migration plan — management-only

Status: **planning only**. This file records a future hosting/access migration and does not change the current GitHub Pages site, source-repository visibility, canonical URL, project content, or provider state.

## Current-state preservation
- Keep the existing public GitHub source repository unchanged.
- Keep the existing GitHub Pages resource and any current URL active until a separate Cloudflare Worker is live, restricted, and verified.
- Do not delete `gh-pages`, disable Pages, redirect URLs, or change canonical identity in this phase.

## Target management state
- Target provider: Cloudflare Workers / Workers Static Assets.
- Planned Worker: `causal-inference-reader`.
- Target Web visibility: restricted even though source remains public.
- Reader policy reference: `shared-reader-access`.
- Preview visibility: private; preview builds disabled until real Access acceptance.
- Production branch: `main`; commit-triggered only; no scheduled polling.
- Public bypass: disabled; no custom domain selected.
- Paid services: not authorized.

## Content/build boundary
This phase does not modify Quarto sources, book/manuscript content, bibliography, assets, current Pages workflow, or build configuration. The existing build command/output directory will be selected and verified only in a later deployment phase.

## Manual/provider gates
Cloudflare login/MFA, account-wide Access verification, reader approval, GitHub App repository authorization, Worker/Builds reconciliation, actual build/output verification, anonymous denial, approved-reader access, direct-asset protection, and final cutover authorization remain separate gates.

## Rollback
Before cutover, Pages remains the recovery path because it is not changed here. After a future verified Worker cutover, retain the previous verified Worker version. No paid upgrade, DNS change, or old-site retirement is authorized by this plan.
