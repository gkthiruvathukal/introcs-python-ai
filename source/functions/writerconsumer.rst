Two Roles: Writer and Consumer of Functions
============================================

.. note::

   *Source:* Adapted from the C# edition (``functions/writerconsumer.rst``).
   Docstrings and ``help()`` are Python-specific additions.  The contract and
   separation-of-concerns framing closely follow the C# original.

When working with functions, there are two distinct perspectives to keep in
mind: the *writer* of the function and the *consumer* (or caller) of the
function.

The Writer
----------

The writer is responsible for:

- Choosing a clear, descriptive name.
- Deciding what parameters the function needs.
- Writing the body so it correctly produces the intended result.
- Documenting what the function does (its *contract*) in a docstring.

A *docstring* is a string literal placed immediately after the ``def`` line.
Python tools can display it as help text:

.. code-block:: python

   def weekly_wages(hours, rate):
       """Return total weekly wages including 1.5x overtime above 40 hours.

       hours -- total hours worked (float)
       rate  -- regular hourly wage in dollars (float)
       """
       if hours <= 40:
           return hours * rate
       else:
           return 40 * rate + (hours - 40) * rate * 1.5

.. code-block:: none

   >>> help(weekly_wages)
   Help on function weekly_wages:

   weekly_wages(hours, rate)
       Return total weekly wages including 1.5x overtime above 40 hours.
       ...

The Consumer
------------

The consumer does not need to know *how* the function is implemented — only
*what* it does (its contract):

- What are the parameters and their expected types?
- What does it return?
- Are there any preconditions (e.g., ``hours`` must be non-negative)?

A well-written function with a clear docstring can be used correctly without
reading the body.  This is the power of *abstraction* — you hide the details
so the consumer can focus on their own problem.

The Contract
------------

The docstring defines the *contract* between writer and consumer:

- The consumer promises to call the function with valid arguments.
- The writer promises to return the correct result for valid arguments.

If the consumer violates the preconditions (e.g., passes a negative number of
hours), the function is not obligated to produce a sensible result.

Separation of Concerns
----------------------

Good programs separate the *computation* (what is calculated) from the
*presentation* (how results are shown).  Functions help with this:

.. code-block:: python

   def weekly_wages(hours, rate):
       """Return total weekly pay."""
       if hours <= 40:
           return hours * rate
       return 40 * rate + (hours - 40) * rate * 1.5

   def main():
       hours = float(input("Hours worked: "))
       rate = float(input("Hourly rate: $"))
       pay = weekly_wages(hours, rate)
       print(f"Weekly wages: ${pay:.2f}")

   if __name__ == '__main__':
       main()

The ``weekly_wages`` function only computes; ``main`` handles input and output.
