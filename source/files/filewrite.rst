.. index:: file; writing, open(); write mode, open(); append mode

.. _filewrite:

Writing Files
=============

.. note::

   *Source:* Adapted from the C# edition (``files/filewrite.rst``).
   Python's ``open(path, "w")`` replaces C#'s ``StreamWriter``.
   The ``with`` statement handles closing automatically, eliminating
   the common C# bug of forgetting to call ``Close()``.

To write a file, pass ``"w"`` (write) or ``"a"`` (append) as the second
argument to ``open()``.

Write Mode
----------

.. index:: open(); "w", f.write()

Opening a file in write mode creates it if it does not exist, or
**silently overwrites it** if it does:

.. code-block:: python

   with open("sample.txt", "w") as f:
       f.write("Hello, file!\n")
       f.write("Second line.\n")

After the ``with`` block exits, Python flushes and closes the file.
There is no need to call ``close()`` explicitly — this is the main
advantage over forgetting it in C#.

You can also use ``print()`` with the ``file=`` keyword argument, which
automatically adds a newline:

.. code-block:: python

   with open("sample.txt", "w") as f:
       print("Hello, file!", file=f)
       print("Second line.", file=f)

Both approaches produce identical output.

Append Mode
-----------

.. index:: open(); "a"

Opening with ``"a"`` leaves existing content intact and adds new lines
at the end:

.. code-block:: python

   with open("log.txt", "a") as f:
       print("New entry added.", file=f)

Example: Copy a File to Upper Case
------------------------------------

.. index:: example; copy upper

This example reads an input file line by line and writes each line in
upper case to a new output file — a Python translation of the C#
``copy_upper`` example:

.. code-block:: python

   def copy_upper(src, dst):
       with open(src) as reader:
           with open(dst, "w") as writer:
               for line in reader:
                   writer.write(line.upper())

   copy_upper("text.txt", "upper_text.txt")

Nested ``with`` statements are valid, though Python also allows combining
them on one line:

.. code-block:: python

   with open(src) as reader, open(dst, "w") as writer:
       for line in reader:
           writer.write(line.upper())

Writing Formatted Data
-----------------------

.. index:: f-string; file output

Use f-strings inside ``f.write()`` or ``print(..., file=f)`` to produce
formatted output:

.. code-block:: python

   import math

   with open("roots.txt", "w") as f:
       print(f"{'n':>4}  {'sqrt(n)':>10}", file=f)
       for n in range(1, 11):
           print(f"{n:4d}  {math.sqrt(n):10.4f}", file=f)

This writes a neatly aligned table to the file, using the same f-string
formatting as on-screen output.
