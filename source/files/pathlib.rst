.. index:: pathlib, Path object, file system

.. _Pathlib:

Working with ``pathlib``
========================

.. note::

   *Source:* Python-specific — no direct equivalent in the C# edition.
   C# uses the ``System.IO.Directory`` and ``System.IO.File`` classes;
   Python's ``pathlib`` module provides an object-oriented interface that
   combines both into a single ``Path`` type.

The ``pathlib`` module, introduced in Python 3.4, represents file system
paths as objects rather than plain strings.  This makes path manipulation
readable and cross-platform.

Creating Path Objects
---------------------

.. index:: Path(); constructor

.. code-block:: python

   from pathlib import Path

   p = Path("data/numbers.txt")   # relative path
   q = Path("/Users/alice/notes") # absolute path
   r = Path.cwd() / "output.txt"  # build from current directory

Path Attributes
---------------

.. index:: Path.name, Path.stem, Path.suffix, Path.parent

A ``Path`` object exposes the components of a path as attributes:

.. code-block:: python

   p = Path("reports/2024/summary.csv")

   print(p.name)    # filename with extension
   print(p.stem)    # filename without extension
   print(p.suffix)  # extension including the dot
   print(p.parent)  # directory containing the file

Output:

.. code-block:: none

   summary.csv
   summary
   .csv
   reports/2024

Checking Existence
------------------

.. index:: Path.exists(), Path.is_file(), Path.is_dir()

.. code-block:: python

   p = Path("data.txt")

   if p.exists():
       print("found")
   if p.is_file():
       print("it is a regular file")
   if p.is_dir():
       print("it is a directory")

Listing Directory Contents
--------------------------

.. index:: Path.iterdir(), Path.glob()

``Path.iterdir()`` yields all entries (files and subdirectories) in a
directory:

.. code-block:: python

   for entry in Path(".").iterdir():
       print(entry.name)

``Path.glob(pattern)`` filters by a wildcard pattern:

.. code-block:: python

   for csv_file in Path("data").glob("*.csv"):
       print(csv_file)

Output (example):

.. code-block:: none

   data/sales.csv
   data/inventory.csv

.. index:: pathlib; convenience methods

Reading and Writing via Path
-----------------------------

.. index:: Path.read_text(), Path.write_text()

For simple cases, ``Path`` objects have ``read_text()`` and
``write_text()`` convenience methods that open, operate, and close the
file automatically:

.. code-block:: python

   content = Path("notes.txt").read_text()
   Path("copy.txt").write_text(content)

For more control — reading line by line, appending, or writing with
formatted output — use ``open()`` as described in :ref:`fileread` and
:ref:`filewrite`.
