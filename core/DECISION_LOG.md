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

## 2026-09-18 — D006

**分类：** CONTENT / PROTOCOL  
**决定：** 本项目主要是一部学习型、整合型、问题驱动的因果推理读本，不要求把全书包装成作者原创理论。作者性的核心在于问题设置、材料组织、概念区分、解释重心和最终哲学判断；AI 可以广泛参与检索、综合、重构和起草，但这些高影响判断及最终公开版本需由作者审核和承担。  
**状态：** active project decision; implemented and CI-validated through PR #6.

## 2026-09-18 — D007

**分类：** CONTENT  
**决定：** 本书明确区分哲学研究、哲学史研究、思想史研究与思想研究。人物和历史材料可以为哲学问题提供资源，但“研究前人的思想”本身不等于完成哲学研究。教学组织继续坚持问题先于人物、先重构论证再评价，并与 `epistemology-textbook` 已采用的问题驱动方向保持一致。  
**状态：** active project decision; implemented and CI-validated through PR #6.

## 2026-09-18 — D008

**分类：** FORM  
**决定：** Web Edition 与未来电子出版/排版形式参考作者的 `What-Remains-Human-Epistemic-Agency-and-Human-Value-in-the-Age-of-AI` 和 `epistemology-textbook` 项目：同一 QMD 源、左侧全书目录、右侧本章目录、稳定长文宽度、响应式数学/表格/图形、明确参考文献收束区，以及未来多格式由同一源生成。参考项目特有的私有部署、评论系统或研究治理不自动复制。  
**状态：** active project decision; implemented and CI-validated through PR #6.

## 2026-09-21 — D009

**分类：** PROTOCOL / FORM  
**决定：** 按当前 Inquiry Publishing Stack 对本项目执行升级：current AHICP `0.3.0-draft @ ed5a60b1016497472072db108072ace59bcdb65d` 作为当前协议入口，既有 HARC-lite 继续作为 project-native 历史治理层；采用 PPF `0.1.1-draft @ e660b48fb216c28c8faa1f0fe2d0816401e1de2c` 记录现有 GitHub Pages 生命周期，但不改变 provider、公开授权或 canonical QMD。现有 repository workflow / `gh-pages` 发布链已验证；provider-side Pages source/binding 与公网 runtime 验收继续作为独立外部 gate。Vault Interface 与 Starter 同步到当前 pinned revisions。  
**状态：** validated in PR #9; if this record is read from `main`, the upgrade is implemented. Provider-side Pages source/binding remains a separate unresolved external gate.  

