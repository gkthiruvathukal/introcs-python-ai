.. index:: tuple, tuple; syntax, tuple; immutability
   ACM-IEEE CS2013; SDF3 Fundamental Data Structures
   ACM-IEEE CS2023; SDF3 Fundamental Data Structures

.. _Tuple-Syntax:

Tuple Syntax
============

.. note::

   *Source:* Python-specific — C# has no direct equivalent in this edition.
   Python tuples are the immutable counterpart to lists.  Use them when a
   fixed-size, ordered collection should not be modified after creation.

A *tuple* is an ordered, *immutable* sequence of values.  Once created,
its elements cannot be changed.

Creating Tuples
---------------

.. index:: tuple; literal, tuple; constructor

Write a tuple with parentheses and commas:

.. code-block:: python

   point = (3, 7)
   rgb = (255, 128, 0)
   empty = ()

Parentheses are optional in most contexts — the comma is what makes a
tuple:

.. code-block:: python

   point = 3, 7        # also a tuple
   print(type(point))

Output:

.. code-block:: none

   <class 'tuple'>

A single-element tuple requires a trailing comma; without it, Python
treats the parentheses as grouping:

.. code-block:: python

   one = (42,)         # tuple with one element
   not_one = (42)      # just the integer 42
   print(type(one), type(not_one))

Output:

.. code-block:: none

   <class 'tuple'> <class 'int'>

Indexing and Length
--------------------

.. index:: tuple; index, tuple; len()

Tuples support indexing, slicing, and ``len()`` exactly like lists:

.. code-block:: python

   rgb = (255, 128, 0)
   print(rgb[0])        # 255
   print(rgb[-1])       # 0
   print(len(rgb))      # 3

Immutability
------------

.. index:: tuple; immutable

Attempting to change an element raises a ``TypeError``:

.. code-block:: python

   rgb = (255, 128, 0)
   rgb[0] = 100     # TypeError: 'tuple' object does not support item assignment

.. index:: tuple vs list, pair: tuple; when to use

Tuples vs. Lists
----------------

.. list-table::
   :header-rows: 1
   :widths: 35 35

   * - Tuple
     - List
   * - Immutable
     - Mutable
   * - ``(1, 2, 3)``
     - ``[1, 2, 3]``
   * - Can be a dict key
     - Cannot be a dict key
   * - Slightly faster
     - More flexible

**Use a tuple** when the structure is fixed by design: a coordinate, an
RGB colour, a database record field.

**Use a list** when items will be added, removed, or reordered.

Converting Between Tuples and Lists
-------------------------------------

.. index:: tuple(); list()

.. code-block:: python

   t = (1, 2, 3)
   lst = list(t)       # convert tuple → list
   lst.append(4)
   t2 = tuple(lst)     # convert list → tuple
   print(t2)

Output:

.. code-block:: none

   (1, 2, 3, 4)
