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

.. code-block:: python

   def one_char_per_line(s: str) -> None:
       """Print each character of s on a separate line."""
       i = 0
       while i < len(s):
           print(s[i])
           i += 1

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

.. code-block:: python

   def count_vowels(s: str) -> int:
       """Return the number of vowel characters in s."""
       vowels = "aeiouAEIOU"
       count = 0
       i = 0
       while i < len(s):
           if s[i] in vowels:
               count += 1
           i += 1
       return count

   print(count_vowels("Hello World"))   # 3

Checking for All Digits
------------------------

.. code-block:: python

   def all_digits(s: str) -> bool:
       """Return True if every character of s is a digit."""
       i = 0
       while i < len(s):
           if not s[i].isdigit():
               return False
           i += 1
       return True

   print(all_digits("12345"))   # True
   print(all_digits("123a5"))   # False

Note the early ``return False`` — as soon as a non-digit is found, there
is no need to check further.

Finding a Character
-------------------

Search for the first occurrence of a target character:

.. code-block:: python

   def find_char(s: str, target: str) -> int:
       """Return the index of the first occurrence of target in s, or -1."""
       i = 0
       while i < len(s):
           if s[i] == target:
               return i
           i += 1
       return -1

This is essentially what ``s.find(target)`` does internally.

.. note::

   The ``for`` loop (covered in the next chapter) makes iterating over a
   string much cleaner — ``for ch in s:`` instead of managing an index
   manually.  The ``while`` forms above are shown to build understanding
   of how indexing works; in practice you will almost always use ``for``.
