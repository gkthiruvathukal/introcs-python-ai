.. index:: recursion, base case, recursive case, call stack

.. _Recursion-Intro:

Introduction to Recursion
=========================

.. note::

   *Source:* Adapted from the C# edition (``recursion/recursion.rst``).
   The C# chapter is a brief forward pointer; this section provides full
   Python coverage.  Recursive structure and base/recursive-case thinking
   are language-agnostic.  Python-specific additions: the default
   recursion limit and ``sys.setrecursionlimit``.

A function is *recursive* if it calls itself.  This sounds circular, but
it works because every recursive call moves closer to a *base case* that
does not recurse.

The Structure of a Recursive Function
---------------------------------------

.. index:: recursion; structure

Every correct recursive function has:

1. **One or more base cases** — inputs small enough to answer directly
   without another recursive call.
2. **One or more recursive cases** — the function calls itself with a
   *simpler* or *smaller* argument, making progress toward a base case.

Factorial
---------

.. index:: factorial; recursive

The mathematical definition of factorial is itself recursive:

.. code-block:: none

   0! = 1                    (base case)
   n! = n × (n-1)!           (recursive case)

In Python:

.. code-block:: python

   def factorial(n):
       if n == 0:
           return 1
       return n * factorial(n - 1)

.. code-block:: python

   print(factorial(5))   # 120

Trace for ``factorial(4)``:

.. code-block:: none

   factorial(4)
     = 4 * factorial(3)
     = 4 * 3 * factorial(2)
     = 4 * 3 * 2 * factorial(1)
     = 4 * 3 * 2 * 1 * factorial(0)
     = 4 * 3 * 2 * 1 * 1
     = 24

The Call Stack
--------------

.. index:: call stack; recursion

Each call to ``factorial`` creates a new *stack frame* holding its own
``n`` and the return address.  When the base case returns 1, frames
unwind in reverse order, multiplying as they go.

Fibonacci Numbers
-----------------

.. index:: Fibonacci; recursive

.. code-block:: python

   def fib(n):
       if n <= 1:
           return n
       return fib(n - 1) + fib(n - 2)

.. code-block:: python

   for i in range(8):
       print(fib(i), end=" ")

Output:

.. code-block:: none

   0 1 1 2 3 5 8 13

This is correct but slow: ``fib(n)`` makes two recursive calls, so the
number of calls grows exponentially.  ``fib(40)`` makes over a billion
calls.  The iterative version or *memoisation* (caching) is far faster
for large inputs.

Python's Recursion Limit
-------------------------

.. index:: sys.setrecursionlimit, recursion limit

Python limits recursive calls to prevent stack overflow.  The default
limit is 1000.  You can inspect or change it:

.. code-block:: python

   import sys
   print(sys.getrecursionlimit())   # 1000

   sys.setrecursionlimit(5000)

Hitting the limit raises ``RecursionError``.  For deeply recursive
problems (large ``n``), prefer an iterative solution or use Python's
``functools.lru_cache`` for memoisation.

When to Use Recursion
---------------------

Recursion is natural when the problem has a recursive structure:
tree traversal, divide-and-conquer algorithms (merge sort, quicksort,
binary search), and problems defined recursively (GCD, fractals).  For
simple counting loops, an iterative approach is clearer and faster.
