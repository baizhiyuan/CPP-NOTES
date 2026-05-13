# CPP-NOTES Knowledge Map Diagrams

This folder holds the **cross-chapter & global** knowledge maps for the CPP-NOTES project (Phase C output).

## Canonical source

`drawio/_mermaid/*.mmd` are the **single source of truth**. SVGs in this folder are generated outputs — never hand-edit them.

To regenerate a single map after editing its `.mmd`:

```bash
npx -y -p @mermaid-js/mermaid-cli mmdc \
  -i drawio/_mermaid/01.type-system.mmd \
  -o drawio/01.type-system.svg \
  --backgroundColor white
```

The folder is named `drawio/` for historical/legacy reasons. If you ever want a `.drawio` XML for visual editing in [diagrams.net](https://app.diagrams.net), paste the `.mmd` content into <https://mermaid.live> and export — but **do not** commit a `.drawio` that diverges from the corresponding `.mmd`.

## Module ↔ Chapter Mapping

Authoritative copy of `drawio/CONCEPTS.md` §1 (8 modules, chapters 02–15).

| Module | Module name (中文 · English) | Chapters | One-line scope |
|--------|------------------------------|----------|----------------|
| 00 | Global Knowledge Map · 全景导航 | all 02–15 | bird's-eye view linking all 7 modules; drives `docs/KNOWLEDGE_MAP.md` §1 |
| 01 | Type System · 类型系统 | 02, 04 | 内建/复合类型、`const/constexpr/consteval`、引用/指针、`auto/decltype`、类型转换、`<=>` 三路比较 |
| 02 | Statements & Control Flow · 语句与控制流 | 04, 05 | 表达式、运算符、求值顺序、流程控制、范围-for、初始化语句、`if constexpr` |
| 03 | Containers & Strings · 容器与字符串 | 03, 09 | 数组、`std::vector/string/array/span`、序列容器/关联容器/无序容器、迭代器分类 |
| 04 | Functions & Algorithms · 函数与算法 | 06, 10 | 形参传递、重载、引用折叠、Lambda、`std::function/bind`、泛型算法、`<execution>` 并发策略、ranges 概览 |
| 05 | Memory & I/O · 内存与 IO | 07, 08 | `new/delete`、智能指针 (`unique_ptr/shared_ptr/weak_ptr`)、分配器、流类层次、文件/字符串流、格式化、`<chrono>` 计时 |
| 06 | Classes & OOP · 类与面向对象 | 11, 12 | 数据成员/方法、访问控制、构造/析构/拷贝/移动、运算符重载、继承、虚函数、RTTI、特殊成员合成 |
| 07 | Templates & Metaprogramming · 模板与元编程 | 13, 14, 15 | 函数/类模板、CTAD、特化与偏特化、Concepts、变长模板、SFINAE、`type_traits`、异常、枚举/联合、嵌套/局部类、命名空间、位域、`volatile` |
| 08 | Modern Toolchain · 现代工具链 (cross-cutting) | 02–15 | C++17/20/23 feature index; godbolt 链接公约；`cppinsights` / `clang-tidy` / `mermaid` 流程；`<format>` / `<ranges>` / `modules` / `coroutine` 速查 |

> Note: the eight `.mmd` files in `_mermaid/` are numbered **00..07** (zero-based) to match the Phase C deliverable list. The mapping to `CONCEPTS.md` module IDs is: `00 → 00 Global`, `01 → 01 Type System`, `02 → 05 Memory (lifecycle subset)`, `03 → 03 Containers`, `04 → 06 Classes`, `05 → 07 Templates`, `06 → 05/07 IO + Exceptions`, `07 → 08 Modern Toolchain`. Module **02 Statements** content is embedded inside `00.global-knowledge-map.mmd` and the chapter-level mermaid blocks in `chapter/05.md` per the Phase D contract.

## Files

| File | Purpose |
|------|---------|
| `_mermaid/00.global-knowledge-map.mmd` → `00.global-knowledge-map.svg` | High-density 40+ node global map (all 8 modules + cross-module bridges) |
| `_mermaid/01.type-system.mmd` → `01.type-system.svg` | int/float/cv-qual/pointer/reference/auto/decltype/typedef-vs-using/nullptr/size_t/`<=>` |
| `_mermaid/02.object-lifecycle.mmd` → `02.object-lifecycle.svg` | stack/heap/new-delete/smart pointers/ctor-dtor chain/RAII/move semantics/RVO/NRVO |
| `_mermaid/03.containers-iterators.mmd` → `03.containers-iterators.svg` | `std::vector/array/deque/list/map/unordered_map` + iterator categories + ranges |
| `_mermaid/04.classes-inheritance.mmd` → `04.classes-inheritance.svg` | class/struct/access/friend/inheritance/virtual/abstract/multi-inheritance/virtual-base/CRTP |
| `_mermaid/05.templates-metaprogramming.mmd` → `05.templates-metaprogramming.svg` | function/class/variable/alias templates + SFINAE + concepts + TMP + `if constexpr` + variadic + CTAD |
| `_mermaid/06.io-exceptions.mmd` → `06.io-exceptions.svg` | iostream hierarchy/stream state/fstream/sstream/exception/try-catch/noexcept/`std::expected` |
| `_mermaid/07.modern-toolchain.mmd` → `07.modern-toolchain.svg` | C++17/20/23 features by category + compilers + godbolt + build systems + sanitizers + clang-tidy |

## Style baseline

All mermaid sources follow the rules in `drawio/CONCEPTS.md` §4:

- `graph TD` direction (top-down)
- Node labels: 中文短语 + `(English term)` when a standard English term exists; acronyms (RAII, SFINAE, CRTP, ADL, RTTI, RVO) keep English only.
- Edge labels: ≤ 6-character Chinese action verbs (e.g. `继承`, `推导出`, `转换为`, `触发`).
- 8–25 nodes per module map (`00.global` may exceed 40).
- No hard-coded `style`/`classDef` — default theme keeps the Phase F single-file HTML portable.

## Re-render everything

```bash
cd /mnt/i/bzy_ws/CPP-NOTES
for f in drawio/_mermaid/*.mmd; do
  out="drawio/$(basename "$f" .mmd).svg"
  npx -y -p @mermaid-js/mermaid-cli mmdc -i "$f" -o "$out" --backgroundColor white
done
```

If puppeteer Chromium is missing on a fresh machine, run the smoke loop once: it caches the browser under `~/.cache/puppeteer` and subsequent renders reuse it.

## Validation

Every SVG is validated by parsing as XML:

```bash
python3 -c "import xml.etree.ElementTree as ET, glob; [ET.parse(f) for f in glob.glob('drawio/*.svg')]; print('OK', len(glob.glob('drawio/*.svg')), 'SVGs')"
```

Expected output: `OK 8 SVGs`.
