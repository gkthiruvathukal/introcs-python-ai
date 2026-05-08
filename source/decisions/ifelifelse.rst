.. index:: elif, if-elif-else

``if``-``elif``-``else`` Statements
====================================

.. note::

   *Source:* Adapted from the C# edition (``decisions/ifelsechained.rst``).
   The grade-classification and wages examples are Python adaptations of the
   original C# examples.  The BMI and ticket-price examples are original
   additions.

When there are more than two choices, chain conditions using ``elif``
(short for "else if").  Python uses ``elif`` where C# uses ``else if``.

.. index:: elif; grade example, if-elif-else; pattern

Grade Classification
--------------------

.. code-block:: python

   score = int(input("Enter score (0-100): "))
   if score >= 90:
       grade = "A"
   elif score >= 80:
       grade = "B"
   elif score >= 70:
       grade = "C"
   elif score >= 60:
       grade = "D"
   else:
       grade = "F"
   print(f"Grade: {grade}")

Python evaluates the conditions top to bottom and executes the first
block whose condition is ``True``.  Once a branch runs, the rest are
skipped.  The ``else`` at the end is a catch-all — it runs only when
*none* of the earlier conditions were true.

.. note::

   The conditions above are ordered from highest to lowest.  Because
   we already know ``score < 90`` by the time we test ``score >= 80``,
   there is no need to write ``80 <= score < 90``.  Each ``elif``
   implicitly carries the negation of all previous conditions.

General Form
------------

.. code-block:: none

   if condition1:
       statements
   elif condition2:
       statements
   elif condition3:
       statements
   ...
   else:
       statements

Any number of ``elif`` clauses is allowed.  The ``else`` clause is
optional but good practice when one of the choices should always apply.

Wages with Overtime
-------------------

.. literalinclude:: ../../examples/introcs-python/decisions/wages.py
   :language: python

Sample run:

.. code-block:: none

   Hours worked: 45
   Hourly rate: $20
   Weekly wages: $950.00

BMI Categories
--------------

Here is an example with four ``elif`` branches:

.. literalinclude:: ../../examples/introcs-python/decisions/bmi.py
   :language: python

``if``-``elif``-``else`` Exercise
-----------------------------------

Write a function ``ticket_price(age)`` that returns the ticket price
based on the following rules:

- Under 5: free (``0``)
- 5–12: ``$8``
- 13–64: ``$15``
- 65 and over: ``$10``

Test it with ages 3, 10, 30, and 70.
