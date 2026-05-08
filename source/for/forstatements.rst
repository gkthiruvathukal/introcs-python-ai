.. index:: for statement, loop; for, foreach

.. _For-Statements:

For Loop Syntax
===============

.. note::

   *Source:* Adapted from the C# edition (``foreach/foreachintro.rst`` and
   ``for/forstatements.rst``).  Python's ``for`` loop is a *foreach* — it
   unifies C#'s separate ``foreach`` and ``for`` constructs into one statement.
   No type declaration is needed for the loop variable.  The ``break`` and
   ``continue`` statements work the same way as in C#.

We have seen how ``while`` loops repeat as long as a condition holds.  A very
common pattern is iterating over every item in a sequence — every character in
a string, every number in a range, every element in a list.  Python's ``for``
loop is designed exactly for this.

If you heard "For each student in the class, record a grade," you would
naturally process one student at a time, in order, until the list is
exhausted.  Python's syntax captures that idea directly:

.. code-block:: none

   for item in iterable:
       statement(s)

On each pass through the loop, ``item`` is bound to the next value from
``iterable``.  When the iterable is exhausted the loop ends.

Iterating Over a String
-----------------------

A string is a sequence of characters, so we can loop over it one character
at a time:

.. code-block:: python

   def one_char_per_line(s: str) -> None:
       for ch in s:
           print(ch)

.. code-block:: python

   one_char_per_line("hi!")

Output:

.. code-block:: none

   h
   i
   !

Compare this with the equivalent ``while`` loop that requires an explicit
index:

.. code-block:: python

   i = 0
   while i < len(s):
       print(s[i])
       i += 1

The ``for`` version keeps the emphasis on the *characters*, not the secondary
bookkeeping.  There is no index to initialise, no ``i += 1`` to remember, and
no risk of an infinite loop.

.. index:: for loop; list iteration

Iterating Over a List
---------------------

The same syntax works for any sequence, including lists:

.. code-block:: python

   scores = [88, 73, 95, 61]
   total = 0
   for score in scores:
       total += score
   print("Total:", total)

Output:

.. code-block:: none

   Total: 317

Iterating Over a Range
----------------------

.. index:: range; with for loop

To repeat something a fixed number of times, or to produce a sequence of
integers, combine ``for`` with ``range()``:

.. code-block:: python

   for i in range(5):
       print(i)

Output:

.. code-block:: none

   0
   1
   2
   3
   4

``range(5)`` generates the integers 0, 1, 2, 3, 4.  The full details of
``range()`` are covered in :ref:`Ranges`.

When to Use ``for`` vs. ``while``
----------------------------------

.. index:: for vs while

Use a ``for`` loop when:

- You are iterating over a known sequence (string, list, range).
- The number of iterations is determined up front.

Use a ``while`` loop when:

- The number of iterations depends on something that changes during the loop
  (user input, a computed condition).
- You need the ``while True`` / ``break`` sentinel pattern.

.. index:: break; in for loop, continue; in for loop

Break and Continue
------------------

``break`` exits the innermost loop immediately; ``continue`` skips the rest
of the current iteration and moves to the next.  Both work inside ``for``
loops just as they do inside ``while`` loops.

.. code-block:: python

   def find_first_vowel(s: str) -> str | None:
       for ch in s.lower():
           if ch in "aeiou":
               return ch
       return None

.. code-block:: python

   print(find_first_vowel("Python"))

Output:

.. code-block:: none

   o

Here ``return`` exits the function as soon as the first vowel is found;
a ``break`` would exit only the loop and continue in the function body.
