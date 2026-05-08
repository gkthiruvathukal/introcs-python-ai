.. index:: interactive while loop, loop; interactive

.. _Interactive-while-Loops:

Interactive ``while`` Loops
============================

.. note::

   *Source:* Adapted from the C# edition (``while/whileinteractive.rst``).
   The ``input_in_range`` example is a Python translation.  The ``while True``
   + ``break`` form and the sentinel-value pattern are original Python additions.

An *interactive while loop* prompts the user for input each time through the
loop.  The loop continues until the user supplies a valid or expected value.

Repeating Until Valid Input
-----------------------------

A classic use: keep asking for a score until the user enters one in range.

.. code-block:: python

   score = int(input("Enter a score (0-100): "))
   while score < 0 or score > 100:
       print(f"{score} is out of range!")
       score = int(input("Enter a score (0-100): "))
   print(f"Score accepted: {score}")

Notice that ``input`` appears *twice* — once before the loop to get the
initial value, and once inside to refresh the value.  This is the
*read-before-loop* pattern.  The C# edition called this an unavoidable
duplication; Python's ``while True`` / ``break`` pattern avoids it:

.. index:: while True; interactive pattern

.. code-block:: python

   while True:
       score = int(input("Enter a score (0-100): "))
       if 0 <= score <= 100:
           break
       print(f"{score} is out of range!")
   print(f"Score accepted: {score}")

Both versions behave identically, but the ``while True`` form only writes
the ``input`` call once.

.. index:: sentinel value, loop; sentinel pattern

Sentinel Values
---------------

A *sentinel value* is a special input that signals "stop the loop."
For example, entering ``-1`` to end a list of scores:

.. code-block:: python

   total = 0
   count = 0
   score = int(input("Enter a score (-1 to stop): "))
   while score != -1:
       total += score
       count += 1
       score = int(input("Enter a score (-1 to stop): "))

   if count > 0:
       print(f"Average: {total / count:.1f}")
   else:
       print("No scores entered.")

Equivalently with ``while True``:

.. code-block:: python

   total = 0
   count = 0
   while True:
       score = int(input("Enter a score (-1 to stop): "))
       if score == -1:
           break
       total += score
       count += 1

   if count > 0:
       print(f"Average: {total / count:.1f}")

Menu Loop
---------

Interactive loops are often used to drive a menu:

.. literalinclude:: ../../examples/introcs-python/while/menu.py
   :language: python

The loop exits only when the user chooses option 3.

.. index:: loop; common pitfalls, floating point; comparison pitfall

Common Pitfalls
---------------

- **Forgetting to update the input inside the loop**: the loop never
  advances and runs forever.
- **Using ``==`` to compare floats**: rounding errors can prevent the
  condition from ever becoming ``False``.  Use a tolerance check instead:
  ``abs(x - target) < 0.0001``.
