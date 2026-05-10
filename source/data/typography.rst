.. index:: syntax template

Reading Python Syntax
=====================

Throughout this book, we describe Python syntax using *templates* — patterns
showing the structure of a statement with the variable parts in italics or
indicated by placeholder names.

For example, the template for an assignment statement is::

   variable = expression

This means: write any valid variable name, then ``=``, then any expression.
The actual code might be::

   area = length * width

.. index:: indentation; as syntax, block; indentation

Indentation is Syntax
---------------------

The most important thing to understand about reading Python syntax is that
*indentation matters*.  In Python, a block is indicated by indentation —
all statements in the same block are indented by the same amount.

.. code-block:: python

   if x > 0:
       print("positive")

Key points:

- The condition is followed by a colon ``:``.
- No parentheses are required around the condition (though they are allowed).
- The body is indented — the standard is **4 spaces**.
- There are no braces.

Colons Introduce Blocks
-----------------------

Whenever you see a ``:``, a *block* follows.  The block is indented relative
to the line with the colon:

.. code-block:: python

   def greet(name):        # colon after function header
       print(f"Hello, {name}!")   # indented body

   for i in range(5):      # colon after for header
       print(i)            # indented body

   if x > 0:               # colon after if condition
       print("positive")   # indented body

Reading Shell Output
--------------------

When we show an interactive shell session, we use ``>>>`` for the prompt and
``...`` for continuation lines.  Output appears on lines with no prompt:

.. code-block:: none

   >>> x = 10
   >>> if x > 5:
   ...     print("big")
   ...
   big

Lines beginning with ``$`` show terminal commands run outside Python:

.. code-block:: none

   $ python3 painting.py
   Calculation of Room Paint Requirements
   Enter room length:

.. index:: traceback, error message; reading, ValueError

Reading Error Messages
-----------------------

When your program has an error, Python shows a *traceback* pointing to where
the problem occurred:

.. code-block:: none

   Traceback (most recent call last):
     File "painting.py", line 3, in <module>
       length = float(input("Enter room length: "))
   ValueError: could not convert string to float: 'abc'

Read from the bottom up: the last line tells you *what* went wrong; the lines
above show *where* in the code it happened.
