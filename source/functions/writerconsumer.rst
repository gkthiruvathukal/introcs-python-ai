Two Roles: Writer and Consumer of Functions
============================================

.. note::

   *Source:* Adapted from the C# edition (``functions/writerconsumer.rst``).
   Docstrings and ``help()`` are Python-specific additions.  The contract and
   separation-of-concerns framing closely follow the C# original.

When working with functions, there are two distinct perspectives to keep in
mind: the *writer* of the function and the *consumer* (or caller) of the
function.

.. index:: function; writer role, docstring; contract

The Writer
----------

The writer is responsible for:

- Choosing a clear, descriptive name.
- Deciding what parameters the function needs.
- Writing the body so it correctly produces the intended result.
- Documenting what the function does (its *contract*) in a docstring.

A *docstring* is a string literal placed immediately after the ``def`` line.
Python tools can display it as help text:

.. literalinclude:: ../../examples/introcs-python/functions/wages.py
   :language: python
   :start-after: # start: weekly_wages
   :end-before: # end: weekly_wages

.. code-block:: none

   >>> help(weekly_wages)
   Help on function weekly_wages:

   weekly_wages(hours, rate)
       Return total weekly wages including 1.5x overtime above 40 hours.
       ...

.. index:: function; consumer role, abstraction; function contract

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

.. index:: separation of concerns, computation vs presentation

Separation of Concerns
----------------------

Good programs separate the *computation* (what is calculated) from the
*presentation* (how results are shown).  Functions help with this:

.. literalinclude:: ../../examples/introcs-python/functions/wages.py
   :language: python

The ``weekly_wages`` function only computes; ``main`` handles input and output.
