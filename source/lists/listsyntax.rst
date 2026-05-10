.. index:: list, list; syntax, list; indexing, list; slicing
   ACM-IEEE CS2013; SDF3 Fundamental Data Structures
   ACM-IEEE CS2023; SDF3 Fundamental Data Structures

.. _List-Syntax:

List Syntax
===========

A *list* is an ordered, mutable sequence of values.  It is the most
commonly used collection in Python.

Creating Lists
--------------

.. index:: list; literal, list; constructor

Use square brackets to write a list literal:

.. code-block:: python

   nums = [4, 7, -2, 5]
   words = ["up", "down", "over"]
   empty = []
   mixed = [1, "hello", 3.14]   # mixed types are allowed

``list()`` converts any iterable to a list:

.. code-block:: python

   chars = list("abc")
   print(chars)

Output:

.. code-block:: none

   ['a', 'b', 'c']

Indexing and Length
--------------------

.. index:: list; index, list; len(), negative index

Elements are accessed by integer index starting at 0:

.. code-block:: python

   nums = [4, 7, -2, 5]
   print(nums[0])    # first element
   print(nums[3])    # last element
   print(len(nums))  # number of elements

Output:

.. code-block:: none

   4
   5
   4

Negative indices count from the end: ``nums[-1]`` is the last element,
``nums[-2]`` is the second-to-last, and so on.

Mutation
--------

.. index:: list; mutable

Unlike strings, lists can be changed after creation:

.. code-block:: python

   nums = [4, 7, -2, 5]
   nums[2] = 99
   print(nums)

Output:

.. code-block:: none

   [4, 7, 99, 5]

Slicing
-------

.. index:: list; slicing, slice

A *slice* extracts a sub-list.  The syntax is ``lst[start:stop]``, which
returns elements from index ``start`` up to (but not including) ``stop``:

.. code-block:: python

   nums = [10, 20, 30, 40, 50]
   print(nums[1:4])   # indices 1, 2, 3
   print(nums[:3])    # from the beginning through index 2
   print(nums[2:])    # from index 2 to the end
   print(nums[:])     # a copy of the whole list

Output:

.. code-block:: none

   [20, 30, 40]
   [10, 20, 30]
   [30, 40, 50]
   [10, 20, 30, 40, 50]

A slice always produces a new list; the original is unchanged.

.. index:: list; membership test

Membership Test
---------------

.. index:: in; list membership

The ``in`` operator tests whether a value is anywhere in the list:

.. code-block:: python

   words = ["up", "down", "over"]
   print("down" in words)
   print("around" in words)

Output:

.. code-block:: none

   True
   False

Iterating Over a List
---------------------

.. index:: for; list iteration

Use a ``for`` loop to visit each element:

.. code-block:: python

   for word in ["cat", "dog", "bird"]:
       print(word.upper())

Output:

.. code-block:: none

   CAT
   DOG
   BIRD

To iterate with an index, use ``enumerate()``:

.. code-block:: python

   scores = [88, 73, 95]
   for i, score in enumerate(scores):
       print(f"{i}: {score}")

Output:

.. code-block:: none

   0: 88
   1: 73
   2: 95
