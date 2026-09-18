# Working Memory — Current Focus

**状态：** ACTIVE

## CURRENT_STAGE

Authorial/pedagogical alignment + Web Edition form alignment; GitHub Pages source binding remains an external blocker for public verification.

## CURRENT_OBJECTIVE

把作者刚确认的项目性质、问题导向哲学观和出版形式参考写入稳定治理，并验证新的 Quarto Web Edition 配置不会破坏全书 HTML 构建。

## PRIMARY_BLOCKER

仓库侧尚无新的代码 blocker。此前公共 Pages 的最终可访问性仍等待仓库 Settings → Pages 将 Source 设为 `gh-pages` / `(root)`，因此本轮形式改动即使 main CI green，也不能在公网验证完成前宣告 production completion。

## IMMEDIATE_NEXT_ACTION

1. 验证 `align-authorial-philosophy-and-publication-form` 的 governance/source checks 和完整 HTML render。
2. 检查“本书目录 / 本章目录 / reader mode / 参考文献收束区 / 响应式公式表格”是否正常生成。
3. PR green 后合并到 `main`。
4. Pages source binding 完成后，对公共站点做最终读者路径验收。

## HANDOFF POINTERS

- Task Plan: `docs/working-memory/task-plan.md`
- Stable decisions: `core/DECISION_LOG.md`
- Content positioning: `core/CONTENT_CORE.md`
- Build/publish rules: `core/FORM_CORE.md`
