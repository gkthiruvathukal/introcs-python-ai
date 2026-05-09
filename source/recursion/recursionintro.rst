.. index:: recursion, base case, recursive case, call stack

.. _Recursion-Intro:

Introduction to Recursion
=========================

.. note::

   *Source:* Adapted from the C# edition (``recursion/recursion.rst``).
   The C# chapter is a brief forward pointer; this section provides full
   Python coverage.  Recursive structure and base/recursive-case thinking
   are language-agnostic.  Python-specific additions: the default
   recursion limit, ``sys.setrecursionlimit``, the absence of
   tail-call optimisation, and the security implications of unbounded
   recursion.

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

.. index:: factorial; recursive, factorial; iterative

The mathematical definition of factorial is itself recursive:

.. code-block:: none

   0! = 1                    (base case)
   n! = n × (n-1)!           (recursive case)

A recursive Python implementation follows that definition directly:

.. code-block:: python

   def factorial_recursive(n: int) -> int:
       if n < 0:
           raise ValueError(f"factorial not defined for negative integers: {n}")
       if n == 0:
           return 1
       return n * factorial_recursive(n - 1)

Trace for ``factorial_recursive(4)``:

.. code-block:: none

   factorial_recursive(4)
     = 4 * factorial_recursive(3)
     = 4 * 3 * factorial_recursive(2)
     = 4 * 3 * 2 * factorial_recursive(1)
     = 4 * 3 * 2 * 1 * factorial_recursive(0)
     = 4 * 3 * 2 * 1 * 1
     = 24

Both versions reject negative inputs with a ``ValueError``, because
factorial is undefined for negative integers.  Raising an exception here
is the right choice: a negative argument is a programming error, not an
expected outcome.

Factorial is *not* an ideal candidate for recursion in Python.  It
requires one stack frame per integer, so ``factorial_recursive(1000)``
will hit the default recursion limit.  The iterative version is simpler,
faster, and scales to any size:

.. code-block:: python

   def factorial_iterative(n: int) -> int:
       if n < 0:
           raise ValueError(f"factorial not defined for negative integers: {n}")
       result = 1
       for i in range(2, n + 1):
           result *= i
       return result

.. code-block:: python

   print(factorial_iterative(5))    # 120
   print(factorial_iterative(100))  # works fine — no stack limit

Python's standard library also provides ``math.factorial(n)``, which is
implemented in C and is the best choice in real code.

.. index:: stack frame; recursion, call stack; depth

The Call Stack
--------------

.. index:: call stack; recursion

Each call to a recursive function creates a new *stack frame* holding its
own local variables and the return address.  When the base case returns,
frames unwind in reverse order.  For ``factorial_recursive(4)``, four
frames are pushed before any frame is popped.

Fibonacci Numbers
-----------------

.. index:: Fibonacci; recursive, Fibonacci; iterative

.. code-block:: python

   def fib_recursive(n: int) -> int:
       if n < 0:
           raise ValueError(f"Fibonacci not defined for negative indices: {n}")
       if n <= 1:
           return n
       return fib_recursive(n - 1) + fib_recursive(n - 2)

.. code-block:: python

   for i in range(8):
       print(fib_recursive(i), end=" ")

Output:

.. code-block:: none

   0 1 1 2 3 5 8 13

Both versions reject negative ``n`` for the same reason: the Fibonacci
sequence is conventionally defined only for non-negative indices, and a
negative argument almost certainly indicates a caller bug.

This is correct but extremely slow: ``fib_recursive(n)`` makes two
recursive calls, so the total number of calls grows exponentially —
``fib_recursive(40)`` makes over a billion calls.  Like factorial,
Fibonacci is *not* an ideal candidate for recursion.

The iterative version computes the same result in O(N) time with no
stack growth at all:

.. code-block:: python

   def fib_iterative(n: int) -> int:
       if n < 0:
           raise ValueError(f"Fibonacci not defined for negative indices: {n}")
       if n <= 1:
           return n
       prev, curr = 0, 1
       for _ in range(2, n + 1):
           prev, curr = curr, prev + curr
       return curr

.. code-block:: python

   print(fib_iterative(40))   # 102334155 — instant
   print(fib_iterative(100))  # 354224848179261915075 — no problem

Use the iterative form (or memoisation — see :ref:`Recursion-Examples`)
whenever you need Fibonacci for large ``n``.

Python's Recursion Limit
-------------------------

.. index:: sys.setrecursionlimit, recursion limit, RecursionError

Python limits recursive calls to prevent the call stack from growing
without bound.  The default limit is 1 000.  You can inspect or raise it:

.. code-block:: python

   import sys
   print(sys.getrecursionlimit())   # 1000

   sys.setrecursionlimit(5000)      # use with caution

Hitting the limit raises ``RecursionError``.

.. index:: tail recursion, van Rossum, Guido; TCO decision

No Tail-Call Optimisation
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: tail-call optimisation, TCO

Some languages (Scheme, Haskell, Kotlin) detect *tail calls* — recursive
calls that are the very last action of a function — and reuse the current
stack frame instead of creating a new one.  **Python does not perform
tail-call optimisation.**  Even a perfectly tail-recursive function
allocates a new frame on every call, so it hits the recursion limit just
as fast as any other recursive function.  This is a deliberate design
decision: Guido van Rossum wanted stack traces to always show the full
call history, which TCO would erase.

Security Implications of Unbounded Recursion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: recursion; security, denial of service; recursion, stack exhaustion

When a recursive function is called with input that controls the depth —
for example, parsing a deeply-nested data structure received from a
network — an attacker can craft input that exhausts the call stack.
Stack exhaustion crashes the Python interpreter or, in a server context,
terminates the worker process.  This is a form of **denial-of-service
(DoS)**.

Mitigations:

- **Validate depth before recursing.** Reject or truncate input whose
  nesting depth exceeds a safe threshold.
- **Use an explicit stack.** Rewrite the algorithm iteratively with a
  list acting as a stack; then the "stack" lives on the heap and is
  bounded only by available memory, not the call-stack limit.
- **Do not raise ``sys.setrecursionlimit`` in production** in response
  to untrusted input — that only delays the crash and may exhaust
  memory entirely.

.. index:: recursion; when to use, divide and conquer, tree traversal

When to Use Recursion
---------------------

Recursion is natural when the problem has an inherently recursive
structure: tree traversal, divide-and-conquer algorithms (merge sort,
quicksort, binary search), and problems defined recursively (GCD,
directory trees, fractals).

Simple counting problems like factorial and Fibonacci belong in an
iterative loop.  A good rule of thumb: if you can easily describe
the algorithm with a ``for`` loop, prefer the loop.
