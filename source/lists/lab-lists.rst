.. index:: labs; lists

.. _lab-lists:

Lab: Lists
==========

Goals for this lab:

- Practice creating and modifying lists.
- Use loops and list methods to process sequences.
- Write functions that take and return lists.

.. index:: list; filter

1. Filter Positives
-------------------

Write a function ``filter_positives(nums)`` that returns a new list
containing only the positive numbers from ``nums``.

.. code-block:: python

   >>> filter_positives([3, -1, 4, -1, 5, -9, 2])
   [3, 4, 5, 2]

Write it first with a ``for`` loop and ``append``, then as a list
comprehension.

.. index:: list; accumulate

2. Running Total
-----------------

Write a function ``running_total(nums)`` that returns a new list where
each element is the cumulative sum of the original list up to that
index.

.. code-block:: python

   >>> running_total([1, 2, 3, 4])
   [1, 3, 6, 10]

.. index:: list; min, max

3. Manual Min and Max
---------------------

Without using the built-in ``min()`` or ``max()`` functions, write:

- ``list_min(nums)`` — returns the smallest element
- ``list_max(nums)`` — returns the largest element

Test with lists containing negative numbers, duplicates, and a
single-element list.

.. index:: list; rotate

4. Rotate Left
--------------

Write a function ``rotate_left(lst, k)`` that returns a new list
with all elements shifted left by ``k`` positions (elements that fall
off the left end wrap around to the right).

.. code-block:: python

   >>> rotate_left([1, 2, 3, 4, 5], 2)
   [3, 4, 5, 1, 2]
   >>> rotate_left([1, 2, 3], 0)
   [1, 2, 3]

Use slicing: the result is ``lst[k:] + lst[:k]``.
Then verify this by also writing an explicit loop version.

.. index:: list; two-pointer

5. Palindrome Check
-------------------

Write a function ``is_palindrome_list(lst)`` that returns ``True``
if the list reads the same forwards and backwards.

.. code-block:: python

   >>> is_palindrome_list([1, 2, 3, 2, 1])
   True
   >>> is_palindrome_list([1, 2, 3])
   False

Try two approaches:

a. Compare ``lst`` to ``lst[::-1]``.
b. Use two indices walking inward from both ends.
