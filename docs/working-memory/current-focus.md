# Working Memory — Current Focus

**状态：** ACTIVE

## CURRENT_STAGE

Authorial/pedagogical alignment and Web Edition form alignment are implemented and CI-validated; public GitHub Pages source binding remains the external blocker.

## CURRENT_OBJECTIVE

保持新的项目定位与阅读形式稳定，并完成公共在线读本的首次可访问性验收。

## PRIMARY_BLOCKER

仓库内没有未解决的内容或构建 blocker。PR #6 已验证：

- 项目性质明确为学习整合、问题组织与作者判断；
- 哲学研究与哲学史/思想史/思想研究的功能区分进入稳定治理；
- “本书目录 / 本章目录 / 本章参考文献”实际出现在渲染 HTML；
- reader mode、长文宽度与响应式数学/表格/图形配置可完整 render。

公共 Pages 最终可访问性仍等待仓库 Settings → Pages 将 Source 设为 `gh-pages` / `(root)`。

## IMMEDIATE_NEXT_ACTION

1. 在仓库 Settings → Pages 中确认 Build and deployment → Source 为 “Deploy from a branch”。
2. Branch 选择 `gh-pages`，folder 选择 `/(root)`，保存。
3. 重新验证公共首页、章节 1/4/7/11、附录、数学、引文、图片、目录标签与前后导航。
4. 公网验收后转入正常内容维护。

## HANDOFF POINTERS

- Task Plan: `docs/working-memory/task-plan.md`
- Stable decisions: `core/DECISION_LOG.md`
- Content positioning: `core/CONTENT_CORE.md`
- Build/publish rules: `core/FORM_CORE.md`
