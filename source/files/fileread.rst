.. index:: file; reading, open(), with statement, for; file lines

.. _fileread:

Reading Files
=============

.. note::

   *Source:* Adapted from the C# edition (``files/fileread.rst``).
   Python's ``with open(...) as f:`` replaces C#'s ``StreamReader``.
   The ``for line in f:`` loop replaces the ``while (!reader.EndOfStream)``
   pattern.  ``f.read()`` corresponds to C#'s ``ReadToEnd()``.

The ``open()`` function connects a Python program to a file on disk.
The ``with`` statement ensures the file is automatically closed when the
block exits — even if an error occurs.

Opening and Reading Line by Line
---------------------------------

.. index:: with open(); reading, for line in f:

The most common pattern reads a file one line at a time:

.. code-block:: python

   with open("sample.txt") as f:
       for line in f:
           print(line, end="")

Each string yielded by ``for line in f:`` includes the trailing newline
character, so we pass ``end=""`` to ``print`` to avoid a double newline.
To remove the newline explicitly:

.. code-block:: python

   with open("sample.txt") as f:
       for line in f:
           line = line.rstrip()
           print(line)

``rstrip()`` strips trailing whitespace (including ``\n`` and ``\r\n``).

.. index:: Path; open()

You can pass a ``pathlib.Path`` object anywhere a filename string is
expected:

.. code-block:: python

   from pathlib import Path

   with open(Path("data") / "numbers.txt") as f:
       for line in f:
           print(line.rstrip())

Reading the Entire File at Once
--------------------------------

.. index:: f.read(), f.readlines()

Two methods read everything in one call:

- ``f.read()`` returns the whole file as a single string (with embedded
  newlines).
- ``f.readlines()`` returns a list of line strings, each ending with
  ``\n``.

.. code-block:: python

   with open("sample.txt") as f:
       contents = f.read()
   print(contents)

.. code-block:: python

   with open("sample.txt") as f:
       lines = f.readlines()
   print(len(lines), "lines")

Use ``f.read()`` when you need the whole text at once (e.g., to pass to
another function).  Use the ``for line in f:`` loop when the file may be
large, since it reads one line at a time without loading everything into
memory.

Example: Summing a File of Numbers
------------------------------------

.. index:: example; sum file

Suppose ``numbers.txt`` contains one integer per line:

.. code-block:: none

   4
   7
   -2
   5

.. code-block:: python

   def sum_file(filename: str) -> int:
       total = 0
       with open(filename) as f:
           for line in f:
               total += int(line.strip())
       return total

   print(sum_file("numbers.txt"))

Output:

.. code-block:: none

   14

Checking Whether a File Exists
--------------------------------

.. index:: Path.exists()

Before opening a file that might not exist, check with ``Path.exists()``:

.. code-block:: python

   from pathlib import Path

   filename = input("Enter file name: ")
   if not Path(filename).exists():
       print("File not found.")
   else:
       with open(filename) as f:
           for line in f:
               print(line.rstrip())

This prevents a ``FileNotFoundError`` and lets you give a clear message
to the user.
