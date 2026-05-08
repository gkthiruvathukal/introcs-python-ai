.. index:: while; sequence iteration, string; while loop

.. _While-Sequence:

While Loops with Sequences
===========================

.. note::

   *Source:* Adapted from the C# edition (``while/while-with-sequence.rst``).
   One-char-per-line and vowel-counting examples are Python translations.
   The note about ``for`` loops is an original forward reference.

Strings are sequences of characters that we can access by index.  Before
the ``for`` loop chapter, we use ``while`` loops with an index variable to
process strings one character at a time.

One Character Per Line
-----------------------

To print each character of a string on its own line:

.. literalinclude:: ../../examples/introcs-python/while/string_utils.py
   :language: python
   :start-after: # start: one_char_per_line
   :end-before: # end: one_char_per_line

.. code-block:: python

   one_char_per_line("bug")

Output:

.. code-block:: none

   b
   u
   g

Following the loop-planning rubric:

- **Changing variable**: ``i`` (the index)
- **Initial value**: ``0``
- **Continuation condition**: ``i < len(s)`` (valid indices are 0 through ``len(s)-1``)
- **Update**: ``i += 1``

Counting Vowels
---------------

.. literalinclude:: ../../examples/introcs-python/while/string_utils.py
   :language: python
   :start-after: # start: count_vowels
   :end-before: # end: count_vowels

.. code-block:: python

   print(count_vowels("Hello World"))   # 3

Checking for All Digits
------------------------

.. literalinclude:: ../../examples/introcs-python/while/string_utils.py
   :language: python
   :start-after: # start: all_digits
   :end-before: # end: all_digits

.. code-block:: python

   print(all_digits("12345"))   # True
   print(all_digits("123a5"))   # False

Note the early ``return False`` — as soon as a non-digit is found, there
is no need to check further.

Finding a Character
-------------------

Search for the first occurrence of a target character:

.. literalinclude:: ../../examples/introcs-python/while/string_utils.py
   :language: python
   :start-after: # start: find_char
   :end-before: # end: find_char

This is essentially what ``s.find(target)`` does internally.

.. note::

   The ``for`` loop (covered in the next chapter) makes iterating over a
   string much cleaner — ``for ch in s:`` instead of managing an index
   manually.  The ``while`` forms above are shown to build understanding
   of how indexing works; in practice you will almost always use ``for``.
