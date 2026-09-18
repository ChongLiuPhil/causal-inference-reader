# AGENTS.md — 因果推理深度读本协作契约

本项目采用受 Human–AI Research Collaboration Protocol 启发的轻量协作层。它不是对上游 HARC 的逐文件复制；项目只保留对长期维护这本 Quarto 读本有直接价值的机制。

## 1. 权威来源

- GitHub 仓库状态高于聊天记忆。
- `manuscript/*.qmd` 是唯一 canonical 正文。
- `_quarto.yml` 是全书章节顺序与当前渲染结构的实现真值。
- `references.bib` 是书目真值。
- 人类长期决定记录在 `core/DECISION_LOG.md`，稳定内容/形式约束分别进入 `CONTENT_CORE.md` 与 `FORM_CORE.md`。
- 当前任务状态进入 `docs/working-memory/`，不得长期只保存在聊天中。

## 2. 任务路由

对实质性请求先标记一个或多个类别：

- `CONTENT`：论点、定义、章节内容、范围、教学结构。
- `FORM`：书籍形式、Quarto、CSS、导航、输出格式、发布呈现。
- `PROTOCOL`：协作规则、工作流、批准、状态持久化。
- `SOURCE`：事实核验、文献、BibTeX、引文与证据。

不要把临时工具默认值升级为长期作者偏好。

## 3. 项目性质与作者责任

本项目首先是作者学习过程中对因果推理材料的整合、梳理和问题化组织，不要求把每一部分都包装成作者原创理论。

作者性主要体现在问题选择、材料组织、解释重心、概念区分、比较边界和最终判断。AI 可以广泛参与检索、核查、综合、重构和起草，但不能把自己生成的完整论证自动当成作者立场。

下列高影响修改需要作者明确接受后才能作为稳定正文方向或 Core 原则：

- 改变章节或全书的核心问题；
- 改变竞争理论之间的解释权重；
- 新增会被理解为作者哲学立场的强判断；
- 改变哲学研究、思想研究、思想史或哲学史材料在全书中的功能关系；
- 对跨传统比较作出强历史同源或规范性结论。

## 4. AI 提议与人类决定

AI 生成的新论点、新术语、新章节结构、新解释或新形式规则，在人类明确接受前只是提议。

高影响不确定性不得通过“最可能如此”自行消解。把它记录到 `docs/working-memory/task-plan.md` 的 Pending Human Decisions / Clarifications，再等待人类决定。

## 5. 内容修改要求

对事实性、历史性、方法学或理论性主张进行实质修改时：

1. 核对相关原始或高质量来源；
2. 保持引文与 `references.bib` 闭合；
3. 区分定义/数学结论、经验假设与价值判断；
4. 不把相关性、图结构、干预效应和实际因果归因相互替换；
5. 不把比较哲学专题描述为现代因果推断主线的历史先声，除非有明确证据支持；
6. 不把“某位哲学家说过什么”本身当成哲学论证的完成；需要说明它回答什么问题、依赖什么理由、如何受到反例或竞争方案的压力；
7. 历史性材料若主要承担哲学史、思想史或思想研究功能，应如实标明，不以“哲学”标签抹去研究类型差别。

## 6. 形式与发布要求

- 当前只构建 HTML。
- PR 必须完整渲染并验证，但不得覆盖生产站点。
- `main` push/merge 必须触发完整渲染与生产发布。
- 任何未来 PDF/EPUB/DOCX 都从同一 QMD 源生成。
- 禁止重新引入长期 LaTeX/TinyTeX/TikZ/dvisvgm 迁移链。
- 旧构建产物不得作为 canonical source 提交。
- 网页与未来电子出版的形式可以参考作者其他 Quarto book 项目，但不得因此复制项目特有的部署或治理层。

## 7. 完成定义

正文、引用、图片、导航或形式的生产改动只有同时满足以下条件才算完成：

1. canonical 源已修改；
2. source/governance checks 通过；
3. 完整 HTML render 通过；
4. PR 检查通过；
5. 合并到 `main` 后生产发布检查通过；
6. 公共 GitHub Pages 上实际验证相关页面。

仅“本地能 render”或“PR green”不等于生产改动完成。

## 8. Working Memory

每个较大工作循环或 handoff 前：

- 更新 `current-focus.md`：只保留当前阶段、目标、首要 blocker、立即下一步。
- 更新 `task-plan.md`：active tasks、next actions、blockers、pending decisions、backlog。
- 重要阶段完成后，将简要历史写入 `work-log.md`。

Work Log 用于回顾，不是每次接管都必须加载的上下文。

## 9. 写入纪律

高影响修改前 fresh-fetch 相关 canonical 文件。写入后，旧摘录视为 stale；后续继续依赖时重新读取最新 revision。

不要把 issue、PR 评论或聊天摘要自动当成规范决定；只有被明确提升到 Core / Decision Log / Working Memory 的内容才具有对应项目状态角色。
