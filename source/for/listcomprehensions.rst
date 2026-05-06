.. index:: list comprehension

.. _List-Comprehensions:

List Comprehensions
===================

.. note::

   *Source:* Python-specific — no equivalent exists in the C# edition.
   List comprehensions are a concise Python idiom for building lists from
   sequences.  Every list comprehension has an equivalent ``for`` loop; the
   examples below show both forms so you can see the correspondence.

A common pattern with ``for`` loops is building a new list by transforming
or filtering an existing sequence:

.. code-block:: python

   squares = []
   for n in range(1, 6):
       squares.append(n ** 2)
   print(squares)

Output:

.. code-block:: none

   [1, 4, 9, 16, 25]

Python provides a compact notation for exactly this pattern called a
*list comprehension*:

.. code-block:: none

   [expression  for  item  in  iterable]

The result is a new list containing ``expression`` evaluated once for each
``item`` in ``iterable``.

Basic Form
----------

.. index:: list comprehension; basic form

The squares example above becomes:

.. code-block:: python

   squares = [n ** 2 for n in range(1, 6)]
   print(squares)

Output:

.. code-block:: none

   [1, 4, 9, 16, 25]

More examples:

.. code-block:: python

   # ASCII codes of each character in a string
   codes = [ord(ch) for ch in "hello"]
   print(codes)

Output:

.. code-block:: none

   [104, 101, 108, 108, 111]

.. code-block:: python

   # Lengths of each word in a list
   words = ["cat", "elephant", "ox"]
   lengths = [len(w) for w in words]
   print(lengths)

Output:

.. code-block:: none

   [3, 8, 2]

Filtered Form
-------------

.. index:: list comprehension; with condition

Add an ``if`` clause to keep only items that satisfy a condition:

.. code-block:: none

   [expression  for  item  in  iterable  if  condition]

The equivalent ``for`` loop is:

.. code-block:: python

   result = []
   for item in iterable:
       if condition:
           result.append(expression)

Example — keep only the even numbers from 0 to 19:

.. code-block:: python

   evens = [n for n in range(20) if n % 2 == 0]
   print(evens)

Output:

.. code-block:: none

   [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

Example — extract only the vowels from a string:

.. code-block:: python

   s = "introduction"
   vowels = [ch for ch in s if ch in "aeiou"]
   print(vowels)

Output:

.. code-block:: none

   ['i', 't', 'o', 'd', 'u', 't', 'i', 'o']

Nested Comprehensions
---------------------

.. index:: list comprehension; nested

You can nest ``for`` clauses to iterate over two sequences simultaneously.
This produces a flat list — not a list of lists:

.. code-block:: python

   pairs = [(r, c) for r in range(3) for c in range(3)]
   print(pairs)

Output:

.. code-block:: none

   [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

The leftmost ``for`` is the outer loop; the rightmost is the inner loop —
the same order as nested ``for`` statements written out explicitly.

When to Use List Comprehensions
--------------------------------

Use a list comprehension when the goal is to *produce a list* from a
sequence.  Prefer a regular ``for`` loop when the body has side effects
(printing, writing a file, mutating external state) or when the logic is
complex enough that a one-liner hurts readability.

A good rule of thumb: if you can read the comprehension aloud as a single
English phrase — "the square of n for n in range 1 to 5" — it is probably
clear enough to use.
