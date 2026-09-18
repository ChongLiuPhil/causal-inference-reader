# Working Memory — Current Focus

**状态：** ACTIVE

## CURRENT_STAGE

QMD-first + HARC-lite 已合并到 `main`；GitHub Pages source binding 待完成。

## CURRENT_OBJECTIVE

完成公共在线读本的首次可访问性验收，然后转入正常维护。

## PRIMARY_BLOCKER

`main` production run #29 已通过 governance、canonical source、完整 Quarto render、reader-output、artifact、`gh-pages` bootstrap 和 Quarto publish。仓库公开元数据为 `has_pages: true`，且 `gh-pages` 已包含完整渲染站点；但公共 URL 仍无法被外部抓取器读取，且 `gh-pages` push 未产生 Pages build/deployment 记录。

当前最可能的剩余账户级配置是 GitHub Pages Source 尚未设为 `gh-pages` / `(root)`。

## IMMEDIATE_NEXT_ACTION

1. 在仓库 Settings → Pages 中确认 Build and deployment → Source 为 “Deploy from a branch”。
2. Branch 选择 `gh-pages`，folder 选择 `/(root)`，保存。
3. 重新验证公共首页、章节 1/4/7/11、附录、数学、引文、图片和前后导航。

## HANDOFF POINTERS

- Task Plan: `docs/working-memory/task-plan.md`
- Stable decisions: `core/DECISION_LOG.md`
- Build/publish rules: `core/FORM_CORE.md`
