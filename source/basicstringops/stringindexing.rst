.. index:: string; indexing, string; slicing

.. _string-indexing:

String Indexing and Slicing
============================

Strings are sequences of characters.  Python counts positions starting at
**0**, so the indices of the characters in ``"coding"`` are:

+-------------+-----+-----+-----+-----+-----+-----+
| Index       | 0   | 1   | 2   | 3   | 4   | 5   |
+-------------+-----+-----+-----+-----+-----+-----+
| Character   | c   | o   | d   | i   | n   | g   |
+-------------+-----+-----+-----+-----+-----+-----+

There are 6 characters and the last index is 5 — one less than the length.

.. warning::

   The last valid index is ``len(s) - 1``, not ``len(s)``.
   Accessing ``s[6]`` on a six-character string raises an ``IndexError``.

.. index:: string; subscript

Subscript Notation
------------------

Use square brackets to access a single character:

.. code-block:: none

   >>> s = "coding"
   >>> s[0]
   'c'
   >>> s[2]
   'd'
   >>> s[5]
   'g'

The result is always a one-character string.

The subscript can be any expression that evaluates to an integer:

.. code-block:: none

   >>> n = 3
   >>> s[n - 1]
   'd'

.. index:: string; negative index

Negative Indices
----------------

Python allows *negative* indices that count from the right end:

.. code-block:: none

   >>> s = "coding"
   >>> s[-1]     # last character
   'g'
   >>> s[-2]     # second from last
   'n'
   >>> s[-6]     # same as s[0]
   'c'

``s[-1]`` is equivalent to ``s[len(s) - 1]``.

.. index:: string; slice, slice notation

Slicing
-------

A *slice* extracts a substring using the notation ``s[start:stop]``.
The result includes characters from index ``start`` up to, **but not
including**, index ``stop``:

.. code-block:: none

   >>> s = "coding"
   >>> s[1:4]
   'odi'
   >>> s[0:3]
   'cod'

Omitting either end uses the beginning or end of the string:

.. code-block:: none

   >>> s[:3]     # from the start
   'cod'
   >>> s[3:]     # to the end
   'ing'
   >>> s[:]      # whole string (copy)
   'coding'

Slices work with negative indices too:

.. code-block:: none

   >>> s[-3:]    # last three characters
   'ing'
   >>> s[:-2]    # everything except the last two
   'codi'

.. index:: string; step in slice

Step in Slices
--------------

An optional third number specifies a *step*:

.. code-block:: none

   >>> s = "abcdefgh"
   >>> s[::2]       # every other character
   'aceg'
   >>> s[::-1]      # reverse the string
   'hgfedcba'

Reversing with ``[::-1]`` is an idiomatic Python trick worth remembering.

Indexing Exercise
-----------------

Predict what each line prints, then verify in the REPL:

.. code-block:: python

   s = "fragment"
   k = 3
   print(s[1])
   print(s[k])
   print(s[2 * k - 2])
   print(s[-1])
   print(s[2:5])
   print(s[::-1])
