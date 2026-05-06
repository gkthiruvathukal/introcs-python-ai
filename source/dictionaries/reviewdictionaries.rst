.. index:: review questions; dictionaries

.. _Review-Dictionaries:

Chapter Review Questions
========================

.. note::

   *Source:* Adapted from the C# edition (``dictionaries/reviewdictionaries.rst``).
   Questions updated for Python ``dict`` syntax and idioms.

#.  Is a Python ``dict`` mutable or immutable?

#.  What is the syntax to create a dictionary mapping ``"a"`` to 1 and
    ``"b"`` to 2?

#.  How do you iterate over all key-value pairs in a dictionary ``d``?

#.  What is the difference between ``d[key]`` and ``d.get(key, default)``?
    When would you prefer the second form?

#.  How is a dictionary like a list?  How is it different?

#.  What restriction applies to dictionary keys?  Why?

#.  What does ``d.pop("x", None)`` do if ``"x"`` is not in ``d``?

#.  Write one line that counts the number of entries in dictionary ``d``.

#.  Given::

       counts = {}
       for word in ["a", "b", "a", "c", "a", "b"]:
           counts[word] = counts.get(word, 0) + 1

    What is ``counts`` after the loop?

#.  Why is looking up a key in a dictionary O(1) on average, while
    searching for a value in a list is O(N)?

#.  What does ``collections.Counter`` add on top of a plain ``dict``?
    Give an example use case.

#.  Can a list be used as a dictionary key?  Can a tuple?  Explain why.
