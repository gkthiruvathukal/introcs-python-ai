.. index:: if statement, Python; if syntax

.. _If-Statements:

Simple ``if`` Statements
========================

An ``if`` statement lets a program choose whether to execute a block of
code based on a condition.  Python's syntax uses a colon and indentation —
no braces, no parentheses around the condition.

.. index:: if; one-branch

One-Branch ``if``
-----------------

.. code-block:: python

   weight = float(input("Enter suitcase weight (lbs): "))
   if weight > 50:
       print("Overweight: $25 extra charge.")
   print("Thank you for flying with us.")

Try this with input ``30`` (no extra message) and ``55`` (extra charge
printed).  The indented ``print`` only runs when the condition is true.
The final ``print`` always runs.

General form:

.. code-block:: none

   if condition:
       statement(s)

The ``condition`` is any expression that evaluates to a Boolean.
The indented block (the *body*) executes only when the condition is
``True``.

.. warning::

   Python uses indentation to define blocks.  Every statement in the ``if``
   body must be indented by the same amount (4 spaces is the standard).
   A ``TabError`` or ``IndentationError`` means the indentation is
   inconsistent.

Two-Branch ``if``-``else``
--------------------------

When you want to do one thing if the condition is true and something
*different* if it is false, add an ``else`` clause:

.. code-block:: python

   temperature = float(input("Enter temperature (°F): "))
   if temperature > 60:
       print("Wear light clothes.")
   else:
       print("Bring a jacket.")

Exactly one of the two blocks executes.  The general form:

.. code-block:: none

   if condition:
       statement(s)    # executed when condition is True
   else:
       statement(s)    # executed when condition is False

Multi-Statement Bodies
-----------------------

The body can contain any number of statements, all indented to the same level:

.. code-block:: python

   balance = float(input("Account balance: $"))
   if balance < 0:
       transfer = -balance
       backup_account -= transfer
       balance += transfer
       print("Balance was negative; funds transferred from backup.")
   print(f"Current balance: ${balance:.2f}")

.. index:: conditional expression, ternary operator

``if`` as an Expression (Conditional Expression)
-------------------------------------------------

Python also has a one-line form called a *conditional expression*
(sometimes called a *ternary operator*):

.. code-block:: python

   label = "positive" if x > 0 else "non-positive"

This sets ``label`` to ``"positive"`` when ``x > 0``, otherwise
``"non-positive"``.  Use it for simple choices; a full ``if``/``else``
is clearer for anything more complex.

Simple If Exercises
-------------------

Predict the output for each fragment, then test in Python:

a. With ``v = "Hi"`` and again with ``v = "Hello there"``:

   .. code-block:: python

      v = input("Enter a word: ")
      if len(v) > 3:
          v = v + v
      print("Now we have", v)

b. With ``x = 7`` and again with ``x = -3``:

   .. code-block:: python

      x = int(input("Enter an integer: "))
      print("The magnitude of", x, "is", end=" ")
      if x < 0:
          x = -x
      print(x)
