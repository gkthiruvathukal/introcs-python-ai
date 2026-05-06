# AGENTS.md — Introduction to Computer Science in Python

This file gives AI agents and contributors a complete picture of the project:
what it is, where things stand, and how to work on it effectively.

---

## What this project is

**Introduction to Computer Science in Python: Software Engineering, Systems,
and Foundational Thinking** is a Sphinx-based course textbook for Comp 170
(Introduction to Computer Science) at Loyola University Chicago.  It is
authored by the Computer Science Department Faculty at Loyola University Chicago.

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
git@github.com:gkthiruvathukal/introcs-python-ai.git
```

Branch: `main`

---

## Source material

When adapting or adding content, always draw from:

1. **`~/Work/introcs-csharp`** — the C# predecessor; the primary source for
   chapter structure, example programs, and narrative voice.
2. **`~/Work/SE4ML`** — secondary source for systems/AI framing.

Every RST file must have a `.. note::` attribution block at the top naming
the specific C# source file(s) ideas come from, or stating
"Python-specific — no equivalent in the C# edition."

---

## Content status (as of 2026-05-06)

### Complete chapters (full prose, no stubs)

| Chapter | Directory |
|---------|-----------|
| Context (motivation, CS intro) | `source/context/` |
| Data (variables, arithmetic, I/O, types) | `source/data/` |
| Functions | `source/functions/` |
| Basic String Operations | `source/basicstringops/` |
| Decisions | `source/decisions/` |
| While Loops | `source/while/` |
| For Loops | `source/for/` |
| Files & pathlib | `source/files/` |
| Lists | `source/lists/` |
| Tuples | `source/tuples/` |
| Dictionaries | `source/dictionaries/` |
| Classes & dataclasses | `source/classes/` |
| Testing (pytest) | `source/testing/` |
| Recursion | `source/recursion/` |
| Data Structures | `source/datastructures/` |

### Remaining stubs

`source/appendix/` — the following files are stubs:

- `cmdline.rst`
- `precedence.rst`
- `lab-versioncontrol.rst`
- `homework-gradecalculation.rst`
- `acknowledgments.rst`
- `contributors.rst`

---

## Repository layout

```
introcs-python/
├── AGENTS.md                   # this file
├── Makefile                    # Sphinx build targets
├── requirements.txt            # sphinx, sphinx-book-theme
├── .github/workflows/main.yml  # CI: HTML → GitHub Pages; PDF/EPUB → releases
└── source/
    ├── conf.py                 # Sphinx configuration
    ├── index.rst               # Top-level toctree
    ├── context/                # Ch 1
    ├── data/                   # Ch 2
    ├── functions/              # Ch 3
    ├── basicstringops/         # Ch 4
    ├── decisions/              # Ch 5
    ├── while/                  # Ch 6
    ├── for/                    # Ch 7
    ├── files/                  # Ch 8
    ├── lists/                  # Ch 9
    ├── tuples/                 # Ch 10
    ├── dictionaries/           # Ch 11
    ├── classes/                # Ch 12
    ├── testing/                # Ch 13
    ├── recursion/              # Ch 14
    ├── datastructures/         # Ch 15
    └── appendix/               # Stubs remaining
```

---

## Build instructions

```bash
# Install dependencies (once)
pip install -r requirements.txt

# HTML (fast, for day-to-day work)
make html
open build/html/index.html

# Check for Sphinx warnings/errors
make html 2>&1 | grep -E "ERROR|WARNING"

# PDF (requires TeX Live with xelatex and gnu-freefont)
make latexpdf
open build/latex/introcs-python.pdf

# EPUB
make epub
```

The PDF uses **xelatex** (not pdflatex) because the book contains Unicode
characters (—, →, ≈, π, etc.) throughout.  Fonts are referenced by filename
(`FreeSerif.otf`) so fontspec uses TeX Live's kpathsea path search rather than
fontconfig — no font installation step needed beyond a standard TeX Live full
install.

---

## GitHub Actions CI

`.github/workflows/main.yml`:

- **Every push to `main`**: builds HTML, LaTeX, EPUB; compiles PDF with TeXLive;
  deploys HTML to GitHub Pages.
- **Tag push (`v*`)**: publishes `introcs-python.pdf` and `introcs-python.epub`
  as GitHub Release assets.
- **`workflow_dispatch`**: manual trigger from the Actions tab.

GitHub Pages URL: `https://gkthiruvathukal.github.io/introcs-python-ai/`

No CNAME configured yet (no custom domain).

---

## RST writing conventions

### File structure

Every section file must follow this pattern:

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
| 1 | `=` | Section title (top of each `.rst` file) |
| 2 | `-` | Subsection |
| 3 | `^` | Sub-subsection |

Chapter toctree files use `#` with overline for the chapter title.

### Code blocks

- `.. code-block:: python` — all Python code
- `.. code-block:: none` — output, shell commands, syntax diagrams
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

### Recursion chapter

- `recursionintro.rst`: shows recursive *and* iterative factorial/Fibonacci
  side-by-side; both versions validate input with `ValueError` for negative n;
  includes "No Tail-Call Optimisation" and "Security Implications of Unbounded
  Recursion" subsections.
- `recursionexamples.rst`: ends with a "Generators for Sequences with a Ceiling"
  section showing infinite generators + `itertools.takewhile` for both
  factorial and Fibonacci.

### Motivation chapter (`source/context/motivation.rst`)

- Includes a full "Programming in the Age of Artificial Intelligence" section
  tracing the historical disruption arc from calculators through generative AI,
  with the reading-before-writing analogy and an AGI/human-in-the-loop caveat.
- Includes a separate "Software Engineering, Automation, and Prototyping"
  section covering CASE tools as the 40-year precursor to AI code generation,
  and the requirements-before-code argument.
- References the Sekharan & Thiruvathukal (2026) op-ed at the top of the AI
  section.

---

## Authors

**Primary author:** George K. Thiruvathukal (thiruvathukal@gmail.com)

**Co-author of foundational op-ed:** Chandra N. Sekharan

This book has its roots in *Introduction to Computer Science in C#* by
Andrew N. Harrington and George K. Thiruvathukal.

See `source/appendix/contributors.rst` for the full contributors list.
