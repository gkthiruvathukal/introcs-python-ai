.. index:: dict; efficiency, hash table, O(1) lookup
   ACM-IEEE CS2013; AL3 Fundamental Data Structures and Algorithms
   ACM-IEEE CS2023; AL3 Fundamental Data Structures and Algorithms

.. _Dictionary-Efficiency:

Dictionary Efficiency
=====================

.. note::

   *Source:* Adapted from the C# edition (``dictionaries/dictionaryefficiency.rst``).
   The hash-table explanation is language-agnostic; the Python context
   replaces C#'s ``List.IndexOf`` with Python's ``list.index()``.

Why is dictionary lookup so fast?  This section explains the idea behind
hash tables — the data structure that makes O(1) average lookup possible.

The Naive Approach: Parallel Lists
------------------------------------

.. index:: parallel lists

You could simulate a dictionary with two parallel lists — one for keys,
one for values — and search for a key with a linear scan:

.. code-block:: python

   keys   = ["one", "two", "three"]
   values = ["uno", "dos", "tres"]

   def slow_lookup(keys: list[str], values: list[str], key: str) -> str:
       i = keys.index(key)   # linear search: O(N)
       return values[i]

``list.index()`` scans from left to right, so on average it examines
N/2 elements — *linear order* O(N).  For a dictionary with one million
entries, this means up to a million comparisons per lookup.

Hash Tables
-----------

.. index:: hash table, hash function

A *hash table* uses a *hash function* to convert a key directly into an
array index.  The idea:

1. Compute ``h = hash(key)`` — a large integer derived from the key's
   content.
2. Use ``h % table_size`` to pick a slot in an internal array.
3. Store the value in that slot.

For lookup, repeat steps 1–2 to find the same slot without searching.
This makes both insert and lookup O(1) *on average*, regardless of how
many entries the dictionary holds.

.. code-block:: python

   print(hash("one"))      # some large integer, e.g. 3713082716806266542
   print(hash("two"))      # a different integer
   print(hash(42))         # integers hash to themselves (usually)

The Immutability Requirement
-----------------------------

.. index:: dict; key must be immutable, hash; immutability

For a hash table to work, the hash of a key must never change while it
is in the dictionary.  If it did, the key could no longer be found.
This is why dictionary keys must be *immutable*: strings, numbers, and
tuples are allowed; lists and other mutable objects are not.

.. code-block:: python

   d = {}
   d[(1, 2)] = "point"   # tuple key: OK
   # d[[1, 2]] = "point" # list key: TypeError

.. index:: Big-O notation; dictionary, O(1); dict operations

Performance Summary
-------------------

.. index:: O(1) vs O(N)

+----------------------------+--------------------+
| Operation                  | Average time       |
+============================+====================+
| ``key in d``               | O(1)               |
+----------------------------+--------------------+
| ``d[key]``                 | O(1)               |
+----------------------------+--------------------+
| ``d[key] = value``         | O(1)               |
+----------------------------+--------------------+
| ``key in list``            | O(N)               |
+----------------------------+--------------------+
| ``list.index(key)``        | O(N)               |
+----------------------------+--------------------+

The constant-time guarantee makes dictionaries the right tool whenever
you need to look up data by a meaningful key rather than by position.
