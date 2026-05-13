# CPP-NOTES Concept Inventory & Module Taxonomy

> Generated 2026-05-14 by autopilot Phase B0-1. **Frozen reference.** Downstream agents (Phase C drawio module maps, Phase D 11 chapter agents, Phase D-review `scripts/audit_chapter.py`, Phase E `KNOWLEDGE_MAP.md`) must use these names **verbatim**. Source: actual content of `chapter/02..15.md` (12,788 lines) on branch `upgrade`.

---

## 1. Global Module Taxonomy (7 modules + 1 global)

| ID | Module name (中文) | Covers chapters | One-line scope |
|----|--------------------|-----------------|----------------|
| 00 | Global Knowledge Map · 全景导航 | all 02–15 | bird's-eye view linking all 7 modules; drives `docs/KNOWLEDGE_MAP.md` §1 |
| 01 | Type System · 类型系统 | 02, 04 | 内建/复合类型、`const/constexpr/consteval`、引用/指针、`auto/decltype`、类型转换、`<=>` 三路比较 |
| 02 | Statements & Control Flow · 语句与控制流 | 04, 05 | 表达式、运算符、求值顺序、流程控制、范围-for、初始化语句、`if constexpr` |
| 03 | Containers & Strings · 容器与字符串 | 03, 09 | 数组、`std::vector/string/array/span`、序列容器/关联容器/无序容器、迭代器分类 |
| 04 | Functions & Algorithms · 函数与算法 | 06, 10 | 形参传递、重载、引用折叠、Lambda、`std::function/bind`、泛型算法、`<execution>` 并发策略、ranges 概览 |
| 05 | Memory & I/O · 内存与 IO | 07, 08 | `new/delete`、智能指针 (`unique_ptr/shared_ptr/weak_ptr`)、分配器、流类层次、文件/字符串流、格式化、`<chrono>` 计时 |
| 06 | Classes & OOP · 类与面向对象 | 11, 12 | 数据成员/方法、访问控制、构造/析构/拷贝/移动、运算符重载、继承、虚函数、RTTI、特殊成员合成 |
| 07 | Templates & Metaprogramming · 模板与元编程 | 13, 14, 15 | 函数/类模板、CTAD、特化与偏特化、Concepts、变长模板、SFINAE、`type_traits`、异常、枚举/联合、嵌套/局部类、命名空间、位域、`volatile` |
| 08 | Modern Toolchain · 现代工具链 (cross-cutting) | 02–15 | C++17/20/23 feature index; godbolt 链接公约；`cppinsights` / `clang-tidy` / `mermaid` 流程；`<format>` / `<ranges>` / `modules` / `coroutine` 速查 |

> **Cluster name discipline:** Phase C drawio files must reuse the IDs `00..08` and the bilingual names exactly. Sub-clusters within a module diagram are free-form but should reference the chapter numbers they cover.

---

## 2. Terminology Table (sorted alphabetically by English term, 70+ rows)

| English | 中文 | Notes / typical use |
|---------|------|---------------------|
| ABI | 应用二进制接口 | 不翻译；与 `extern "C"`、name-mangling 一起出现 |
| ADL (Argument-Dependent Lookup) | 实参依赖查找 | 不翻译缩写；Ch06、Ch11 友元函数 |
| aggregate initialization | 聚合初始化 | Ch11；C++20 designated initializer |
| alias template | 别名模板 | `using` 引入；Ch13 |
| alignas / alignof | 对齐限定 / 对齐查询 | Ch02 |
| auto type deduction | auto 类型推导 | Ch02、Ch06、Ch13 |
| bind / placeholders | 绑定 / 占位符 | `std::bind`, `std::placeholders::_1`；Ch10 |
| CRTP | 奇异递归模板模式 | 不翻译；Ch12/Ch13 |
| CTAD (Class Template Argument Deduction) | 类模板实参推导 | C++17；Ch13；含 user-defined deduction guide |
| concept (C++20) | 概念约束 | "concept" 不翻译；与 `requires` 从句配合 |
| const / constexpr / consteval / constinit | const/常量表达式/即时函数/常量初始化 | Ch02、Ch04、Ch11 |
| coroutine (C++20) | 协程 | C++20；Module 07 速查项 |
| dangling reference | 悬空引用 | Ch02、Ch06 |
| decltype / decltype(auto) | decltype 类型推导 | Ch02、Ch13 |
| deduction guide | 推导指引 | Ch13 CTAD 配套 |
| designated initializer (C++20) | 指派初始化器 | Ch11 |
| dynamic_cast / static_cast / reinterpret_cast / const_cast | 四种命名转换 | Ch04、Ch12 |
| ellipsis / parameter pack | 省略号 / 参数包 | Ch13 变长模板 |
| enable_if / void_t | 启用判定 / void 探测 | Ch13、Ch14 SFINAE |
| exception safety | 异常安全 | Ch15；basic / strong / no-throw 三级 |
| explicit | 显式 | Ch11 单参构造、Ch12 转换运算符 |
| extern "C" | C 语言链接 | Ch06 函数链接、ABI |
| fold expression (C++17) | 折叠表达式 | Ch13；包展开的运算符折叠 |
| friend | 友元 | Ch11 访问控制 |
| function-try-block | 函数级 try 块 | Ch15 异常处理；构造函数初始化列表保护 |
| inline / inline variable (C++17) | 内联函数 / 内联变量 | Ch06、Ch11 静态成员 |
| iterator categories | 迭代器分类 | Ch10；input/output/forward/bidirectional/random-access/contiguous |
| lambda expression | Lambda 表达式 | Ch10；闭包类型、捕获、`mutable`、generic lambda (C++14)、template lambda (C++20) |
| literal type / structural type | 字面值类型 / 结构化类型 | Ch11；编译期常量 |
| lvalue / rvalue / xvalue / prvalue / glvalue | 左值/右值/将亡值/纯右值/泛左值 | 保留英文；Ch04 表达式值类别 |
| make_unique / make_shared | 工厂函数 | Ch08；推荐用法 |
| member pointer (`->*`, `.*`) | 成员指针 | Ch11、Ch12 |
| modules (C++20) | 模块 | C++20 编译单元；Module 07 速查 |
| move semantics / std::move / std::forward | 移动语义 / 转发 | Ch11 移动构造、Ch13 完美转发 |
| name mangling | 名称修饰 | Ch06；`_Z3Addii` 类样式 |
| narrowing conversion | 窄化转换 | Ch04 |
| nested / anonymous namespace | 嵌套/匿名命名空间 | Ch15 |
| nested / local class | 嵌套类 / 局部类 | Ch15 |
| noexcept | 不抛出限定 / 操作符 | Ch15；可作为限定符或操作符 |
| nullptr / std::nullptr_t | 空指针字面值 | Ch02 |
| object lifetime / storage duration | 对象生存期 / 存储期 | Ch02、Ch08；automatic / static / thread / dynamic |
| operator overloading | 运算符重载 | Ch12 |
| partial / full specialization | 偏特化 / 完全特化 | Ch13 |
| perfect forwarding | 完美转发 | Ch13；万能引用 + `std::forward` |
| placement new | 定位 new | Ch08 |
| pointer-to-member / pointer-to-member-function | 数据成员指针 / 成员函数指针 | Ch11、Ch12 |
| RAII | 资源获取即初始化 | 不翻译；Ch08 智能指针、Ch11 构造析构 |
| ranges (C++20) | 范围 | "ranges" 不翻译；Ch10 范围算法 + view |
| reference collapsing | 引用折叠 | Ch13；与万能引用、`std::forward` 配合 |
| RTTI (`typeid`, `dynamic_cast`) | 运行时类型识别 | Ch12 |
| RVO / NRVO | 返回值优化 / 具名 RVO | 不翻译；Ch06、Ch11 |
| SFINAE | 替换失败非错误 | 不翻译；Ch13、Ch14 |
| size_t / ptrdiff_t / nullptr_t | 标准整型别名 | Ch02、Ch03 |
| spaceship operator (`<=>`) | 三路比较运算符 | C++20；Ch04、Ch12 |
| std::format / std::print (C++20/23) | 格式化输出 | Ch07；可选替代 `printf` |
| structured binding (C++17) | 结构化绑定 | Ch09、Ch04 |
| tag dispatch | 标签分派 | Ch10 迭代器、Ch14 |
| three-way comparison | 三路比较 | Ch04、Ch12 |
| TMP (Template Metaprogramming) | 模板元编程 | 不翻译；Ch14 |
| trailing return type | 尾置返回类型 | Ch06 `auto fn() -> T` |
| translation unit / ODR (One Definition Rule) | 翻译单元 / 一处定义原则 | Ch06、Ch11、Ch13 |
| type alias / using directive | 类型别名 / using 指令 | Ch02、Ch15 |
| type erasure | 类型擦除 | Ch10 `std::function`、Ch08 删除器 |
| type traits | 类型萃取 | `<type_traits>`；Ch14 |
| unevaluated context | 未求值语境 | Ch04 `sizeof/decltype/noexcept` 内部 |
| union / variant | 联合 / 变体 | Ch15；C++17 `std::variant` 安全替代 |
| universal / forwarding reference | 万能引用 / 转发引用 | Ch13 |
| value category | 值类别 | Ch04 |
| variadic template | 变长模板 | Ch13 |
| vexing parse | 烦人解析 | Ch11 默认构造 `T t();` |
| virtual / override / final | 虚 / 重写 / 终止 | Ch12 |
| virtual inheritance / virtual base | 虚继承 / 虚基类 | Ch12 |
| void* | 通用指针 | Ch02 |
| volatile | 易变限定 | Ch15 |

---

## 3. Key Identifiers Per Chapter (audit_chapter.py inputs)

> Each chapter agent **MUST** preserve these literal identifiers; `scripts/audit_chapter.py` greps for them. `// future:` marks tokens the upgrade pass is expected to introduce (stub chapters only).

### Ch02 对象与基本类型 (386 lines, full)
- `int`, `unsigned`, `long long`, `char`, `signed char`, `unsigned char`, `bool`, `float`, `double`, `long double`, `size_t`, `ptrdiff_t`
- `const`, `constexpr`, `consteval` `// future:`, `constinit` `// future:`, `auto`, `decltype`, `using`, `typedef`
- `nullptr`, `std::nullptr_t`, `void*`, reference (`&`), rvalue-reference `// future:`
- `sizeof`, `alignof`, `alignas`
- `std::numeric_limits`, `std::cout`, `std::endl`, `std::cin`, `std::is_same_v`, `std::integral`

### Ch03 数组、vector与字符串 (711 lines, full)
- C array, `[]`, multi-dimensional array, decay to pointer
- pointer arithmetic, `std::begin/std::end`, range-for
- C-string, `\0`, `strlen`, `strcmp`
- `std::vector`, `std::string`, `std::array` `// future:`, `std::span` `// future:`
- `size_type`, `iterator`, `push_back`, `emplace_back`

### Ch04 表达式 (987 lines, full)
- value category: lvalue, rvalue, xvalue, prvalue, glvalue
- integral promotion, floating-point promotion, numeric conversion, narrowing
- operator precedence, sequence point / sequenced-before
- `static_cast`, `dynamic_cast`, `reinterpret_cast`, `const_cast`
- `std::move`, `std::partial_ordering`, `std::strong_ordering`, `std::weak_ordering`
- `<=>` (three-way), `sizeof`, `decltype`, `consteval`

### Ch05 语句 (1004 lines, full)
- `if`, `else`, `switch`, `case`, `default`, `if constexpr` (C++17), `if`-init / `switch`-init (C++17), `if consteval` `// future:`
- `while`, `do-while`, `for`, range-`for` (C++11), range-`for` init (C++20)
- `break`, `continue`, `goto`, label, `return`
- `std::initializer_list`, `std::allocator`, `std::basic_string`, `std::vector`

### Ch06 函数 (1560 lines, full)
- function declaration / definition, ODR, inline function
- parameter passing (by value / reference / pointer / const-ref), default args
- function overload resolution, name mangling, `extern "C"`
- trailing return type, `auto`, `decltype(auto)`, `constexpr`/`consteval` function
- function pointer, `std::function`, lambda, recursion, ADL
- RVO / NRVO, copy elision (C++17 guaranteed)

### Ch07 深入IO (727 lines, full)
- `std::basic_istream`, `std::basic_ostream`, `std::cin`, `std::cout`, `std::cerr`, `std::clog`
- `std::ifstream`, `std::ofstream`, `std::fstream`, `std::stringstream`, `std::istringstream`, `std::ostringstream`
- `std::ios_base`, `std::ios::sync_with_stdio`, `std::ios_base::failure`, `failbit/badbit/eofbit/goodbit`
- formatting: `std::boolalpha`, `std::fixed`, `std::setw`, `std::setprecision`, `std::quoted`, `std::flush`
- `std::format` `// future:`, `std::print` `// future:`

### Ch08 动态内存管理 (825 lines, full)
- `new`, `delete`, `new[]`, `delete[]`, placement-new, `std::nothrow`
- `std::unique_ptr`, `std::shared_ptr`, `std::weak_ptr`, `std::make_unique`, `std::make_shared`
- `std::default_delete`, custom deleter, `std::enable_shared_from_this`
- `std::allocator`, `std::allocator_traits`, `std::pmr` `// future:`

### Ch09 序列与关联容器 (1363 lines, full)
- `std::vector`, `std::list`, `std::forward_list`, `std::deque`, `std::array`, `std::basic_string`
- `std::set`, `std::map`, `std::multiset`, `std::multimap`
- `std::unordered_set`, `std::unordered_map`, `std::unordered_multiset`, `std::unordered_multimap`
- container adaptor: `std::stack`, `std::queue`, `std::priority_queue`
- `std::pair`, `std::tuple`, structured binding, `node_handle` (C++17) `// future:`

### Ch10 泛型算法 (1289 lines, full)
- iterator categories: input/output/forward/bidirectional/random-access/contiguous (C++20)
- `std::find`, `std::copy`, `std::copy_if`, `std::accumulate`, `std::partial_sum`, `std::transform`, `std::sort`, `std::is_permutation`
- inserter family: `std::back_inserter`, `std::front_inserter`, `std::inserter`, `std::ostream_iterator`, `std::istream_iterator`
- `std::iterator_traits`, sentinel (C++20), `std::ranges` `// future:`, `std::execution::seq/par/par_unseq` (C++17)
- callable: function pointer, `std::function`, `std::bind`, `std::bind_front` (C++20), lambda, `std::placeholders`

### Ch11 类 (1931 lines, full)
- `struct` / `class`, incomplete type, member declaration, in-class member initializer (C++11)
- `mutable`, static data member, `inline` static member (C++17)
- access specifier: `public` / `private` / `protected`, `friend`
- special members: default ctor, copy ctor, move ctor (C++11), copy assign, move assign, dtor
- `=default`, `=delete`, member initializer list, delegating constructor
- literal class, `constexpr` constructor, member pointer (`.*`, `->*`), `std::bind` interop

### Ch12 类的进阶 (1446 lines, full)
- `operator` overloading: member vs non-member, conversion operator, `explicit operator T()`
- `<=>` spaceship operator and `= default` comparisons (C++20)
- inheritance: `public/protected/private` base, slicing
- `virtual`, `override`, `final`, pure virtual (`= 0`), abstract class
- vtable, vptr, virtual destructor, virtual inheritance / virtual base
- `dynamic_cast`, `typeid`, RTTI
- special members under inheritance, multiple inheritance, diamond problem

### Ch13 模板 (352 lines, partial — heavy upgrade expected)
- `template`, `typename`, `class` template parameter, non-type template parameter (NTTP)
- function template, class template, member template, friend template
- explicit instantiation (`template void f<int>(int)`), `extern template`
- full specialization (`template<>`), partial specialization
- CTAD, deduction guide (C++17)
- `concept`, `requires` clause, `requires` expression (C++20)
- variadic template, parameter pack, `sizeof...`, fold expression (C++17)
- universal/forwarding reference, `std::forward`, reference collapsing
- alias template (`using`), variable template (C++14)
- `typename` / `template` disambiguation for dependent names
- `// future:` `auto`-templated function (C++20), `requires`-clause on members, lambda templates (C++20)

### Ch14 元编程 (87 lines, stub — heavy upgrade expected)
- `<type_traits>`, `std::is_same`, `std::remove_reference`, `std::remove_cv`, `std::add_const`
- `std::true_type`, `std::false_type`, `std::integral_constant`
- `std::enable_if`, `std::enable_if_t`, `std::void_t` (C++17), `std::conditional`, `std::conjunction`, `std::disjunction`
- `if constexpr` (C++17), tag dispatch
- compile-time recursion, Erwin Unruh prime example
- `// future:` `constexpr if` patterns, concept-based dispatch (C++20), `std::is_constant_evaluated()` (C++20), `consteval` blocks

### Ch15 其他的工具与技术 (120 lines, stub — moderate upgrade)
- exception handling: `try`, `catch`, `throw`, stack unwinding, `terminate`
- `noexcept` (specifier + operator), `function-try-block`, exception object
- standard exceptions: `std::exception`, `std::runtime_error`, `std::logic_error`, `std::bad_alloc`, `std::out_of_range`
- `enum`, scoped `enum class` (C++11), underlying type
- `union`, anonymous union, `std::variant` `// future:`
- nested class, local class
- nested namespace (C++17 simplified `A::B::C`), anonymous namespace, `using` directive
- bit-field, `volatile`, `std::atomic` `// future:` as `volatile` replacement

---

## 4. mermaid Style Baseline

All Phase D chapter agents and Phase E `KNOWLEDGE_MAP.md` **MUST** follow:

- **Direction:** `graph TD` (top-down) is default for hierarchy/taxonomy diagrams; use `graph LR` only for control-flow / state machines / pipeline arrows.
- **Allowed chart types:** `graph TD/LR`, `flowchart TD`, `mindmap`, `classDiagram`, `stateDiagram-v2`. Avoid `gantt` / `journey`.
- **Node naming:** short noun phrase in 中文; if a standard English term exists, append in parentheses, e.g. `泛左值 (glvalue)`. Acronyms (RAII, SFINAE, CRTP, ADL, RTTI, RVO) keep English only.
- **Edge labels:** action verb in 中文, ≤ 6 字, e.g. `继承`, `推导出`, `转换为`, `触发`.
- **Node count:** 8–25 per chapter mermaid; if > 25 split into sub-graphs with `subgraph` cluster.
- **IDs:** ASCII only, prefer chapter-prefixed (`c06_lambda`, `c11_ctor`); use `&nbsp;` inside `[ ]` only when essential.
- **Colors:** avoid hard-coded `style` unless `classDef` is reused; rely on default theme so the single-file HTML stays portable.
- **Validation:** every mermaid block must render under `mermaid-cli` (`mmdc`) without errors — Phase C0 smoke test is the contract.

---

## 5. godbolt Link Format

Each chapter agent must include **2–5 full-parameter godbolt links** (NOT `client.gd` shortlinks). The canonical template (x86-64 gcc 14.2, C++17) is:

```
https://godbolt.org/?source=#g:!((g:!((g:!((h:codeEditor,i:(filename:'1',fontScale:14,fontUsePx:'0',j:1,lang:c%2B%2B,...))),k:50,l:'4',n:'0',o:'',s:0,t:'0'),(g:!((h:compiler,i:(compiler:g142,filters:(...),lang:c%2B%2B,libs:!(),options:'-std%3Dc%2B%2B17',source:1),l:'5',n:'0',o:'+x86-64+gcc+14.2+(C%2B%2B,+Editor+%231)',t:'0')),k:50,l:'4',n:'0',o:'',s:0,t:'0')),l:'2',n:'0',o:'',t:'0'),version:4
```

Rules:
- Prefer one godbolt link per **major sub-topic** (e.g. one per `##` heading).
- Default compiler `g142` (gcc 14.2). For C++20 features (`<=>`, concepts) switch to `-std=c++20`; for C++23 (e.g. `std::print`) use `-std=c++2b` with clang `clang_trunk` if gcc lacks support.
- Always paste a **non-trivial** but **self-contained** example that compiles cleanly.
- For Concepts / ranges / modules / coroutines, include an explanatory comment block at the top of the snippet.
- The chapter agent must **inline the URL on its own line** so the Phase F single-file HTML can rewrite it to `<a href=...>` automatically.

---

## 6. Cross-chapter Concept Index Seed (alphabetic, 32 rows)

> Seed for Phase E `KNOWLEDGE_MAP.md` §4 — KNOWLEDGE_MAP will expand to 50+ rows.

| Concept | Chapters | Module |
|---------|----------|--------|
| ADL (Argument-Dependent Lookup) | 06, 11 | 06 Classes / 04 Functions |
| auto type deduction | 02, 06, 13 | 01 Type System |
| bind / placeholders | 10 | 04 Functions & Algorithms |
| const / constexpr / consteval | 02, 04, 06, 11 | 01 Type System |
| copy elision / RVO / NRVO | 06, 11 | 04 Functions / 06 Classes |
| CRTP | 12, 13 | 06 Classes / 07 Templates |
| CTAD (deduction guide) | 13 | 07 Templates |
| decltype / decltype(auto) | 02, 06, 13 | 01 Type System |
| exception (try/catch/noexcept) | 15 | 07 Templates & Meta (misc) |
| `if constexpr` | 05, 13, 14 | 02 Statements / 07 Templates |
| inheritance & virtual functions | 12 | 06 Classes |
| iterator categories | 09, 10 | 03 Containers / 04 Algorithms |
| lambda expression | 10, 13 | 04 Functions & Algorithms |
| move semantics / `std::move` | 04, 11 | 06 Classes |
| name mangling / `extern "C"` | 06 | 04 Functions |
| nullptr / `std::nullptr_t` | 02 | 01 Type System |
| operator overloading | 12 | 06 Classes |
| perfect forwarding | 13 | 07 Templates |
| pointer arithmetic / array decay | 03 | 03 Containers |
| RAII | 08, 11 | 05 Memory / 06 Classes |
| ranges (C++20) | 10 | 04 Algorithms / 08 Toolchain |
| RTTI / `dynamic_cast` / `typeid` | 12 | 06 Classes |
| SFINAE / `enable_if` / `void_t` | 13, 14 | 07 Templates |
| smart pointers (`unique_/shared_/weak_`) | 08 | 05 Memory & I/O |
| spaceship operator `<=>` | 04, 12 | 01 Type System / 06 Classes |
| stream class hierarchy | 07 | 05 Memory & I/O |
| structured binding | 04, 09 | 02 Statements / 03 Containers |
| three-way comparison categories | 04, 12 | 01 Type System |
| `type_traits` library | 14 | 07 Templates & Meta |
| union / `std::variant` | 15 | 07 Templates & Meta |
| value category (lvalue/rvalue/...) | 04 | 01 Type System |
| variadic template / fold expression | 13 | 07 Templates |

---

## 7. Frozen IDs & Contracts

- **Module IDs `00..08`** are immutable. Phase C drawio module map files must be named `drawio/module_<ID>_<short-slug>.drawio` (e.g. `drawio/module_01_type_system.drawio`).
- **Chapter slugs** for cross-link in Phase D follow `chapter/<NN>...md` (existing filenames) — no renames.
- **Terminology table § 2** is the canonical 中/英 mapping. Chapter agents may NOT introduce a different Chinese translation for a listed term without updating this file first.
- **Identifier list § 3** is the audit allowlist. Chapter agents may freely add new identifiers but **must not delete** any current entry without `// dropped:` annotation.
- **mermaid baseline § 4** and **godbolt format § 5** are non-negotiable for the Phase F single-file HTML build.

> End of frozen inventory. Do not edit during Phase C–H without re-running B0-1.
