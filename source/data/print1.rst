.. index::
   single: print

.. _write-to-screen:

Writing to the Screen
=====================

.. note::

   *Source:* Drawn from the SE4ML Python chapter (``chapter_python.rst``,
   lines 753–780) and adapted from the C# edition (``data/print1.rst``).
   The ``sep=`` and ``end=`` keyword arguments are Python-specific additions.

The primary way to produce output in Python is the built-in ``print``
function.

Basic Use
---------

Pass ``print`` a string and it writes that string to the screen, followed by
a newline:

.. code-block:: none

   >>> print("Hello, world!")
   Hello, world!

You can print the value of any expression:

.. code-block:: none

   >>> print(2 + 3)
   5
   >>> total = 42
   >>> print(total)
   42

Multiple Arguments
------------------

``print`` can take multiple arguments, separated by commas.  It writes them
separated by spaces:

.. code-block:: none

   >>> print("The answer is", 42)
   The answer is 42
   >>> print(1, 2, 3)
   1 2 3

You can change the separator with the ``sep`` keyword argument:

.. code-block:: none

   >>> print(1, 2, 3, sep=", ")
   1, 2, 3
   >>> print("cat", "dog", "bird", sep=" | ")
   cat | dog | bird

Controlling the End Character
-------------------------------

By default, ``print`` adds a newline after the last value.  You can change
this with the ``end`` keyword argument.  To suppress the newline entirely, use
``end=""``::

   print("Enter your name: ", end="")

This is useful when you want user input to appear on the same line as the
prompt.  (The ``input()`` function handles this automatically, as we will see
in :ref:`io`, but ``print`` with ``end=""`` is needed in other situations.)

To print several items on the same line in separate ``print`` calls:

.. code-block:: none

   >>> print("one", end=" ")
   >>> print("two", end=" ")
   >>> print("three")
   one two three

Printing Nothing
----------------

A ``print()`` with no arguments writes a blank line:

.. code-block:: none

   >>> print("Before")
   >>> print()
   >>> print("After")
   Before

   After

This is useful for adding vertical space in output.

Printing to a File
------------------

``print`` can write to a file instead of the screen using the ``file``
keyword argument:

.. code-block:: python

   with open("output.txt", "w") as f:
       print("Hello, file!", file=f)

We will cover file I/O in the Files chapter.
