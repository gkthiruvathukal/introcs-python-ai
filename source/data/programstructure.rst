.. index:: program structure, if __name__

Python Program Structure
========================

A Python program file — a ``.py`` file — is much simpler in structure than
the equivalent in C# or Java.

No Required Wrapper
-------------------

In C#, every statement must live inside a class and a ``Main`` method:

.. code-block:: none

   // C# — not Python
   using System;
   class Hello {
       static void Main() {
           Console.WriteLine("Hello, world!");
       }
   }

In Python, you simply write statements at the top level of the file:

.. code-block:: python

   print("Hello, world!")

There is no required class, no ``Main``, no ``using`` directive.

.. index:: if __name__ == '__main__'

The ``if __name__ == '__main__':`` Pattern
------------------------------------------

When Python runs a file directly (``python3 filename.py``), it sets a special
variable called ``__name__`` to the string ``'__main__'``.  When the same
file is *imported* by another file as a module, ``__name__`` is set to the
module's name instead.

This lets you write files that work both as standalone programs *and* as
reusable modules:

.. code-block:: python

   def greet(name):
       print(f"Hello, {name}!")

   if __name__ == '__main__':
       greet("world")

- If you run this file directly, ``__name__ == '__main__'`` is true and
  ``greet("world")`` is called.
- If another file does ``import greet_module``, the ``if`` block is skipped
  and only the ``greet`` function is made available.

This pattern is a best practice once you start writing functions you want to
reuse.  The earlier chapters do not require it, but you should adopt it as
soon as your programs grow beyond a few lines.

.. index:: indentation

Indentation
-----------

Python uses *indentation* to show the structure of a program — which
statements belong to a function, loop, or condition.  Unlike C# which uses
braces ``{}``, Python requires consistent indentation.

.. code-block:: python

   def double(x):
       return x * 2      # indented — part of the function

   print(double(5))      # not indented — not part of the function

The standard is 4 spaces per level.  Never mix tabs and spaces.

A missing or wrong indentation level is a syntax error:

.. code-block:: python

   def double(x):
   return x * 2   # IndentationError: expected an indented block

.. index:: comments

Comments
--------

A comment starts with ``#`` and runs to the end of the line.  Python ignores
comments completely:

.. code-block:: python

   HEIGHT = 8          # ceiling height in feet
   area = length * width   # calculate floor area

Use comments to explain *why*, not *what* — the code itself should make
*what* it does clear.

Statement Endings
-----------------

Python statements do not end with a semicolon.  The end of a line ends the
statement.  If you need to continue a statement across lines, enclose the
expression in parentheses:

.. code-block:: python

   result = (first_number
             + second_number
             + third_number)

You can also use a backslash ``\`` to continue a line, but parentheses are
preferred.
