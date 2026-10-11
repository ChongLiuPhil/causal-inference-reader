# 网页电子书排版统一：2026-10-11

本轮属于已授权的 FORM/阅读界面优化，参考 constructs-language-reference-logic 的 Quarto 阅读设置，并**不改变**正文、引用、公式、翻译、章节顺序、原有 Quarto 搜索、发布服务商或访问权限。

现有 _quarto.yml 的 HTML 阅读层新增：柔白、暖纸、浅绿、深夜主题；16–26px 字号（默认 19px）；三档行距、620/720/820px 版心、衬线/无衬线、专注、阅读进度、书签及恢复默认。偏好仅保存在浏览器 localStorage；Quarto 原生脚注与文献悬停仍由 Quarto 提供。手机端悬浮设置入口与已有语言导航分离。

阅读层来源：ChongLiuPhil/constructs-language-reference-logic 的 `web/reader-comfort.mjs`/`web/reader-comfort.css`；引用源 blob 分别为 `236482b864a8c54c0e9616b18afd38fc2f10c708` / `ae31acd3ca1c171b2308205c27a3a1362d0d5047`；本书仅追加 Quarto 样式适配，不再创建第二套论文或专著源。

验证：`node --test tests/reader-comfort.test.mjs`，原有 Quarto 完整 HTML 构建、来源/书目/链接校验、访问控制与部署回执。PR CI 成功不等于已验证线上浏览器；如涉及正式发布，仍以现有仓库 main-only 发布与真实运行状态为准。
