# Upgrade Notes · 升级状态与 Hand-off

> 由 `oh-my-claudecode:autopilot` 自动生成。记录本次 deep-interview → omc-plan consensus → autopilot 三段式升级管道的实际产出、剩余工作、以及推送命令。
>
> Source plan: `.omc/plans/cpp-notes-upgrade.md`（v3 共识版，Architect REVISE + Critic APPROVE-WITH-MINOR）
> Source spec: `.omc/specs/deep-interview-cpp-notes-upgrade.md`（歧义度 10%）

---

## 1. 已完成（落在 `upgrade` 分支，共 9 个 commit）

| Phase | 输出 | Commit | 状态 |
|---|---|---|---|
| A | `legacy` + `upgrade` 分支均指向 `d204347` | — | ✅ |
| A.5 | 4 验证脚本 (`title_fidelity.py` / `audit_chapter.py` / `check_links.py` / `anchor_set.py`) | `e22a5e3` | ✅ |
| B | 开源配套 (LICENSE MIT / CONTRIBUTING / CoC 2.1 / Issue+PR 模板 / .gitignore) | `287d0eb` + `d4edab6`(fix) | ✅ |
| C0 | mermaid-cli WSL smoke test PASS (10.7KB SVG via Chromium) | — | ✅ |
| B0-1 | `drawio/CONCEPTS.md` 304 行（72 术语 + 14 章 ID 白名单 + 9 模块拓扑 + godbolt 公约 + 32 交叉索引种子） | `a1a320d` | ✅ |
| C | 8 张 drawio 模块图：mermaid `.mmd` canonical (484 行) + 8 个 SVG (60-100KB) + `drawio/README.md` | `e738bbe` | ✅ |
| B0-2 | **Ch02 Manual** 金样：386 → **718 行**，fidelity 1.0，title 100%，10 个 WG21 paper 引用 | `aebc152` | ✅ |
| B0-3 | **Ch09 Quickref** 金样：1363 → **1808 行**，fidelity 1.0，title 100%，18 张速查表 + 5 godbolt | `d726a81` | ✅ |
| B0-4 | **Ch13 Principle** 金样（stub 扩写）：352 → **1474 行**，fidelity 1.0，title 100%，10 WG21 paper | `185bfc6` | ✅ |
| E (skeleton) | `docs/KNOWLEDGE_MAP.md` 243 行（9 模块表 + 14 章摘要 + 50 交叉索引 + 3 学习路径） | `f61752c` | 🟡 final pass 待跑 |
| F (chrome) | `docs/CPP-NOTES.html` 366 行 / 20KB（侧栏 / 主题 / 搜索 / mermaid+Prism / 14 占位 section） | `f61752c` | 🟡 章节内容嵌入待 Phase F final |
| G | `README.md` 改写（徽章 / 14 章节 URL-encode 索引 / 资源入口 / AC-README-TOC 通过） | `f61752c` | ✅ |
| Phase H draft | 本文件 (`docs/UPGRADE_NOTES.md`) | `f61752c` | ✅ |

**verify_all.sh 结果：43 / 44 PASS**（唯一未过：legacy chapter/10 嵌的 Windows 绝对路径图，pre-existing 数据问题，将在 Phase D Ch10 升级时清理）

## 2. 进行中（agents 后台）

| Phase | 文件 | 状态 |
|---|---|---|
| D-pilot | `chapter/14.第十四章：元编程.md` Principle-style 扩写（87→≥600） | 🔄 后台运行 |

## 3. 已设计但**未在本次 autopilot 中执行**

> 出于上下文预算与时间考虑，下列阶段保留完整提示词模板和分发策略，但**未跑全**。可由后续 session 接力（指令：`autopilot .omc/plans/cpp-notes-upgrade.md`）。

| Phase | 范围 | 预计耗时 |
|---|---|---|
| **D**（11 章其余精修） | Ch03 / Ch04 / Ch05 / Ch06 / Ch07 / Ch08 / Ch10 / Ch11 / Ch12 / Ch14 / Ch15 | 11 × ~8-15 分钟 |
| **D-review** | 独立 audit agent 对 14 章逐一评 fidelity，失败重跑 | ~30 分钟 |
| **F** | `docs/CPP-NOTES.html` 单文件巨页（含 Mermaid CDN / Prism / Lunr / Theme toggle / 14 章嵌入） | ~30-60 分钟 |
| **E final** | KNOWLEDGE_MAP §3 重写（结合 D 后的真实关键 API + 难度评分） | ~10 分钟 |
| **H push** | 用户手动执行（见下节） | — |

## 4. 验证现状

跑 `bash scripts/verify_all.sh -v` 当前结果（部分项目尚未完成时的预期）：

```
title_fidelity: chapter/02.* ✅  其它 13 个（含 09/13 升级前）= legacy 100% 匹配自己（trivially pass）
audit_chapter:  chapter/02.* ✅  其它 13 个 = legacy 与自己一致 = pass
check_links:    README.md 22/23 通过，仅 docs/CPP-NOTES.html 待 Phase F 落地
README TOC:     legacy 14 章节锚文本 ⊂ 新 README ✅
drawio SVG:     8/8 XML 解析通过 ✅
branch:         legacy = d204347 ✅；reflog 无 push ✅
```

## 5. Hand-off：用户手动推送

**在执行推送前请确认 `git log --graph --oneline --all` 看分支拓扑、`git diff legacy..main --stat` 看升级摘要**。

```bash
cd /mnt/i/bzy_ws/CPP-NOTES

# 步骤 1：把 upgrade 分支 fast-forward 到 main（本地操作，无 force）
git checkout main
git merge --ff-only upgrade

# 步骤 2：清理 worktree（如果有）
git worktree list
git worktree prune

# 步骤 3：推送两个分支到 GitHub（普通 push，无 --force-with-lease）
# legacy 分支是 GitHub 首次出现，远端 main 仍是 d204347（== 本地 legacy）
git push origin legacy

# main 分支是 d204347 的直系后代，fast-forward push，零 force
git push origin main

# 步骤 4（可选）：删除本地 upgrade 分支
git branch -d upgrade

# 步骤 5（可选）：启用 GitHub Pages
#   Settings → Pages → Source = main, /docs
#   访问 https://baizhiyuan.github.io/CPP-NOTES/CPP-NOTES.html
```

## 6. 后续接力策略

### Option A · 一次性把剩余 11 章升完
```bash
# 在新 session 里跑：
/oh-my-claudecode:autopilot .omc/plans/cpp-notes-upgrade.md
```
autopilot 会检测已有的金样和 CONCEPTS.md，跳过已完成阶段，从 Phase D 继续。

### Option B · 增量升级，每周 1-2 章
按 `chapter/XX.*.md` 顺序，每次 issue 一个 `chXX` 的 PR：
1. `/oh-my-claudecode:executor "用顶尖 C++ 专家身份重写 chapter/06.*.md，金样参考 chapter/02.*.md（Manual）"`
2. 跑 `bash scripts/verify_all.sh`
3. commit `docs(ch06): rewrite with handbook structure`

### Option C · 只产出 HTML 站，章节维持现状
若不再升级章节，直接 dispatch 一个 Phase F agent：
```
/oh-my-claudecode:executor "按 .omc/plans/cpp-notes-upgrade.md Phase F 规范，把所有 chapter/*.md 嵌入 docs/CPP-NOTES.html，参考 /mnt/i/bzy_ws/docs/claude-code/claude-code-setup.html"
```

## 7. 已知约束与设计选择

- **远端 main 不会被 force 覆写**：本地 `main` 始终 == `d204347` 直到 Phase H 步骤 1 才 fast-forward。
- **drawio 文件夹名保留**为兑现「需要一个专门的 drawio 文件夹」原话，但 canonical 源是 mermaid `.mmd`；想可视化编辑请把 `.mmd` 粘到 https://mermaid.live。
- **章节文件名全角冒号 U+FF1A 保留不动**，所有跨链接 URL-encode 成 `%EF%BC%9A`。
- **代码示例不强制可编译**，但要求 C++17 语法正确 + 重点示例 godbolt 全参数链接（防 client.gd 短链 rot）。
- **金样三章** (Ch02 / Ch09 / Ch13) 作为 Manual / Quickref / Principle 三个写作模板的锚点，后续 11 章 agent prompt 必读这三章作为 in-context 参考。

---

**生成于** 2026-05-14 by `oh-my-claudecode:autopilot` (deep-interview → omc-plan v3 consensus → autopilot)。

---

## 8. 本次 autopilot 收尾状态（最终快照）

- **Branches**:
  - `legacy` = `d204347814323e7c76ec032a24a0a9a9b081b355` （冻结）
  - `upgrade` = `8b42cb5e873bcb72bc0e0d59247c355a8eac9677` （14 commits ahead）
  - `main` = `8b42cb5e873bcb72bc0e0d59247c355a8eac9677` （已 fast-forward 到 upgrade，**未 push**）

- **Worktrees**:
  - `/mnt/i/bzy_ws/CPP-NOTES` → `upgrade` （Ch14 pilot agent 的工作树）
  - `/tmp/cpp-main` → `main` （用于 Phase H 隔离的 worktree，可在 hand-off 后 `git worktree remove /tmp/cpp-main`）

- **如果 Ch14 pilot agent 在 autopilot session 结束后才完成**：它的 commit 会落在 `upgrade` 分支末端。
  让 `main` 也包含它，在新 shell 里跑：
  ```bash
  cd /tmp/cpp-main
  git merge --ff-only upgrade
  ```

- **最终推送命令（与 §5 一致，重复一遍以便 copy-paste）**：
  ```bash
  cd /tmp/cpp-main          # 或 git checkout main
  git push origin legacy    # 远端首次出现 legacy 分支，普通 push
  git push origin main      # 远端 main 仍是 d204347；本地 main 是其直系后裔；fast-forward push，无 force
  ```

- **运行 `bash scripts/verify_all.sh`** 收尾验证：44/44 PASS（截至当前 commit `8b42cb5`，不含 Ch14 pilot 的 commit）。

- **下一步推荐**：
  1. 在浏览器 / VSCode 中点开 `docs/CPP-NOTES.html` 检查 chrome 是否符合预期；
  2. `git diff legacy..main --stat` 看升级摘要（应见 ~15 文件改动 + 几千行新增）；
  3. 若满意，跑 §5 的推送命令；
  4. 在新 session 跑 `/oh-my-claudecode:autopilot .omc/plans/cpp-notes-upgrade.md` 续上剩余 10+ 章节（除 14 之外，每章 ~10 分钟 / opus）。
