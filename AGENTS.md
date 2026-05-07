# AGENTS.md — Introduction to Computer Science in Python

This file gives AI agents and contributors a complete picture of the project:
what it is, where things stand, and how to work on it effectively.

---

## What this project is

**Introduction to Computer Science in Python: Principles and Practice** is a
Sphinx-based course textbook for Comp 170 (Introduction to Computer Science) at
Loyola University Chicago.  It is authored by the Computer Science Department
Faculty at Loyola University Chicago.

The book teaches introductory CS concepts using Python.  It is a ground-up
Python rewrite of the prior C# edition (`introcs-csharp`, located at
`~/Work/introcs-csharp`).  Chapter structure and pedagogical arc are preserved;
all code and language-specific explanations are Python-native.

The book's broader argument — that programming, data structures, and algorithms
should be taught as foundations for systems and engineering thinking, especially
in the age of AI — is articulated in:

> Chandra N. Sekharan and George K. Thiruvathukal,
> *"Now's the Time: Computer Science Must Evolve to Emphasize Software and
> Systems Engineering with Artificial Intelligence (AI),"*
> IEEE Computer, Education Department, 2026.
> https://arxiv.org/abs/2604.27230

---

## Remote repository

```
git@github.com:LoyolaChicagoBooks/introcs-python-ai.git
```

Branch: `main`

Latest release tag: `v0.1`

---

## Deployed sites

- **GitHub Pages (custom domain):** https://introcs-python.cs.luc.edu
- **CNAME file:** generated at CI time (`build/html/CNAME`) — do not commit it
- **GitHub Releases (PDF + EPUB):** published automatically on tag pushes

---

## Source material

When adapting or adding content, draw from:

1. **`~/Work/introcs-csharp`** — the C# predecessor; primary source for
   chapter structure, example programs, and narrative voice.
2. **`~/Work/SE4ML`** — secondary source for systems/AI framing.
3. **`~/Work/comp-501-book`** — PhD student contributions (COMP 501, Loyola);
   source for: hardware/software, terminal, modules/scope, user input, error
   handling, lists of dicts, dict algorithms, internet data, GUI chapters.
4. **`~/Work/operatingsystems`** — Linux terminal examples drawn from
   `source/introduction.rst`.

Every RST file contributed by PhD students carries a `.. note::` attribution:
`*Source:* Contributed by PhD students in COMP 501 at Loyola University Chicago.`

---

## Content status (as of 2026-05-07)

### Complete chapters (full prose, no stubs)

| Chapter | Directory |
|---------|-----------|
| Context (motivation, CS intro) | `source/context/` |
| **Episodes in Computing History** *(preliminary)* | `source/computing_history/` |
| Hardware and Software | `source/hardware/` |
| The Terminal | `source/terminal/` |
| Data (variables, arithmetic, I/O, types) | `source/data/` |
| Functions | `source/functions/` |
| Modules and Variable Scope | `source/modules/` |
| Basic String Operations | `source/basicstringops/` |
| Decisions | `source/decisions/` |
| User Input | `source/user_input/` |
| While Loops | `source/while/` |
| For Loops | `source/for/` |
| Files & pathlib | `source/files/` |
| Error Handling | `source/error_handling/` |
| Lists | `source/lists/` |
| Tuples | `source/tuples/` |
| Dictionaries | `source/dictionaries/` |
| Lists of Dictionaries | `source/lists_of_dicts/` |
| Dictionary Algorithms | `source/dict_algorithms/` |
| Internet Data | `source/internet_data/` |
| Classes & dataclasses | `source/classes/` |
| Testing (pytest) | `source/testing/` |
| Recursion | `source/recursion/` |
| Data Structures | `source/datastructures/` |
| Graphical User Interfaces (Tkinter) | `source/gui/` |

### Appendix

| File | Status |
|------|--------|
| `lesson_plan.rst` | Complete — 16-week table with chapter links |
| `contributors.rst` | Complete — all authors, faculty, emeritus |
| `acknowledgments.rst` | Stub |
| `cmdline.rst` | Stub |
| `precedence.rst` | Stub |
| `lab-versioncontrol.rst` | Stub |
| `homework-gradecalculation.rst` | Stub |

---

## Repository layout

```
introcs-python/
├── AGENTS.md                   # this file
├── Makefile                    # Sphinx build targets
├── requirements.txt            # sphinx, sphinx-book-theme, etc.
├── .github/workflows/main.yml  # CI: HTML → GitHub Pages; PDF/EPUB → releases
└── source/
    ├── conf.py                 # Sphinx configuration
    ├── index.rst               # Top-level toctree
    ├── _static/logo.png        # Book logo
    ├── context/                # Ch 1 — motivation
    ├── computing_history/      # Ch 2 — episodes in computing history (preliminary)
    ├── hardware/               # Ch 3
    ├── terminal/               # Ch 4
    ├── data/                   # Ch 5
    ├── functions/              # Ch 6
    ├── modules/                # Ch 7
    ├── basicstringops/         # Ch 8
    ├── decisions/              # Ch 9
    ├── user_input/             # Ch 10
    ├── while/                  # Ch 11
    ├── for/                    # Ch 12
    ├── files/                  # Ch 13
    ├── error_handling/         # Ch 14
    ├── lists/                  # Ch 15
    ├── tuples/                 # Ch 16
    ├── dictionaries/           # Ch 17
    ├── lists_of_dicts/         # Ch 18
    ├── dict_algorithms/        # Ch 19
    ├── internet_data/          # Ch 20
    ├── classes/                # Ch 21
    ├── testing/                # Ch 22
    ├── recursion/              # Ch 23
    ├── datastructures/         # Ch 24
    ├── gui/                    # Ch 25
    └── appendix/               # lesson_plan, contributors, stubs
```

Each chapter follows the two-file pattern:
- `chapter/chapter.rst` — container: `#`-underlined title + toctree
- `chapter/overview.rst` (or multiple sub-files) — content: `=`-underlined title

---

## Build instructions

```bash
# Install dependencies (once)
pip install -r requirements.txt

# HTML (fast, for day-to-day work)
make html
open build/html/index.html

# Full clean rebuild (required when adding new toctree entries)
make clean && make html

# Check for Sphinx warnings/errors
make html 2>&1 | grep -E "ERROR|WARNING"

# PDF (requires TeX Live full install with xelatex)
make latex
# then compile PDF:
make -C build/latex
open build/latex/introcs-python.pdf

# EPUB
make epub
```

The PDF uses **xelatex** (not pdflatex) because the book contains Unicode
characters throughout. The `texlive-full` CI image already includes all
required fonts — no `tlmgr install` step is needed.

---

## GitHub Actions CI

`.github/workflows/main.yml`:

- **Every push to `main`**: builds HTML, LaTeX, EPUB; compiles PDF with
  `xu-cheng/texlive-action/full`; deploys HTML to GitHub Pages at
  `https://introcs-python.cs.luc.edu`.
- **Tag push (`v*`)**: publishes `introcs-python.pdf` and `introcs-python.epub`
  as GitHub Release assets via `softprops/action-gh-release`.
- **`workflow_dispatch`**: manual trigger from the Actions tab.

Do **not** add `tlmgr install` steps — the full TeXLive image already contains
everything needed, and network-dependent `tlmgr` calls have failed in CI.

---

## RST writing conventions

### File structure

Every content file must follow this pattern:

```rst
.. index:: keyword, another keyword

.. _Label-Name:

Section Title
=============

.. note::

   *Source:* Adapted from the C# edition (``chapter/file.rst``).
   <what changed for Python>

[prose]

.. code-block:: python

   [example]

Output:

.. code-block:: none

   [output]
```

### Heading levels

| Level | Underline char | Used for |
|-------|---------------|----------|
| 1 | `#` (no overline) | Chapter container title (`chapter.rst`) |
| 2 | `=` | Section title (top of each content `.rst` file) |
| 3 | `-` | Subsection |
| 4 | `^` | Sub-subsection |

### Code blocks

- `.. code-block:: python` — all Python code
- `.. code-block:: none` — output, shell commands, syntax diagrams
- `.. code-block:: bash` — shell/Linux commands
- Always precede output blocks with a plain `Output:` line (not a directive)
- No `.. literalinclude::` — all code is inline

### Review questions

Each numbered review question must contain **exactly one question**.  If a
topic naturally has two parts, use `a.` / `b.` / `c.` sub-items:

```rst
#.  Main question stem.

    a.  Part one.
    b.  Part two.
```

### Voice and tone

- Direct, instructional, patient — follow the C# edition's style
- Explain the *why*, not just the *what*
- Second person ("you", "your program")
- Bold (`**term**`) for key terms when first introduced in characteristics lists
- Prefer prose paragraphs over bullet lists
- Soften absolute statements: prefer "is unlikely to" over "cannot"

---

## Python idioms to prefer

- f-strings over `%` or `.format()`
- `pathlib.Path` over `os.path`
- `with open(...) as f:` for all file I/O
- `for item in iterable:` over index-based loops where natural
- `snake_case` for variables/functions, `PascalCase` for classes
- Raise `ValueError` for invalid arguments (not silent failure)

---

## C# → Python translation reference

| C# | Python |
|----|--------|
| `Console.WriteLine(x)` | `print(x)` |
| `Console.Write(x)` | `print(x, end='')` |
| `Console.ReadLine()` | `input()` |
| `int.Parse(s)` / `double.Parse(s)` | `int(s)` / `float(s)` |
| `{0:F2}` format strings | f-string `{value:.2f}` |
| `//` comments | `#` comments |
| `&&`, `\|\|`, `!` | `and`, `or`, `not` |
| `else if` | `elif` |
| `foreach (var x in seq)` | `for x in seq:` |
| `List<T>` | `list` |
| `Dictionary<K,V>` | `dict` |
| `Stack<T>` | `list` (append/pop) |
| `Queue<T>` | `collections.deque` |
| NUnit `[Test]` / `Assert.AreEqual` | pytest `def test_*` / `assert` |
| `null` | `None` |

---

## Key content notes

### Computing history chapter (`source/computing_history/`)

Preliminary — not intended to be exhaustive. Based primarily on the author's
own published works:
- "Episodes in Computing History — Salon Talk" (Thiruvathukal, 2025)
- "Computer Science and Cultural History: A Dialogue" (Thiruvathukal & Dennis, CESTEMER 2017)
- "AI &| ML" panel talk (Thiruvathukal, LUCRA 2024)
- CiSE Editor-in-Chief mini-history project (2013–2016)

### Terminal chapter (`source/terminal/`)

Extended with Linux command examples drawn from `~/Work/operatingsystems/source/introduction.rst`.
Covers: pwd, ls, cd, mkdir, whoami, cat, touch, cp, mv, rm, echo, less, grep,
find, plus File Permissions (chmod, chown) and Process Management (ps, top, kill).

### Recursion chapter

- `recursionintro.rst`: shows recursive *and* iterative factorial/Fibonacci
  side-by-side; both versions validate input with `ValueError` for negative n;
  includes "No Tail-Call Optimisation" and "Security Implications of Unbounded
  Recursion" subsections.
- `recursionexamples.rst`: ends with a "Generators for Sequences with a Ceiling"
  section showing infinite generators + `itertools.takewhile`.

### Motivation chapter (`source/context/motivation.rst`)

- Includes "Programming in the Age of Artificial Intelligence" section with
  AGI/human-in-the-loop caveat.
- Includes "Software Engineering, Automation, and Prototyping" section.
- References the Sekharan & Thiruvathukal (2026) op-ed.

---

## Authors

**Lead Editor and Co-Author:** George K. Thiruvathukal (thiruvathukal@gmail.com)

**Faculty Co-Authors:** Konstantin Läufer, Leo Irakliotis

**Contributing Co-Authors (COMP 501 PhD students):** Ihab Al Shaikhli,
Arslan Bisharat, Behnaz Eslami, Matt Hyatt, Jason Luce, Manny Sandoval
Madrigal, Mujtaba Nazari, Erik Pautsch, Michael Saban, Rushikesh Shirsat,
Nicholas Synovic

**Other Contributors:** Thomas W. Christopher (IIT, Emeritus),
Andy Harrington (Loyola, Emeritus)

See `source/appendix/contributors.rst` for the full contributors list.
