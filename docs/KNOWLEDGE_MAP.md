# CPP-NOTES Knowledge Map · 全景知识体系

> 整个项目的「鸟瞰图」。先看模块拓扑 → 再看学习路径 → 然后用交叉索引随查随用。
>
> Source of truth for terminology and module taxonomy: [`../drawio/CONCEPTS.md`](../drawio/CONCEPTS.md).
> Diagrams: see [`../drawio/`](../drawio/) (mermaid canonical → SVG export).

---

## §1 全局知识体系（mermaid）

> 顶层视图：14 个章节如何聚成 9 个模块、模块如何互相依赖。

```mermaid
graph TD
  subgraph Foundation[基础层]
    M01[01 类型系统<br/>Ch02 / Ch04]
    M02[02 语句与控制流<br/>Ch04 / Ch05]
  end
  subgraph Containers[数据与算法层]
    M03[03 容器与字符串<br/>Ch03 / Ch09]
    M04[04 函数与算法<br/>Ch06 / Ch10]
  end
  subgraph Runtime[运行时与 IO 层]
    M05[05 内存与 IO<br/>Ch07 / Ch08]
  end
  subgraph OOP[面向对象层]
    M06[06 类与 OOP<br/>Ch11 / Ch12]
  end
  subgraph Meta[模板与元编程层]
    M07[07 模板与元编程<br/>Ch13 / Ch14 / Ch15]
  end
  subgraph Modern[现代工具链 跨章节]
    M08[08 现代工具链<br/>C++17/20/23 索引]
  end

  M01 --> M02
  M01 --> M03
  M01 --> M04
  M02 --> M04
  M03 --> M04
  M01 --> M05
  M03 --> M05
  M01 --> M06
  M04 --> M06
  M06 --> M07
  M04 --> M07
  M08 -. 渗透到每个章节 .-> M01
  M08 -. .-> M02
  M08 -. .-> M03
  M08 -. .-> M04
  M08 -. .-> M05
  M08 -. .-> M06
  M08 -. .-> M07

  Global[00 全景导航] === M01 & M03 & M06 & M07 & M08
```

> 同样的图以 SVG 形式存于 [`../drawio/00.global-knowledge-map.svg`](../drawio/00.global-knowledge-map.svg) 供 HTML 站离线渲染。

---

## §2 9 个模块详解

> 每个模块嵌入对应 drawio SVG + 一段 ~200 字的角色说明 + 覆盖章节链接。
>
> SVG 由 mermaid-cli 从 `drawio/_mermaid/0X.*.mmd` 渲染产出；如需可视化编辑请参考 [`../drawio/README.md`](../drawio/README.md).

### M00 全景导航
- 角色：所有模块的目录与跳转面板，用作 HTML 站点的首屏导航。
- 模块图：[`../drawio/00.global-knowledge-map.svg`](../drawio/00.global-knowledge-map.svg)
- 关联章节：全部 14 章

### M01 类型系统 · Type System
- 角色：现代 C++ 的最小可用骨架——把「值类别」「const 正确性」「`auto/decltype` 推导」「`<=>` 三路比较」一次拉通。
- 模块图：[`../drawio/01.type-system.svg`](../drawio/01.type-system.svg)
- 关联章节：第 2 章（对象与基本类型）、第 4 章（表达式中类型相关部分）

### M02 语句与控制流 · Statements & Control Flow
- 角色：把 C 风格控制流过渡到现代 C++（`if constexpr` / `if-init` / range-for / `[[fallthrough]]`）。
- 模块图：[`../drawio/02.object-lifecycle.svg`](../drawio/02.object-lifecycle.svg)
  > _Note: `drawio/_mermaid/02.*.mmd` 的 slug 由 Phase C agent 决定，可能为 `02.statements.mmd` 或 `02.object-lifecycle.mmd`；Phase E 完成后链接以实际 SVG 命名为准。_
- 关联章节：第 4、5 章

### M03 容器与字符串 · Containers & Strings
- 角色：从 C 数组到 `std::vector / span / mdspan` 的演进；STL 容器选型矩阵。
- 模块图：[`../drawio/03.containers-iterators.svg`](../drawio/03.containers-iterators.svg)
- 关联章节：第 3、9 章

### M04 函数与算法 · Functions & Algorithms
- 角色：函数式接口 + 泛型算法。`std::function / lambda / bind / ranges` 全家桶。
- 模块图（占位）：将由 Phase C 产出于 `drawio/04.*.svg`
- 关联章节：第 6、10 章

### M05 内存与 IO · Memory & I/O
- 角色：`new/delete` → 智能指针 → 分配器；iostream 状态机 + `<format>` 现代替代。
- 模块图：[`../drawio/06.io-exceptions.svg`](../drawio/06.io-exceptions.svg)（slug 以实际产出为准）
- 关联章节：第 7、8 章

### M06 类与 OOP · Classes & OOP
- 角色：从「特殊成员函数五法则」到虚函数、RTTI、CRTP 的完整 OOP 视图。
- 模块图：[`../drawio/04.classes-inheritance.svg`](../drawio/04.classes-inheritance.svg)
- 关联章节：第 11、12 章

### M07 模板与元编程 · Templates & Metaprogramming
- 角色：模板基础 → SFINAE → C++20 Concepts；附带异常 / 命名空间 / 嵌套类等"碎片但工业必备"。
- 模块图：[`../drawio/05.templates-metaprogramming.svg`](../drawio/05.templates-metaprogramming.svg)
- 关联章节：第 13、14、15 章

### M08 现代工具链 · Modern Toolchain
- 角色：C++17/20/23 特性按主题索引；godbolt / cppinsights / clang-tidy / mermaid 工作流。
- 模块图：[`../drawio/07.modern-toolchain.svg`](../drawio/07.modern-toolchain.svg)
- 关联章节：跨章

---

## §3 14 章节摘要表

> 速查表。难度 ★ 入门 / ★★ 工程师 / ★★★ 专家。估时阅读 = 仔细读一遍的预计时间。
>
> _Phase E 自动填充：完成 Phase D 后，本表会由 audit-agent 重新生成关键 API + 难度评分。当前为占位版本。_

| 章 | 名称 | 关键词 | 难度 | 估时 | 主要 API |
|----|------|--------|------|------|----------|
| 02 | 对象与基本类型 | type / `const` / `auto` / 引用 / 指针 | ★ | 45 min | `int`, `size_t`, `const`, `constexpr`, `auto`, `decltype` |
| 03 | 数组、vector与字符串 | 数组退化 / `std::vector` / `std::string` | ★ | 50 min | `std::vector`, `std::string`, `std::array`, `std::span` |
| 04 | 表达式 | 值类别 / 运算符 / 求值顺序 / 转换 | ★★ | 70 min | `<=>`, `static_cast`, `dynamic_cast`, sequencing rules |
| 05 | 语句 | 控制流 / 异常 / `try` | ★ | 50 min | `if constexpr`, range-for, `[[fallthrough]]` |
| 06 | 函数 | 重载 / lambda / 返回类型推导 | ★★ | 100 min | `std::function`, `auto -> trailing return`, `noexcept` |
| 07 | 深入IO | iostream 状态机 / fstream / 格式化 | ★★ | 50 min | `std::cin/cout`, `std::ofstream`, `<format>` (C++20) |
| 08 | 动态内存管理 | `new` / 智能指针 / RAII | ★★ | 60 min | `std::unique_ptr`, `std::shared_ptr`, `std::weak_ptr`, `make_unique` |
| 09 | 序列与关联容器 | STL 容器矩阵 / 迭代器分类 | ★★ | 100 min | `std::map`, `std::unordered_map`, `std::deque`, `std::list` |
| 10 | 泛型算法 | `<algorithm>` / lambda / ranges | ★★ | 90 min | `std::sort`, `std::transform`, `std::ranges::*` |
| 11 | 类 | 特殊成员函数 / 构造析构拷贝移动 | ★★★ | 140 min | rule-of-five, `explicit`, `friend`, copy-and-swap |
| 12 | 类的进阶 | 继承 / 虚函数 / RTTI / CRTP | ★★★ | 110 min | `virtual`, `override`, `final`, `dynamic_cast` |
| 13 | 模板 | 函数/类模板 / SFINAE / Concepts | ★★★ | 70 min | `template`, `requires`, CTAD, deduction guides |
| 14 | 元编程 | TMP / `type_traits` / `if constexpr` | ★★★ | 55 min | `std::enable_if`, `std::void_t`, fold expressions |
| 15 | 其他的工具与技术 | 异常 / 枚举 / namespace / 位域 | ★★ | 55 min | `noexcept`, `enum class`, `inline namespace`, bitfields |

---

## §4 概念交叉索引

> 字母序。每行 = 概念 → 出现章节 → 所属模块。50+ 条来自 `../drawio/CONCEPTS.md` §2。

| 概念 | 出现章节 | 所属模块 |
|------|---------|---------|
| ABI / `extern "C"` | 06 | 08 |
| ADL (实参依赖查找) | 06, 11 | 04 / 06 |
| aggregate initialization / designated init (C++20) | 11 | 06 |
| alias template (`using`) | 13 | 07 |
| alignas / alignof | 02 | 01 |
| auto type deduction | 02, 06, 13 | 01 |
| bind / placeholders | 10 | 04 |
| concept (C++20) / requires | 13 | 07 / 08 |
| const / constexpr / consteval / constinit | 02, 04, 11 | 01 |
| copy elision / RVO / NRVO | 06, 11 | 06 |
| coroutine (C++20) | — | 08 |
| CRTP | 12, 13 | 06 / 07 |
| CTAD (C++17) | 13 | 07 |
| decltype / decltype(auto) | 02, 13 | 01 |
| dynamic_cast / RTTI | 12 | 06 |
| enable_if / void_t / SFINAE | 13, 14 | 07 |
| exception safety (basic/strong/no-throw) | 15 | 07 |
| explicit | 11, 12 | 06 |
| fold expression (C++17) | 13 | 07 |
| friend | 11 | 06 |
| function-try-block | 15 | 07 |
| inline / inline variable (C++17) | 06, 11 | 04 / 06 |
| iterator categories (input/forward/.../contiguous) | 10 | 04 |
| lambda (capture / mutable / generic / template) | 10 | 04 |
| lvalue / rvalue / xvalue / prvalue / glvalue | 04 | 01 |
| make_unique / make_shared | 08 | 05 |
| modules (C++20) | — | 08 |
| move / std::move / std::forward / 完美转发 | 11, 13 | 06 / 07 |
| name mangling | 06 | 08 |
| narrowing conversion | 04 | 01 |
| namespace (nested / anonymous / inline) | 15 | 07 |
| noexcept (operator / specifier) | 15 | 07 |
| nullptr / std::nullptr_t | 02 | 01 |
| object lifetime / storage duration | 02, 08 | 01 / 05 |
| operator overloading | 12 | 06 |
| pack expansion / variadic template / parameter pack | 13 | 07 |
| partial / full specialization | 13 | 07 |
| placement new | 08 | 05 |
| pointer-to-member (`->*`, `.*`) | 11, 12 | 06 |
| ranges (C++20) / views | 10 | 04 / 08 |
| RAII | 08, 11 | 05 / 06 |
| reference collapsing | 13 | 07 |
| smart pointers (unique/shared/weak) | 08 | 05 |
| spaceship (`<=>`, C++20) | 04, 12 | 01 / 06 |
| std::format (C++20) | 07 | 05 / 08 |
| std::span / std::mdspan | 03 | 03 / 08 |
| structured binding (C++17) | 02 | 01 |
| three-way comparison | 04, 12 | 01 / 06 |
| type_traits | 14 | 07 |
| typeid | 12 | 06 |
| `auto` in function returns (C++14) | 06 | 04 |
| `[[nodiscard]]` / `[[fallthrough]]` (C++17) | 05, 06 | 02 / 04 |

---

## §5 三条学习路径

### 路径 A · On-the-job 速查（≤ 2 小时初读，长期常驻 HTML 侧栏）
1. M01 类型系统：跳读，重点看 `const`/`auto`/value categories
2. M03 容器矩阵：第 9 章「9.0 容器全景速查表」直接抄走
3. M04 算法：第 10 章「ranges 对照表」
4. 遇到具体问题用 §4 索引按字母跳转

### 路径 B · 巩固型阅读（~12 小时，按章顺序，全员推荐）
```
Ch02 → Ch03 → Ch04 → Ch05 → Ch06 → Ch07 → Ch08
     → Ch09 → Ch10
     → Ch11 → Ch12
     → Ch13 → Ch14 → Ch15
```
读完后跑一遍每章末尾的「易错点 / 现代 C++ 补丁」自测。

### 路径 C · 深度原理（~20 小时，准备造轮子或写编译器友好代码）
```
Ch04 (表达式 + value category)
 → Ch11 (rule-of-five / copy-elision)
 → Ch12 (虚函数表 / RTTI)
 → Ch13 (two-phase lookup / SFINAE)
 → Ch14 (TMP / std::void_t / fold)
 → Ch08 (allocator / placement new)
 → Ch15 (异常机制 / function-try-block)
```
每节配合 godbolt `-fdump-class-hierarchy` / `-fdump-tree-original` 看编译器实际行为。

---

## §6 本表与 `drawio/CONCEPTS.md` 的差异

| 维度 | KNOWLEDGE_MAP（本文件） | CONCEPTS.md |
|------|------------------------|--------------|
| 受众 | 读者（HTML 站消费者） | 后续 agent / 工具（验证脚本） |
| 内容 | 摘要、学习路径、按需查阅 | 全量术语、ID 白名单、style guide |
| 同步 | 章节升级后 Phase E 重生成 | 一旦冻结即只追加，不修改 |
| 引用方向 | 单向引用 CONCEPTS.md | 不引用本文件 |

> 任何术语冲突以 CONCEPTS.md 为准。
