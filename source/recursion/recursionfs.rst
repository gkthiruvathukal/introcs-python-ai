.. index:: filesystem; recursive traversal, observer pattern; filesystem walker,
           depth-first search; filesystem, breadth-first search; filesystem,
           DFS; filesystem, BFS; filesystem
   ACM-IEEE CS2013; OS8 File Systems
   ACM-IEEE CS2023; OS8 File Systems
   ACM-IEEE CS2013; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2023; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2013; AL2 Algorithmic Strategies
   ACM-IEEE CS2023; AL2 Algorithmic Strategies

.. _Recursion-Filesystem:

Recursive Filesystem Traversal
================================

.. note::
   *Source:* Adapted from `recursion-book-python-filesystems
   <https://github.com/gkthiruvathukal/recursion-book-python-filesystems>`_
   by George K. Thiruvathukal.

File systems are trees: each directory may contain files and other
directories.  Recursive algorithms map naturally onto this structure.
This section presents a reusable *event-driven walker* that separates
traversal logic from what you do at each node.

.. index:: observer pattern; filesystem, SAX parser; analogy, event-driven programming

The Observer Pattern
---------------------

.. index:: FileSystemEventWalker

The walker fires *events* — ``enter_dir``, ``visit_file``, ``leave_dir``,
``error`` — and passes them to a *handler* object you provide.  This is
the same idea as a SAX XML parser: the traversal engine and the
application logic are completely separate.  The base class defines the
interface:

.. literalinclude:: ../../examples/introcs-python/recursion/os_walker.py
   :language: python
   :start-after: # start: handler_base
   :end-before: # end: handler_base

Every method defaults to doing nothing, so a handler only overrides the
events it cares about.  Returning ``False`` from ``enter_dir`` prunes
that subtree — the walker skips it without raising an error.

DFS: Depth-First Traversal
----------------------------

.. index:: depth-first search; recursive implementation

The recursive walker visits a directory fully before moving to the next
sibling:

.. literalinclude:: ../../examples/introcs-python/recursion/os_walker.py
   :language: python
   :start-after: # start: walk_dfs
   :end-before: # end: walk_dfs

``walk_dfs`` fires ``enter_dir`` when it arrives at a directory, then
recurses into each subdirectory (skipping symlinks to prevent cycles),
fires ``visit_file`` for each file, and fires ``leave_dir`` before
returning.  All filesystem exceptions are caught and routed to
``handler.error`` so a single unreadable directory does not abort the
entire walk.

A Concrete Handler
^^^^^^^^^^^^^^^^^^^

.. index:: PrintHandler; filesystem

This handler prints every entry indented by its depth in the tree:

.. literalinclude:: ../../examples/introcs-python/recursion/os_walker.py
   :language: python
   :start-after: # start: print_handler
   :end-before: # end: print_handler

Calling it on a small project directory:

.. code-block:: python

   walk_dfs("project", PrintHandler())

Output:

.. code-block:: none

   [project/]
     README.md
     [src/]
       main.py
       utils.py
     [tests/]
       test_main.py

BFS: Breadth-First Traversal
------------------------------

.. index:: breadth-first search; iterative implementation, deque; BFS

Depth-first recursion finishes one branch before backtracking.
Breadth-first traversal visits every entry at depth 1 before anything
at depth 2.  Because BFS uses a queue rather than the call stack it is
naturally iterative:

.. literalinclude:: ../../examples/introcs-python/recursion/os_walker.py
   :language: python
   :start-after: # start: walk_bfs
   :end-before: # end: walk_bfs

Instead of recursive calls, ``walk_bfs`` appends child directories to a
``deque`` and processes them in FIFO order.  The same ``PrintHandler``
works with either traversal — the handler interface does not change.

Choosing DFS or BFS
--------------------

.. index:: DFS vs BFS

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * -
     - DFS (recursive)
     - BFS (iterative queue)
   * - Order
     - Finishes a full subtree before moving to the next sibling
     - All entries at depth N before any entry at depth N+1
   * - Stack
     - Call stack — depth limited by Python's recursion limit
     - Explicit ``deque`` — bounded only by available memory
   * - Use when
     - You need ``enter``/``leave`` pairing (size rollups, XML-style output)
     - You want level-order output or the tree is thousands of levels deep

For everyday filesystem tools — pretty-printing, searching, size
accounting — DFS is simpler and the recursion depth is well within
Python's default limit.  BFS is the better choice when trees are
pathologically deep or when level-order output is required.
