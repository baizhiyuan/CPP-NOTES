## 变更概要
<!-- 一两句话说明本 PR 做了什么 -->

## 关联章节
- 章节文件：
- 关联 issue: #
- 关联模块（drawio）：

## 自检清单（请逐项勾选）

- [ ] 原作者表述未被删除（如有同义合并，已逐字核对信息点完整保留）
- [ ] `python scripts/title_fidelity.py legacy <chapter>` 通过（≥ 95%）
- [ ] `python scripts/audit_chapter.py <chapter>` 输出 `pass: true`，`fidelity_score ≥ 0.9`
- [ ] `python scripts/check_links.py <chapter>` 0 failure（全角冒号已 URL-encode）
- [ ] 顶部「一句话定义」段落字数 ∈ [40, 200] 且包含本章核心 API/概念
- [ ] 至少一个 mermaid 章节框架图
- [ ] 末尾「易错点 / 现代 C++ 补丁」小节存在，每条引用 cppreference 或 WG21 paper
- [ ] 代码示例 C++17 语法正确；重点示例附 godbolt 完整链接（非 client.gd 短链）
- [ ] 章末交叉链接 `[相关模块: → drawio/0X.svg](../drawio/0X.svg)` 已加
- [ ] Conventional Commit 前缀正确（`docs(chXX):` / `feat(diagrams):` / `chore:` / ...）

## 截图 / 渲染对比
<!-- 如改图表或排版，贴 mermaid 渲染结果或 HTML 站截图 -->

## 备注
<!-- 任何需要 reviewer 特别关注的点 -->
