.. index:: function; return value

Returned Function Values
========================

.. note::

   *Source:* Adapted from the C# edition (``functions/funcreturn.rst``).
   The weekly-wages example mirrors the C# original.  Python-specific
   details (implicit ``None`` return, early return pattern) are original
   additions.

So far, our functions have *done* something (printed output) but not
*produced* a value for the calling code to use.  Functions that return values
are far more flexible.

.. index:: return statement

The ``return`` Statement
------------------------

Use ``return`` to send a value back to the caller:

.. code-block:: python

   def add(a, b):
       return a + b

   result = add(3, 4)
   print(result)

Output:

.. code-block:: none

   7

The returned value can be used in any expression:

.. code-block:: none

   >>> add(3, 4) * 2
   14
   >>> print(f"Sum: {add(10, 5)}")
   Sum: 15

Example: Weekly Wages
---------------------

Here is a function that calculates wages including overtime:

.. code-block:: python

   def weekly_wages(hours, rate):
       """Return total weekly wages including overtime pay above 40 hours."""
       if hours <= 40:
           return hours * rate
       else:
           overtime = hours - 40
           return 40 * rate + overtime * rate * 1.5


   hours = float(input("Enter hours worked: "))
   rate = float(input("Enter hourly rate: $"))
   pay = weekly_wages(hours, rate)
   print(f"Weekly wages: ${pay:.2f}")

Sample run:

.. code-block:: none

   Enter hours worked: 45
   Enter hourly rate: $20
   Weekly wages: $950.00

The function *computes* the value and *returns* it; the calling code decides
what to do with it (here, print it).

.. index:: None; implicit return

Functions Without ``return``
-----------------------------

A function that does not have a ``return`` statement (or that reaches the end
without hitting one) automatically returns ``None``:

.. code-block:: none

   >>> def say_hi():
   ...     print("Hi!")
   ...
   >>> result = say_hi()
   Hi!
   >>> print(result)
   None

This is Python's way of handling what C# calls ``void`` functions.  Use
``return`` only when the caller needs a value.

.. index:: function; early return

Early Return
------------

A function can have more than one ``return`` statement.  Python exits the
function and returns as soon as it hits any ``return``:

.. code-block:: python

   def absolute_value(x):
       if x >= 0:
           return x
       return -x

The second ``return`` is only reached if ``x < 0``.
