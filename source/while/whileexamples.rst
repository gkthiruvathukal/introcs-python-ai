.. index:: bisection method, numerical methods

While Loop Examples
===================

.. _bisection-method:

Bisection Method
----------------

For a striking example of while loops in action, consider a problem from
scientific computing: finding a root of a function — a value of ``x`` where
``f(x) = 0``.

In mathematics class you learned exact formulas for roots of polynomials.
In practice those methods rarely work beyond simple cases, so we
*approximate* solutions numerically instead.

The *bisection method* works for any continuous function.  You only need to
find two points ``a`` and ``b`` where ``f(a)`` and ``f(b)`` have *opposite
signs* — since the function is continuous and crosses zero somewhere between
them, there must be a root in the interval.

**Algorithm:** Find the midpoint ``c = (a + b) / 2``.

- If ``f(c)`` is close enough to zero, we are done — ``c`` is the root.
- Otherwise, ``f(c)`` has the opposite sign of either ``f(a)`` or ``f(b)``.
  Replace whichever endpoint matches the sign of ``f(c)`` with ``c``.
  This halves the interval while keeping a sign change across it.

Repeat until the interval is small enough.

Example: square root of 2
^^^^^^^^^^^^^^^^^^^^^^^^^^

We find the root of :math:`f(x) = x^2 - 2` in the interval [0, 2], which is
:math:`\sqrt{2} \approx 1.41421`.

.. literalinclude:: ../../examples/introcs-python/while/bisection.py
   :language: python

Output:

.. code-block:: none

   Root ≈ 1.4142135624
   math.sqrt(2) = 1.4142135624

The loop runs until the interval ``[a, b]`` is narrower than ``1e-10``.
Each iteration *halves* the interval, so it converges quickly — about 33
iterations to reach that tolerance starting from [0, 2].

Why This Matters
^^^^^^^^^^^^^^^^

.. index:: while loop; tolerance condition, precondition checking, first-class functions

The bisection method illustrates several important ideas:

- **While loops with a tolerance condition**: ``while (b - a) > tolerance``
  is a natural pattern for numerical algorithms that refine an estimate.
- **Precondition checking**: the function returns ``None`` (Python's null
  value) when the inputs violate the required precondition.
- **Passing a function as an argument**: ``f`` is passed to ``bisection``
  like any other value — a preview of Python's first-class functions.
