# Contributing to BZY C++ Notes

感谢你愿意为这份「现代 C++ 工程师手册」出力。本仓库的目标是：**以 C++ Primer 5e 的章节骨架为底，整合 C++17 主线 + C++20/23 实务，做一份每一页都是干货的速查手册。**

## 写作规则（硬约束）

1. **不删除原作者描述**。你可以润色、合并同义句、扩写——但不能让原 `legacy` 分支里的任何信息点消失。可以用 `python scripts/audit_chapter.py chapter/0X.*.md` 自检你的章节是否仍然保留 ≥ 0.9 的语义保真度。
2. **图形管道单源**：章节内插图用 mermaid（嵌入 ```mermaid``` 代码块）。跨章节 / 全局模块图统一存 `drawio/`，**`drawio/_mermaid/*.mmd` 是 canonical 源**，`drawio/*.svg` 是从 mermaid 导出的产物。如需可视化编辑：把 `.mmd` 内容粘到 [mermaid.live](https://mermaid.live) 后导出更新。不要再手写 `.drawio` XML。
3. **C++ 标准范围**：C++17 是主线；C++20/23 重点特性 (concepts / ranges / `<=>` / `std::format` / modules) 写在每章末尾的「现代 C++ 补丁」小节里，标注标准来源（cppreference 链接或 WG21 paper 编号，如 `P0515R3`）。
4. **代码示例**：必须 C++17 语法正确。重点示例附 [godbolt](https://godbolt.org/) 链接，链接里**保留 `source=...&compiler=...` 完整参数**而不是 `client.gd` 短链，防止 URL rot。不强制示例可独立编译运行。
5. **写作语言**：中文为主。`RAII / lvalue / rvalue / SFINAE / CRTP / ABI / RVO / NRVO / TMP` 等专业术语保留英文。
6. **文件名保留全角冒号 U+FF1A**（例：`02.第二章：对象与基本类型.md`）。所有跨文件链接里 `：` 必须 URL-encode 成 `%EF%BC%9A`。提交前跑 `python scripts/check_links.py <你修改的文件>` 验证。

## 章节级最小公共结构

每章必须包含：

| 段落 | 要求 |
|---|---|
| **顶部「一句话定义」** | 40–200 中文字，用 `>` 引用块或加粗短句；至少包含本章 1 个核心 API 或概念关键词 |
| **「章节知识框架」** | mermaid `graph TD` 或 `mindmap`，节点 8–25 个 |
| **主体** | 三选一形态：手册版 / 速查版 / 原理版（参考金样：第 2 / 第 9 / 第 13 章） |
| **末尾「易错点 / 现代 C++ 补丁」** | 5–10 条工程师常踩坑 + C++20/23 替代方案，每条引用标准来源 |
| **章末交叉链接** | 1–2 条 `[相关模块: → drawio/0X.svg](../drawio/0X.svg)` |

## 提交规范

- **Conventional Commits**：`feat:` / `feat(diagrams):` / `docs:` / `docs(chXX):` / `chore:` / `fix:` 。
- **每章一个 commit**，标题 `docs(chXX): rewrite with handbook structure`。
- **不要提交 `node_modules/`、`*.swp`、`.DS_Store`、`*.bak`**——`.gitignore` 已覆盖。
- 不要在本仓库做 `git push --force` 类操作。`main` 分支历史须保持线性 fast-forward。

## PR 流程

1. Fork → 在 fork 仓库新建特性分支，命名 `docs/chXX-section-name` 或 `feat/topic`。
2. 跑本地校验：

   ```bash
   python scripts/title_fidelity.py legacy chapter/0X.第X章：YY.md
   python scripts/audit_chapter.py chapter/0X.第X章：YY.md
   python scripts/check_links.py chapter/0X.第X章：YY.md
   ```

3. 提 PR，遵循 `.github/PULL_REQUEST_TEMPLATE.md` 的清单。
4. 一个章节优化 = 一个 PR。

## 验证脚本一览

| 脚本 | 作用 | 退出码 |
|---|---|---|
| `scripts/title_fidelity.py legacy <md>` | 章节标题对照 legacy 模糊匹配 | 0 = ≥95% / 1 = 不达标 |
| `scripts/audit_chapter.py <md>` | 输出章节 fidelity JSON 报告 | 0 = pass / 1 = fail |
| `scripts/check_links.py <file>` | URL 编码 round-trip + 链接可达 | 0 = clean / 1 = 有 broken |
| `scripts/anchor_set.py <md>` | 导出标题集合（README TOC 用） | 0 |

## Code of Conduct

参与本项目即同意遵守 [Contributor Covenant 2.1](./CODE_OF_CONDUCT.md)。
