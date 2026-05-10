.. index:: labs; nested loops

.. _lab-nested-loops:

Lab: Nested Loops
=================


Goals for this lab:

- Practice ``for`` loops with ``range()``.
- Use nested loops to produce two-dimensional output.
- Build strings by accumulation.

.. index:: print_reps

1. ``print_reps``
-----------------

Write a function ``print_reps(s, count)`` that prints ``s`` repeated
``count`` times on a single line.

Example calls and expected output::

    print_reps("Ok", 4)
    print_reps("*", 5)

.. code-block:: none

   OkOkOkOk
   *****

Use a ``for`` loop — do *not* use Python's ``s * count`` shortcut here.

.. index:: string_of_reps

2. ``string_of_reps``
----------------------

Write a function ``string_of_reps(s, count)`` that *returns* a string
consisting of ``s`` repeated ``count`` times (without printing).

.. code-block:: python

   >>> string_of_reps("ab", 3)
   'ababab'

Build the result by accumulating into an initially empty string using a
``for`` loop.  After you have it working, verify that ``s * count`` gives
the same answer — this is Python's built-in way to repeat a string.

.. index:: factorial

3. ``factorial``
----------------

Write a function ``factorial(n)`` that returns n! = 1 × 2 × … × n
iteratively.  Use ``range(1, n + 1)`` and a running product:

.. code-block:: none

   n = 0 → 1
   n = 1 → 1
   n = 5 → 120
   n = 6 → 720

Think through the starting value of your accumulator before coding.

After it passes basic tests, find the largest value of ``n`` for which
Python gives a correct answer.  (Hint: Python integers have arbitrary
precision, so you may be surprised.)

.. index:: print_rectangle

4. ``print_rectangle``
-----------------------

Write a function ``print_rectangle(n_cols, n_rows, fill, border)`` that
prints a rectangle ``n_cols`` wide and ``n_rows`` tall, using ``border``
characters on the perimeter and ``fill`` characters inside.

Example call::

    print_rectangle(5, 4, '.', '#')

Expected output:

.. code-block:: none

   #######
   #.....#
   #.....#
   #######

Notes:

- The outer dimensions include the border, so the interior is
  ``(n_cols) × (n_rows - 2)`` cells.
- Rows consist of: top border row, ``n_rows - 2`` interior rows, bottom
  border row.
- An interior row is one border character, ``n_cols`` fill characters,
  one border character.

Build the row strings with ``string_of_reps`` or string multiplication.

.. index:: multiplication table

5. Multiplication Table
-----------------------

Write a function ``mult_table(n)`` that prints an ``n × n`` multiplication
table with row and column headers.  Example call::

    mult_table(5)

Expected output:

.. code-block:: none

    * |  1  2  3  4  5
   -------------------
    1 |  1  2  3  4  5
    2 |  2  4  6  8 10
    3 |  3  6  9 12 15
    4 |  4  8 12 16 20
    5 |  5 10 15 20 25

Suggestions:

- Compute the column width from ``len(str(n * n))`` so the table scales.
- Print the header row with a ``for`` loop, then a separator line, then
  the body rows using nested loops.
- Use an f-string with a computed field width for alignment.

This exercise is similar to the modular multiplication table in
:ref:`For-Examples` but without the modulus operation.
