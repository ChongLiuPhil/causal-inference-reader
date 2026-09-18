# Working Memory — Task Plan

**状态：** ACTIVE TASK PLAN

## ACTIVE TASKS

- WM-T001 — 建立 HARC-lite 项目治理层并清理误导协作的旧 LaTeX 构建残留 — VALIDATED / PENDING-MERGE
- WM-T002 — 使 QMD-first migration PR #3 可合并并通过完整 HTML validation — COMPLETED
- WM-T003 — 修复首次 main Pages 发布的 gh-pages bootstrap 并完成生产部署 — IN-PROGRESS
- WM-T004 — 实际验证公共站点首页、章节 1/4/7/11、附录、数学、引文、图片和前后导航 — TODO

## NEXT ACTIONS

1. 合并 PR #4。
2. 观察 main 的完整 Quarto + Pages workflow。
3. 验证 `gh-pages` 产物和公共站点。
4. 生产验证完成后把当前阶段转为正常维护。

## BLOCKERS

- 首次 main run #23 的 source/render/reader checks 全部成功，但 publish 因远端不存在 `gh-pages` 失败。
- PR #4 已加入自动创建 `gh-pages` 的修复；尚需 main push 实测。

## PENDING HUMAN DECISIONS / CLARIFICATIONS

### CLR-001 — 开放许可

- Status: WAITING-HUMAN
- Severity: NON-BLOCKING
- Uncertain point: 书籍文本、代码/配置和图形资源是否采用同一许可证，尚未记录。
- Promotion destination: PROTOCOL / repository licensing files

## TODO / BACKLOG

- 在生产发布稳定后评估将 publish job 的 write permission 与 PR validation 的 read-only permission 进一步拆分。
- 评估是否加入 issue templates / CODEOWNERS。
- 正式 release 后完善版本化引用元数据。
- 如未来启用 PDF/EPUB/DOCX，先更新 Form Core 和 Decision Log，再从同一 QMD 增加输出配置。

## SYNC DEFECTS

- 当前 `main` 已是 QMD-first，但尚未包含 HARC-lite 协作层。
- 公共 Pages 尚未完成首次成功发布验证。
