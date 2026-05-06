.. index:: path string, file; path, absolute path, relative path

.. _Path-Strings:

Path Strings
============

.. note::

   *Source:* Adapted from the C# edition (``files/paths.rst``).
   Python uses plain strings or ``pathlib.Path`` objects instead of C#'s
   ``System.IO.Path`` class.  Cross-platform separator differences are
   the same, but Python's ``pathlib`` handles them transparently.

When a program runs there is always a *current working directory*.  Files in
that directory can be opened by their plain name, like ``"data.txt"``.  Files
elsewhere require a *path string* — a chain of directory names leading to
the target file.

Absolute and Relative Paths
----------------------------

.. index:: absolute path, relative path, current working directory

An *absolute path* starts from the root of the file system:

.. code-block:: none

   /Users/alice/Documents/data.txt       (macOS / Linux)
   C:\Users\alice\Documents\data.txt     (Windows)

A *relative path* starts from the current working directory and does not
begin with a separator:

.. code-block:: none

   data.txt                  (file in the current directory)
   reports/summary.txt       (subdirectory of the current directory)
   ../other_project/run.py   (one level up, then into another folder)

``..`` means "the parent directory"; ``.`` means "the current directory."

Cross-Platform Path Separators
--------------------------------

.. index:: path separator, pathlib.Path; / operator

Windows uses ``\`` and macOS/Linux use ``/``.  Hard-coding either character
makes scripts fragile.  Python's ``pathlib`` module handles this automatically
using the ``/`` operator to join path components:

.. code-block:: python

   from pathlib import Path

   p = Path("reports") / "2024" / "summary.txt"
   print(p)

Output (macOS/Linux):

.. code-block:: none

   reports/2024/summary.txt

The ``/`` operator always uses the correct separator for the current OS.

Finding the Current Directory
------------------------------

.. index:: Path.cwd(), Path.home()

.. code-block:: python

   from pathlib import Path

   print(Path.cwd())    # current working directory
   print(Path.home())   # user's home directory

Output (example):

.. code-block:: none

   /Users/alice/projects/myapp
   /Users/alice

Full details on working with ``Path`` objects — reading attributes,
checking existence, and listing directories — are in :ref:`Pathlib`.
