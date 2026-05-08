.. index:: recursion; examples, GCD; recursive, binary search; recursive,
           generator; factorial, generator; Fibonacci

.. _Recursion-Examples:

Recursion Examples
==================

.. note::

   *Source:* Adapted from the C# edition (``recursion/recursion.rst``).
   GCD and binary search are classic examples mentioned in the C# text;
   this section provides full Python implementations.  Flatten and
   directory traversal are Python-specific additions.

GCD — Euclidean Algorithm
--------------------------

.. index:: GCD; recursive, Euclidean algorithm

The greatest common divisor of two integers has an elegant recursive
definition:

.. code-block:: none

   gcd(a, 0) = a                  (base case)
   gcd(a, b) = gcd(b, a % b)     (recursive case)

.. code-block:: python

   def gcd(a: int, b: int) -> int:
       if b == 0:
           return a
       return gcd(b, a % b)

.. code-block:: python

   print(gcd(48, 18))   # 6
   print(gcd(100, 75))  # 25

Each call reduces ``b`` toward 0 because ``a % b < b`` for any ``b > 0``.
Python's standard library provides ``math.gcd`` which uses the same
algorithm.

Recursive Binary Search
------------------------

.. index:: binary search; recursive

Binary search on a sorted list can be expressed recursively: check the
midpoint, then recurse on the left or right half:

.. code-block:: python

   def binary_search(data: list, target, lo: int = 0, hi: int | None = None) -> int:
       if hi is None:
           hi = len(data) - 1
       if lo > hi:
           return -1             # not found
       mid = (lo + hi) // 2
       if data[mid] == target:
           return mid
       elif data[mid] < target:
           return binary_search(data, target, mid + 1, hi)
       else:
           return binary_search(data, target, lo, mid - 1)

.. code-block:: python

   data = [-5, 2, 8, 9, 12, 22]
   print(binary_search(data, 9))    # 3
   print(binary_search(data, 7))    # -1

Each recursive call halves the search space, giving O(log N) depth.

Flattening a Nested List
------------------------

.. index:: flatten; recursive, nested list

Some problems only make sense recursively.  Flattening an arbitrarily
nested list has no clean iterative equivalent:

.. code-block:: python

   def flatten(lst: list) -> list:
       result = []
       for item in lst:
           if isinstance(item, list):
               result.extend(flatten(item))
           else:
               result.append(item)
       return result

.. code-block:: python

   nested = [1, [2, 3], [4, [5, 6]], 7]
   print(flatten(nested))

Output:

.. code-block:: none

   [1, 2, 3, 4, 5, 6, 7]

Directory Tree Traversal
------------------------

.. index:: os.walk; recursive, directory traversal

File systems are trees — a natural fit for recursion:

.. code-block:: python

   from pathlib import Path

   def print_tree(path, indent: int = 0) -> None:
       print("  " * indent + path.name)
       if path.is_dir():
           for child in sorted(path.iterdir()):
               print_tree(child, indent + 1)

.. code-block:: python

   print_tree(Path("."))

The function calls itself for each subdirectory, unwinding naturally
when a directory has no more children.

Memoisation with ``lru_cache``
--------------------------------

.. index:: functools.lru_cache, memoisation

The naive recursive Fibonacci is exponential because it recomputes the
same values repeatedly.  ``functools.lru_cache`` stores results
automatically:

.. code-block:: python

   from functools import lru_cache

   @lru_cache(maxsize=None)
   def fib(n: int) -> int:
       if n <= 1:
           return n
       return fib(n - 1) + fib(n - 2)

.. code-block:: python

   print(fib(50))   # 12586269025 — computed instantly

With caching, each value of ``fib(n)`` is computed exactly once,
reducing the total work to O(N).

Generators for Sequences with a Ceiling
-----------------------------------------

.. index:: generator; infinite sequence, yield, itertools.takewhile

For sequences defined by a recurrence — like factorials and Fibonacci
numbers — Python *generators* offer a third style that is neither
recursive nor a plain loop.  A generator function uses ``yield`` to
produce one value at a time, suspending execution between calls.  This
makes it natural to express "generate values indefinitely, and let the
caller decide when to stop."

Infinite Factorial Generator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: generator; factorial

.. code-block:: python

   def factorials():
       """Yield 0!, 1!, 2!, 3!, ... without bound."""
       result = 1
       n = 0
       while True:
           yield result
           n += 1
           result *= n

The generator runs forever by design.  To collect only the values up to
a ceiling, use ``itertools.takewhile``:

.. code-block:: python

   from itertools import takewhile

   for f in takewhile(lambda x: x <= 1_000_000, factorials()):
       print(f)

Output:

.. code-block:: none

   1
   1
   2
   6
   24
   120
   720
   5040
   40320
   362880

You can also write a self-contained generator that accepts the ceiling
directly — useful when you want a single, reusable function:

.. code-block:: python

   def factorials_up_to(ceiling: int):
       """Yield each factorial that does not exceed *ceiling*."""
       if ceiling < 1:
           raise ValueError(f"ceiling must be >= 1, got {ceiling}")
       result, n = 1, 0
       while result <= ceiling:
           yield result
           n += 1
           result *= n

.. code-block:: python

   print(list(factorials_up_to(1_000_000)))

Output:

.. code-block:: none

   [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

Infinite Fibonacci Generator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: generator; Fibonacci

.. code-block:: python

   def fibonacci():
       """Yield F(0), F(1), F(2), ... without bound."""
       prev, curr = 0, 1
       while True:
           yield prev
           prev, curr = curr, prev + curr

.. code-block:: python

   from itertools import takewhile

   fibs = list(takewhile(lambda x: x <= 1000, fibonacci()))
   print(fibs)

Output:

.. code-block:: none

   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

Again, a ceiling-aware version keeps the intent local to the function:

.. code-block:: python

   def fibonacci_up_to(ceiling: int):
       """Yield each Fibonacci number that does not exceed *ceiling*."""
       if ceiling < 0:
           raise ValueError(f"ceiling must be >= 0, got {ceiling}")
       prev, curr = 0, 1
       while prev <= ceiling:
           yield prev
           prev, curr = curr, prev + curr

.. code-block:: python

   print(list(fibonacci_up_to(1000)))

Output:

.. code-block:: none

   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

Why Generators?
^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Property
     - Generators
   * - Memory
     - O(1) — only the current value is in memory at any time
   * - Stack depth
     - O(1) — no recursive frames; no ``RecursionError``
   * - Early termination
     - Natural with ``takewhile``, ``break``, or ``next()``
   * - Composability
     - Pipe generators through ``itertools`` functions freely

Generators are the idiomatic Python choice for producing a potentially
large (or infinite) sequence of values one at a time.  They combine the
clarity of recursive definitions with the efficiency of iterative loops.
