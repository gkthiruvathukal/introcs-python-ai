.. index:: recursion; examples, GCD; recursive, binary search; recursive

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

   def gcd(a, b):
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

   def binary_search(data, target, lo=0, hi=None):
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

   def flatten(lst):
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

   def print_tree(path, indent=0):
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
   def fib(n):
       if n <= 1:
           return n
       return fib(n - 1) + fib(n - 2)

.. code-block:: python

   print(fib(50))   # 12586269025 — computed instantly

With caching, each value of ``fib(n)`` is computed exactly once,
reducing the total work to O(N).
