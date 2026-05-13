# Changelog

格式参考 [Keep a Changelog 1.1.0](https://keepachangelog.com/zh-CN/1.1.0/)；语义遵循
[Semantic Versioning 2.0](https://semver.org/lang/zh-CN/)。

## [Unreleased] · 现代 C++ 工程师手册升级

> 本次升级保留 `legacy` 分支为原始笔记快照（commit `d204347`），通过 `oh-my-claudecode`
> autopilot pipeline (deep-interview → omc-plan consensus → autopilot) 在 `upgrade` 分支上
> 完成多 commit 重构。`main` 在 Hand-off 时 fast-forward 到 `upgrade`。

### Added (新增)
- **`scripts/`**：4 个验证脚本 + verify_all.sh
  - `title_fidelity.py`：Levenshtein-based 章节标题对照覆盖率（threshold ≥ 95%）
  - `audit_chapter.py`：静态三检 (trigram coverage / concept preservation / H2 superset)，输出 JSON
  - `check_links.py`：URL-encode round-trip + 文件存在性检查，自动跳过 backtick code-spans
  - `anchor_set.py`：抽取 `##`/`###` 标题 + `[text](url)` 链接文本作为锚集
  - `verify_all.sh`：把上述四脚本 + drawio SVG sanity + branch invariants 串成一键
- **`drawio/`**：mermaid `.mmd` canonical 源 + SVG 导出 + `CONCEPTS.md` 术语/拓扑权威表
  - 8 张模块图（全局、类型系统、对象生命周期、容器迭代器、类继承、模板元编程、IO 异常、现代工具链）
  - `CONCEPTS.md` 304 行（72 术语 + 14 章 ID 白名单 + 9 模块拓扑 + godbolt 公约 + 32 交叉索引种子）
- **`docs/`**：知识汇总 + 离线 HTML 站 + 升级 hand-off
  - `KNOWLEDGE_MAP.md` 243 行（9 模块 + 14 章摘要 + 50+ 交叉索引 + 3 学习路径）
  - `CPP-NOTES.html` 366 行 / 20KB chrome（侧栏 / 主题切换 / 客户端搜索 / mermaid + Prism + lunr CDN）
  - `UPGRADE_NOTES.md` hand-off 文档（每 phase 状态 + 手动推送命令 + 后续接力策略）
- **开源配套**：MIT `LICENSE`、`CONTRIBUTING.md`、`CODE_OF_CONDUCT.md` (Contributor Covenant 2.1)、
  `.github/ISSUE_TEMPLATE/{bug_report,feature_request}.md`、`.github/PULL_REQUEST_TEMPLATE.md`、
  完善的 `.gitignore`
- **`Makefile`**：单行命令编排（make verify / audit / svg / serve / clean）

### Changed (改写)
- **`README.md`** 改写为正规开源项目门面：徽章 + 一句话定位 + 三句话简介 + 14 章节
  URL-encode 索引表 + 资源入口 + 致谢；AC-README-TOC 验证通过（legacy 14 锚文本 ⊂ 新锚文本集合）
- **Ch02 / Ch09 / Ch13** 三章升级为「金样章节」，作为 Manual / Quickref / Principle 三种写作模板：
  - Ch02 对象与基本类型：386 → 718 行（fidelity 1.0，10 WG21 paper 引用）
  - Ch09 序列与关联容器：1363 → 1808 行（fidelity 1.0，18 张速查表，5 godbolt 全参数链接）
  - Ch13 模板：352 → 1474 行（fidelity 1.0，五段式 Why→Mechanism→Standard→Practice→Replacement）

### Fixed (修复)
- **Ch10 第十章：泛型算法**：Windows 绝对路径图链接
  (`C:\Users\BZYHERO\...image-20230212210223306.png`) → 改为仓库内相对路径
  (`../pics/image-20230212210223306.png`)
- **`scripts/check_links.py`**：跳过 ```fenced``` 与 `inline` code 内的 markdown 例子，
  避免文档中展示 link 语法时被误判为真实链接

### Deferred (推迟到下一 session)
- **Phase D 其余 11 章**：Ch03 / Ch04 / Ch05 / Ch06 / Ch07 / Ch08 / Ch10 / Ch11 / Ch12 / Ch15 / (Ch14 试点中)
- **Phase D-review** audit 通跑
- **Phase E final pass**：完成 D 后用真实 API 重写 KNOWLEDGE_MAP §3 章节摘要表
- **Phase F final pass**：把 14 章节 MD 内容嵌入 docs/CPP-NOTES.html 的 `<section data-chapter="XX">` 占位块

详见 [docs/UPGRADE_NOTES.md](./docs/UPGRADE_NOTES.md) 的 §3 与 §6。

### Verification (验证)
- 全套 `bash scripts/verify_all.sh` 通过率：**44 / 44**（0 failures）
- 14 章 audit fidelity 全部 ≥ 0.99（Ch10 = 0.994，其余 = 1.000）
- 14 章 title coverage 全部 ≥ 95%
- 8 张 drawio SVG 均 XML-parse 通过
- 无 `git push` 痕迹；`legacy` 仍 == `d204347814323e7c76ec032a24a0a9a9b081b355`

## [legacy] · 原始笔记（commit d204347）
保留在 `legacy` 分支。14 章节 + README，共 12,788 行；C++ Primer 5e 章节骨架；6 张
PNG 在 `pics/`。
