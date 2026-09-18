# Working Memory — Task Plan

**状态：** ACTIVE TASK PLAN

## ACTIVE TASKS

- WM-T001 — 建立 HARC-lite 项目治理层并清理误导协作的旧 LaTeX 构建残留 — COMPLETED
- WM-T002 — 使 QMD-first migration PR #3 可合并并通过完整 HTML validation — COMPLETED
- WM-T003 — 修复首次 main Pages 发布的 gh-pages bootstrap 并完成生产分支发布 — COMPLETED
- WM-T004 — 实际验证公共站点首页、章节 1/4/7/11、附录、数学、引文、图片和前后导航 — BLOCKED / WAITING-PAGES-SOURCE

## NEXT ACTIONS

1. 人类在 GitHub Settings → Pages 中确认 Source = “Deploy from a branch”。
2. Branch = `gh-pages`，folder = `/(root)`，保存。
3. 公网可访问后完成逐页验收。
4. 验收后把 Current Focus 转为正常维护。

## BLOCKERS

- 仓库侧生产链已全部 green：main run #29 的 governance/source/render/reader/artifact/bootstrap/publish 均成功。
- `gh-pages` 最新提交为 Quarto 生成的 “Built site for gh-pages”，并包含完整 HTML 站点。
- 公开仓库元数据为 `has_pages: true`，但外部 URL 仍不可读取，且没有观察到 `gh-pages` 对应 Pages build/deployment 记录。
- 当前剩余 blocker 为 Pages source/binding 的仓库设置，连接器没有该管理端写权限。

## PENDING HUMAN DECISIONS / CLARIFICATIONS

### CLR-001 — 开放许可

- Status: WAITING-HUMAN
- Severity: NON-BLOCKING
- Uncertain point: 书籍文本、代码/配置和图形资源是否采用同一许可证，尚未记录。
- Promotion destination: PROTOCOL / repository licensing files

## TODO / BACKLOG

- 生产站点稳定后评估将 publish job 的 write permission 与 PR validation 的 read-only permission 进一步拆分。
- 评估是否加入 issue templates / CODEOWNERS。
- 正式 release 后完善版本化引用元数据。
- 如未来启用 PDF/EPUB/DOCX，先更新 Form Core 和 Decision Log，再从同一 QMD 增加输出配置。

## SYNC DEFECTS

- 公共 Pages 可访问性尚未完成最终验收。
