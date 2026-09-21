# AHICP Project Session Context Bootstrap — 因果推理深度读本

当前会话只保存 repository resolver，不复制动态项目状态。

```text
AHICP REPOSITORY CONTEXT — ACTIVE

Control:
- AHICP_MANIFEST.yaml
- AHICP_CONTEXT_INTERFACE.yaml

Compatibility:
- HARC_MANIFEST.yaml
- HARC_CONTEXT_INTERFACE.yaml

Working Memory:
- docs/working-memory/current-focus.md
- docs/working-memory/task-plan.md

Content/Form:
- core/CONTENT_CORE.md
- core/FORM_CORE.md
- core/DECISION_LOG.md

Publication:
- publishing.yaml
- website.yaml
- .github/workflows/publish-book.yml

Policy:
- repository-backed
- fresh-read before high-impact action/write
- no authoritative session copy
```

公开 Web Edition 已获授权，但 GitHub Pages provider-side source/binding 的最终验收仍是独立状态。
不要因为 gh-pages 分支发布成功就把公网 runtime 自动写成已验证。
