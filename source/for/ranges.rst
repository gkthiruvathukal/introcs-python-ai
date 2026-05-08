.. index:: range(), loop; range

.. _Ranges:

The ``range()`` Function
========================

.. note::

   *Source:* Adapted from the C# edition (``for/forstatements.rst``).
   The three-part C# ``for`` heading — initialisation, condition, update —
   is replaced in Python by ``range()``.  All the same counting patterns are
   available; the syntax is more concise and harder to get wrong.

Python's ``range()`` produces a sequence of integers on demand.  Paired with
``for``, it covers every counter-based loop that C# handles with
``for (int i = ...; ...; ...)`` headings.

One-Argument Form: ``range(n)``
--------------------------------

.. index:: range(n)

.. code-block:: none

   range(n)   →  0, 1, 2, ..., n-1

This replaces the C# pattern ``for (int i = 0; i < n; i++)``.

.. code-block:: python

   for i in range(4):
       print(i)

Output:

.. code-block:: none

   0
   1
   2
   3

To see the full sequence at once, convert it to a list:

.. code-block:: python

   print(list(range(4)))

Output:

.. code-block:: none

   [0, 1, 2, 3]

Two-Argument Form: ``range(start, stop)``
------------------------------------------

.. index:: range(start, stop)

.. code-block:: none

   range(start, stop)   →  start, start+1, ..., stop-1

This replaces ``for (int i = start; i < stop; i++)``.

.. code-block:: python

   for i in range(1, 6):
       print(i)

Output:

.. code-block:: none

   1
   2
   3
   4
   5

Note that ``stop`` is *exclusive* — the loop runs while ``i < stop``, just
like C#'s condition.

Three-Argument Form: ``range(start, stop, step)``
--------------------------------------------------

.. index:: range(start, stop, step)

.. code-block:: none

   range(start, stop, step)   →  start, start+step, start+2*step, ...

This replaces ``for (int i = start; i < stop; i += step)``.

Counting by fives from 0 to 20:

.. code-block:: python

   print(list(range(0, 25, 5)))

Output:

.. code-block:: none

   [0, 5, 10, 15, 20]

The sequence stops *before* it would equal or exceed ``stop``.

Reverse Iteration
-----------------

.. index:: range; reverse, reversed()

A negative step counts downward:

.. code-block:: python

   for i in range(5, 0, -1):
       print(i)

Output:

.. code-block:: none

   5
   4
   3
   2
   1

``range(n-1, -1, -1)`` visits indices n-1 down to 0, which is the Python
equivalent of C#'s ``for (int i = n-1; i >= 0; i--)``.

An alternative that reads more naturally is ``reversed(range(n))``:

.. code-block:: python

   for i in reversed(range(5)):
       print(i)

Output:

.. code-block:: none

   4
   3
   2
   1
   0

.. index:: range; lazy evaluation, range; memory efficiency

Range Objects Are Lazy
-----------------------

``range()`` does *not* build a list in memory — it computes each integer on
demand.  This makes ``range(1_000_000)`` just as cheap to create as
``range(5)``.  Only use ``list(range(...))`` when you actually need a list.

Summary
-------

.. list-table::
   :header-rows: 1
   :widths: 45 45

   * - C# ``for`` heading
     - Python equivalent
   * - ``for (int i=0; i<n; i++)``
     - ``for i in range(n):``
   * - ``for (int i=a; i<b; i++)``
     - ``for i in range(a, b):``
   * - ``for (int i=a; i<b; i+=k)``
     - ``for i in range(a, b, k):``
   * - ``for (int i=n-1; i>=0; i--)``
     - ``for i in range(n-1, -1, -1):``
