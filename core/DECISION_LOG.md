# Decision Log

本文件记录需要跨会话、跨协作者持续有效的项目决定。保留历史，不删除被取代条目。

## 2026-09-18 — D001

**分类：** FORM / PROTOCOL  
**决定：** `manuscript/*.qmd` 为唯一 canonical 正文源；references/assets/book.css/_quarto.yml 为配套项目源，不再维护第二套 LaTeX 正文。  
**状态：** implemented on `main`.

## 2026-09-18 — D002

**分类：** FORM / PROTOCOL  
**决定：** 当前只发布 HTML。PR 完整验证但不发布生产；`main` push/merge 完整 render 并发布 GitHub Pages。未来 EPUB/PDF/DOCX 必须从相同 QMD 生成。  
**状态：** implemented on `main`; branch publication verified, public URL verification pending Pages source binding.

## 2026-09-18 — D003

**分类：** PROTOCOL  
**决定：** 任何生产内容修改只有在 CI 通过、`main` 发布成功且公共 GitHub Pages 实际验证后才视为完成。  
**状态：** active.

## 2026-09-18 — D004

**分类：** FORM / PROTOCOL  
**决定：** LaTeX→QMD 只允许作为一次性迁移；迁移完成后删除 LaTeX/TinyTeX/TikZ/dvisvgm 迁移 machinery 和旧 canonical 痕迹。  
**状态：** implemented on `main`; migration machinery、旧 Makefile/PDF 和 stale QMD migration headers 已清理。

## 2026-09-18 — D005

**分类：** PROTOCOL  
**决定：** 参考 `ChongLiuPhil/Human-AI-Research-Collaboration-Protocol` 建立项目适配的 HARC-lite 协作层，采用“仓库状态高于聊天记忆、零上下文接管、CONTENT/FORM/PROTOCOL/SOURCE 路由、Decision Log、Working Memory、高影响不确定性不猜测”等机制；不复制第二套正文，也不宣称完整 HARC conformance。  
**上游参考 commit：** `e741c43c5cd158c43910e3832c7d757226717a97`  
**状态：** implemented and CI-validated on `main`.
