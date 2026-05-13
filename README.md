# BZY C++ Notes · 现代 C++ 工程师手册

[![C++17](https://img.shields.io/badge/C%2B%2B-17-00599c?logo=cplusplus&logoColor=white)](https://en.cppreference.com/w/cpp/17)
[![Standards Coverage](https://img.shields.io/badge/coverage-C%2B%2B17%20%E2%86%92%2023-blue)](#features)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

> **一句话定位**：以 C++ Primer 5e 章节骨架为底，整合 C++17 主线 + C++20/23 实务，做一份**每一页都是干货**的在职工程师速查手册——14 章笔记 + 9 张知识体系图 + 一个单文件离线 HTML 站。

本项目是 [@baizhiyuan](https://github.com/baizhiyuan) 多年 C++ 学习笔记的「升级版」。我们把原稿的每一句话保留下来，再由 AI agent 扮演资深 C++ 专家：补现代标准、补对比表、补 godbolt 链接、补「易错点」小节。原始版本永久保留在 `legacy` 分支。

---

## ✨ 为什么读它 (Features)

1. **手册不是教材**：默认你已经写过 C++，知道循环和指针。每章直接进「速查表 / 工程实践 / 易错点」。
2. **C++17 主线 + 现代补丁**：主体 C++17，每章末尾「现代 C++ 补丁」小节列出 C++20/23 等价方案（concepts / ranges / `<=>` / `std::format` / modules），每条带 cppreference 链接或 WG21 paper 编号。
3. **图文并茂**：每章自带 mermaid 知识框架图；跨章节 9 张模块总图存 `drawio/`（mermaid 源 + SVG 导出，GitHub 原生渲染）。
4. **godbolt 全参数链接**：重点示例附保留 `source/compiler` 参数的完整 godbolt URL，不用短链——5 年后仍可点开。
5. **单文件离线 HTML**：`docs/CPP-NOTES.html` 双击即开、零构建、零网络也能读（mermaid CDN 失败时降级为代码块）。

---

## 📚 章节索引

C++ Primer 5e 的章节骨架（第 1 章合并入本 README）：

| # | 章节 | 模块 | 难度 |
|---|------|------|------|
| 2 | [第二章：对象与基本类型](./chapter/02.%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E5%AF%B9%E8%B1%A1%E4%B8%8E%E5%9F%BA%E6%9C%AC%E7%B1%BB%E5%9E%8B.md) | 01 类型系统 | ★ |
| 3 | [第三章：数组、vector与字符串](./chapter/03.%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9A%E6%95%B0%E7%BB%84%E3%80%81vector%E4%B8%8E%E5%AD%97%E7%AC%A6%E4%B8%B2.md) | 03 容器 | ★ |
| 4 | [第四章：表达式](./chapter/04.%E7%AC%AC%E5%9B%9B%E7%AB%A0%EF%BC%9A%E8%A1%A8%E8%BE%BE%E5%BC%8F.md) | 01 / 02 | ★★ |
| 5 | [第五章：语句](./chapter/05.%E7%AC%AC%E4%BA%94%E7%AB%A0%EF%BC%9A%E8%AF%AD%E5%8F%A5.md) | 02 控制流 | ★ |
| 6 | [第六章：函数](./chapter/06.%E7%AC%AC%E5%85%AD%E7%AB%A0%EF%BC%9A%E5%87%BD%E6%95%B0.md) | 04 函数 | ★★ |
| 7 | [第七章：深入IO](./chapter/07.%E7%AC%AC%E4%B8%83%E7%AB%A0%EF%BC%9A%E6%B7%B1%E5%85%A5IO.md) | 05 IO | ★★ |
| 8 | [第八章：动态内存管理](./chapter/08.%E7%AC%AC%E5%85%AB%E7%AB%A0%EF%BC%9A%E5%8A%A8%E6%80%81%E5%86%85%E5%AD%98%E7%AE%A1%E7%90%86.md) | 05 内存 | ★★ |
| 9 | [第九章：序列与关联容器](./chapter/09.%E7%AC%AC%E4%B9%9D%E7%AB%A0%EF%BC%9A%E5%BA%8F%E5%88%97%E4%B8%8E%E5%85%B3%E8%81%94%E5%AE%B9%E5%99%A8.md) | 03 容器 | ★★ |
| 10 | [第十章：泛型算法](./chapter/10.%E7%AC%AC%E5%8D%81%E7%AB%A0%EF%BC%9A%E6%B3%9B%E5%9E%8B%E7%AE%97%E6%B3%95.md) | 04 算法 | ★★ |
| 11 | [第十一章：类](./chapter/11.%E7%AC%AC%E5%8D%81%E4%B8%80%E7%AB%A0%EF%BC%9A%E7%B1%BB.md) | 06 OOP | ★★★ |
| 12 | [第十二章：类的进阶](./chapter/12.%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%EF%BC%9A%E7%B1%BB%E7%9A%84%E8%BF%9B%E9%98%B6.md) | 06 OOP | ★★★ |
| 13 | [第十三章：模板](./chapter/13.%E7%AC%AC%E5%8D%81%E4%B8%89%E7%AB%A0%EF%BC%9A%E6%A8%A1%E6%9D%BF.md) | 07 模板 | ★★★ |
| 14 | [第十四章：元编程](./chapter/14.%E7%AC%AC%E5%8D%81%E5%9B%9B%E7%AB%A0%EF%BC%9A%E5%85%83%E7%BC%96%E7%A8%8B.md) | 07 元编程 | ★★★ |
| 15 | [第十五章：其他的工具与技术](./chapter/15.%E7%AC%AC%E5%8D%81%E4%BA%94%E7%AB%A0%EF%BC%9A%E5%85%B6%E4%BB%96%E7%9A%84%E5%B7%A5%E5%85%B7%E4%B8%8E%E6%8A%80%E6%9C%AF.md) | 07 杂项 | ★★ |

> 文件名故意保留全角冒号 `：` (U+FF1A) 以兼容原稿。所有跨文件链接已 URL-encode（`%EF%BC%9A`），跑 `python scripts/check_links.py README.md` 自检。

---

## 🗺️ 知识体系入口

- **[全局知识汇总 docs/KNOWLEDGE_MAP.md](./docs/KNOWLEDGE_MAP.md)** — 9 模块拓扑 + 3 条学习路径 + 50+ 概念交叉索引
- **[drawio/ 知识图谱](./drawio/)** — 8 张模块总图 + 1 张全局图，mermaid `.mmd` canonical + SVG 导出
- **[docs/CPP-NOTES.html 离线站点](./docs/CPP-NOTES.html)** — 单文件巨页：侧栏导航 + 14 章 + 主题切换 + 客户端搜索（双击即开）
- **[drawio/CONCEPTS.md](./drawio/CONCEPTS.md)** — 术语 + 模块拓扑权威表，给 agent / 工具消费

---

## 🚀 快速开始

```bash
git clone https://github.com/baizhiyuan/CPP-NOTES.git
cd CPP-NOTES

# 离线 HTML（推荐入口）
open docs/CPP-NOTES.html        # macOS
xdg-open docs/CPP-NOTES.html    # Linux
start docs/CPP-NOTES.html       # Windows

# 仅看某一章
cat 'chapter/06.第六章：函数.md' | less

# 查具体概念在哪一章
python scripts/anchor_set.py docs/KNOWLEDGE_MAP.md | grep -i lambda
```

---

## 🛡️ 质量保障

每个章节升级 PR 必须通过：

```bash
python scripts/title_fidelity.py legacy <chapter>   # 标题对照 legacy ≥ 95%
python scripts/audit_chapter.py    <chapter>        # 语义保真 fidelity ≥ 0.9
python scripts/check_links.py      <chapter>        # 链接 URL-encode round-trip
bash   scripts/verify_all.sh                        # 全套检查一键跑
```

`legacy` 分支保留原始笔记的精确快照；任何升级版本都不能丢失原作者信息点。

---

## 🤝 贡献

欢迎补丁、新示例、修订错误。详见：

- [CONTRIBUTING.md](./CONTRIBUTING.md) — 写作规则、提交规范、PR 自检清单
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) — Contributor Covenant 2.1
- [.github/ISSUE_TEMPLATE/](./.github/ISSUE_TEMPLATE/) — 「报错」与「补充建议」两个模板
- [.github/PULL_REQUEST_TEMPLATE.md](./.github/PULL_REQUEST_TEMPLATE.md) — PR 自检清单

---

## 📜 致谢

- 原始笔记作者：[@baizhiyuan](https://github.com/baizhiyuan)（保留在 `legacy` 分支）
- 章节骨架参考：Stanley B. Lippman 等 *C++ Primer 5/e*
- 升级流水线：本项目通过 `oh-my-claudecode` autopilot pipeline 完成升级（deep-interview → omc-plan consensus → autopilot 三段式管道）

## 📄 License

[MIT](./LICENSE) © 2026 Zhiyuan Bai (baizhiyuan)
