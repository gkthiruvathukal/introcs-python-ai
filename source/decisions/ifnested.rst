.. index:: nested if, if; nested

Nested ``if`` Statements
========================

.. note::

   *Source:* Adapted from the C# edition (``decisions/ifnested.rst``).
   Python-specific indentation guidance is original.  Loan-approval and
   shipping-cost examples replace the original C# examples.

An ``if`` body can itself contain another ``if`` statement.  This is
called *nesting*.  Python's indentation makes the nesting level visually
obvious.

Example: Loan Approval
----------------------

A simple loan approval process requires both a minimum credit score
*and* sufficient income:

.. code-block:: python

   credit_score = int(input("Credit score: "))
   annual_income = float(input("Annual income: $"))

   if credit_score >= 650:
       if annual_income >= 30000:
           print("Loan approved.")
       else:
           print("Denied: income too low.")
   else:
       print("Denied: credit score too low.")

The outer ``if`` checks the credit score; only if that passes does the
inner ``if`` check the income.

.. index:: nested if; reading, indentation; nesting level

Reading Nested Code
--------------------

Indentation levels tell you which ``else`` belongs to which ``if``:

.. code-block:: python

   if a:
       if b:
           print("both a and b")
       else:
           print("a but not b")
   else:
       print("not a")

The ``else`` at indentation level 4 belongs to ``if b:``.
The ``else`` at indentation level 0 belongs to ``if a:``.

.. index:: flattening nested if, refactoring; conditions

Flattening Nested ``if`` With ``and``
--------------------------------------

When nesting exists only to combine conditions, you can often flatten it
using ``and``:

.. code-block:: python

   if credit_score >= 650 and annual_income >= 30000:
       print("Loan approved.")
   else:
       print("Denied.")

This is simpler when you do not need separate messages for each failure
reason.

Example: Shipping Cost
----------------------

Shipping cost depends on both weight and destination zone:

.. literalinclude:: ../../examples/introcs-python/decisions/shipping.py
   :language: python
   :start-after: # start: shipping_cost
   :end-before: # end: shipping_cost

Nesting is appropriate here because the cost formula differs by zone.

Avoiding Excessive Nesting
---------------------------

Deep nesting (three or more levels) is hard to read.  Consider these
refactoring options:

- Extract nested logic into a helper function.
- Use ``and`` / ``or`` to combine conditions.
- Use ``elif`` to flatten a chain of nested ``if``/``else`` statements.

.. code-block:: python

   # deep nesting — harder to follow
   if a:
       if b:
           if c:
               do_thing()

   # flattened with and — clearer
   if a and b and c:
       do_thing()
