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

#.  Two ways to look up a key.

    a.  What does ``d[key]`` do if the key is not present?
    b.  What does ``d.get(key, default)`` do instead?
    c.  When would you prefer the second form?

#.  Comparing dicts and lists.

    a.  How is a dictionary similar to a list?
    b.  How is it different?

#.  Dictionary key restrictions.

    a.  What restriction applies to dictionary keys?
    b.  Why does that restriction exist?

#.  What does ``d.pop("x", None)`` do if ``"x"`` is not in ``d``?

#.  Write one line that counts the number of entries in dictionary ``d``.

#.  Given::

       counts = {}
       for word in ["a", "b", "a", "c", "a", "b"]:
           counts[word] = counts.get(word, 0) + 1

    What is ``counts`` after the loop?

#.  Why is looking up a key in a dictionary O(1) on average, while
    searching for a value in a list is O(N)?

#.  ``collections.Counter``.

    a.  What does ``collections.Counter`` add on top of a plain ``dict``?
    b.  Give an example use case.

#.  Keys and mutability.

    a.  Can a list be used as a dictionary key?  Why or why not?
    b.  Can a tuple be used as a dictionary key?  Why or why not?
