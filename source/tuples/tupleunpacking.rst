.. index:: tuple unpacking, multiple assignment, swap variables

.. _Tuple-Unpacking:

Tuple Unpacking
===============

*Tuple unpacking* (also called *destructuring*) assigns each element of
a tuple to a separate variable in one statement.

Basic Unpacking
---------------

.. index:: tuple unpacking; basic

.. code-block:: python

   point = (3, 7)
   x, y = point
   print(x, y)

Output:

.. code-block:: none

   3 7

The number of variables on the left must match the number of elements
in the tuple (or you get a ``ValueError``).

Swapping Variables
------------------

.. index:: swap; variables

The cleanest way to swap two variables in Python uses tuple unpacking:

.. code-block:: python

   a, b = 10, 20
   a, b = b, a
   print(a, b)

Output:

.. code-block:: none

   20 10

Python evaluates the right-hand side completely before assigning, so no
temporary variable is needed.

Unpacking Function Return Values
----------------------------------

.. index:: tuple; multiple return values

A function can return multiple values as a tuple, and the caller can
unpack them:

.. code-block:: python

   def min_max(nums: list) -> tuple:
       return min(nums), max(nums)

   lo, hi = min_max([3, 1, 4, 1, 5, 9])
   print(lo, hi)

Output:

.. code-block:: none

   1 9

Unpacking in ``for`` Loops with ``zip()``
------------------------------------------

.. index:: zip(), for; tuple unpacking

``zip(a, b)`` pairs up elements from two sequences.  Unpacking in the
``for`` heading processes both at once:

.. code-block:: python

   names = ["Alice", "Bob", "Carol"]
   scores = [88, 73, 95]

   for name, score in zip(names, scores):
       print(f"{name}: {score}")

Output:

.. code-block:: none

   Alice: 88
   Bob: 73
   Carol: 95

``zip()`` stops at the shortest sequence.  Use ``zip(strict=True)`` in
Python 3.10+ to raise an error if the sequences have different lengths.

.. index:: star expression; unpacking, extended unpacking

Extended Unpacking
------------------

.. index:: tuple unpacking; *rest

A ``*`` prefix captures the "rest" of the sequence into a list:

.. code-block:: python

   first, *rest = [1, 2, 3, 4, 5]
   print(first)   # 1
   print(rest)    # [2, 3, 4, 5]

   *body, last = [1, 2, 3, 4, 5]
   print(body)    # [1, 2, 3, 4]
   print(last)    # 5
