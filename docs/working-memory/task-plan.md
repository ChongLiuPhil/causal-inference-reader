# Working Memory — Task Plan

**状态：** ACTIVE TASK PLAN

## ACTIVE TASKS

- WM-T001 — 建立 HARC-lite 项目治理层并清理会误导后续协作的旧 LaTeX 构建残留 — IN-PROGRESS
- WM-T002 — 使 PR #3 在 canonical QMD 状态上通过完整 HTML validation 并可合并 — TODO
- WM-T003 — 合并到 `main` 后确认生产发布 workflow green — TODO
- WM-T004 — 实际验证公共站点首页、章节 1/4/7/11、附录、数学、引文、图片和前后导航 — TODO

## NEXT ACTIONS

1. 运行 project governance checks。
2. 运行完整 Quarto HTML validation。
3. 以 stacked PR 审查治理升级，不把它误认为已进入 `main`。
4. 返回并完成 PR #3 / production 闭环。

## BLOCKERS

- PR #3 当前仍未完成正式 merge/deploy 闭环。
- 公共 GitHub Pages 在 main 发布前不能作为完成证据。

## PENDING HUMAN DECISIONS / CLARIFICATIONS

### CLR-001 — 开放许可

- Status: WAITING-HUMAN
- Severity: NON-BLOCKING
- Uncertain point: 书籍文本、代码/配置和图形资源是否采用同一许可证，尚未记录。
- Promotion destination: PROTOCOL / repository licensing files

## TODO / BACKLOG

- 评估是否加入 issue templates / CODEOWNERS。
- 正式 release 后完善版本化引用元数据。
- 如未来启用 PDF/EPUB/DOCX，先更新 Form Core 和 Decision Log，再从同一 QMD 增加输出配置。

## SYNC DEFECTS

- `main` 尚未反映当前 QMD-first migration branch。
