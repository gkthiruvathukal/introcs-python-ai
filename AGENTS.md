# AGENTS.md — Introduction to Computer Science in Python

This file gives AI agents and contributors a complete picture of the project:
what it is, how it is built, and how to work on it effectively.

---

## What this project is

**Introduction to Computer Science in Python** is a Sphinx-based course textbook
written for Comp 170 (Introduction to Computer Science) at Loyola University Chicago.
It is authored by the Computer Science Department Faculty at Loyola University Chicago.

The book teaches introductory CS concepts using Python as the implementation language.
It is a ground-up Python rewrite of a prior C# edition of the same course
(`introcs-csharp`, located at `/Volumes/Work/introcs-csharp`).
The chapter structure and pedagogical arc are preserved from that edition,
but all code, toolchain references, and language-specific explanations are Python-native.

### Relationship to the C# edition

The C# book (`introcs-csharp`) is the authoritative reference for:
- The overall narrative voice and writing style — preserve this when writing new content
- The conceptual ordering of topics
- The set of example programs (painting, birthday series, wages, grade, GCD, etc.)

The Python edition deliberately differs from the C# edition in these ways:
- No `foreach` chapter: Python's `for` loop covers both C# `foreach` and `for`
- No `arrays` chapter: Python `lists` cover both C# arrays and `List<T>`
- No `interfaces` chapter: replaced by `dataclasses` section in the classes chapter
- New `tuples` chapter: no C# equivalent
- `fstrings.rst` added to the data chapter (replaces `writeline-substitution`)
- `librarymodule.rst` replaces `libraryclass.rst` (Python uses modules, not static classes)
- `pathlib.rst` added to files chapter (replaces C# `Directory` class content)
- `pytest` replaces NUnit for testing
- `dataclasses` section added to classes chapter
- Appendix: Git replaces Mercurial; `pip`/`venv` replaces Mono tools

---

## Repository layout

```
introcs-python/
├── AGENTS.md               # this file
├── Makefile                # Sphinx build targets
├── requirements.txt        # Python dependencies (sphinx, sphinx-book-theme)
└── source/
    ├── conf.py             # Sphinx configuration
    ├── index.rst           # Top-level toctree
    ├── context/            # Ch 1: Motivation, resources, what is CS
    ├── data/               # Ch 2: Variables, arithmetic, strings, I/O, types
    ├── functions/          # Ch 3: Defining functions, scope, modules
    ├── basicstringops/     # Ch 4: String indexing, methods
    ├── decisions/          # Ch 5: if/elif/else, boolean expressions
    ├── while/              # Ch 6: While loops, interactive input, GCD
    ├── for/                # Ch 7: For loops, range(), list comprehensions
    ├── files/              # Ch 8: Reading/writing files, pathlib
    ├── lists/              # Ch 9: Lists, searching, sorting
    ├── tuples/             # Ch 10: Tuples, unpacking
    ├── dictionaries/       # Ch 11: Dicts, word frequency, efficiency
    ├── classes/            # Ch 12: OOP, dataclasses, Rational class
    ├── testing/            # Ch 13: pytest
    ├── recursion/          # Ch 14: Recursive algorithms
    ├── datastructures/     # Ch 15: Stacks, queues, linked lists
    └── appendix/           # Contributors, acknowledgments, CLI, precedence
```

Each chapter directory contains:
- A chapter toctree file (`<chapter>/<chapter>.rst`) with `####` title underline
- Section files with `===` title underlines
- Every section currently has a `.. todo::` block describing content to write

---

## Build instructions

### Prerequisites

```
pip install -r requirements.txt
```

The two required packages are `sphinx` and `sphinx-book-theme`.

### Building HTML

```
make html
```

Output is written to `build/html/`. Open `build/html/index.html` in a browser.

### Other targets

```
make epub        # EPUB output
make latexpdf    # PDF via LaTeX (requires a LaTeX installation)
make text        # Plain text
make linkcheck   # Check all external hyperlinks
make clean       # Remove the build/ directory
```

### Checking todos

```
grep -r ".. todo::" source/ | wc -l
```

All section stubs currently contain `todo` directives. Sphinx renders these
when `todo_include_todos = True` is set in `conf.py` (it is).

---

## Writing conventions

### RST style

- Chapter toctree files use `#` with overline (`####` above and below the title)
- Section files use `=` underline only (`===` below the title)
- Subsections use `-` underline
- Default code block language is `python` (set globally in `conf.py` via `rst_prolog`)
- Use `.. code-block:: python` for inline examples; `.. literalinclude::` for
  external example files once the examples submodule exists
- Use `.. code-block:: none` for program output and shell commands
- Cross-references: `:ref:\`label\`` for internal links; `:repsrc:\`path\`` for
  links to the examples repository

### Voice and tone

Follow the C# edition's style: direct, instructional, patient. Explain the *why*
not just the *what*. Walk through example programs line by line where appropriate.
Use the second person ("you", "your program").

### Python idioms to prefer

- f-strings over `%` formatting or `.format()`
- `pathlib.Path` over `os.path`
- `with open(...) as f:` for all file I/O
- `for item in iterable:` over index-based loops where natural
- Type hints are optional and should be introduced late (classes chapter or later)
- `snake_case` for variables and functions, `PascalCase` for classes

### What to note when adapting from the C# edition

- Drop all `using System;`, namespace blocks, `static void Main()`, and `class` wrappers
- `Console.WriteLine(...)` → `print(...)`
- `Console.Write(...)` → `print(..., end='')`
- `Console.ReadLine()` → `input()`
- `double.Parse(s)` / `int.Parse(s)` → `float(s)` / `int(s)`
- `//` comments → `#` comments
- `{0:F2}` format strings → f-string `{value:.2f}`
- Semicolons and braces → indentation
- `&&`, `||`, `!` → `and`, `or`, `not`
- `else if` → `elif`

---

## Examples submodule

The examples repository (`introcs-python-examples`) does not exist yet.
When it is created, it will be added as a git submodule at `examples/`.
The `extlinks` entry in `conf.py` already points to:

```
https://github.com/LoyolaChicagoBooks/introcs-python-examples/blob/master/%s
```

Until then, use inline `.. code-block:: python` for all code.
When the submodule is ready, convert key examples to `.. literalinclude::` directives.

---

## Content status

All chapters are scaffolded with section stubs. Every stub contains a `.. todo::`
block. No section has final prose yet. Work proceeds chapter by chapter, starting
from Chapter 1 (Context) and moving forward.

To see all outstanding todos:

```
grep -rl ".. todo::" source/
```

---

## Authors and contributors

**Author:** The Computer Science Department Faculty at Loyola University Chicago

See `source/appendix/contributors.rst` for the full contributors list
(currently a placeholder pending confirmation of contributors).

This book has its roots in *Introduction to Computer Science in C#* by
Andrew N. Harrington and George K. Thiruvathukal, which is the direct
predecessor to this work.
