.. index:: review questions; tuples

.. _Review-Tuples:

Chapter Review Questions
========================

.. note::

   *Source:* Python-specific — no direct equivalent in the C# edition.
   Questions cover Python tuple syntax, immutability, unpacking, and
   common use cases.

#.  What is the key difference between a tuple and a list?

#.  How do you create a tuple with a single element?  What happens if
    you write ``(42)`` instead?

#.  Is the following valid Python?  What does it create?::

       t = 1, 2, 3

#.  What error occurs when you try to assign to an element of a tuple?

#.  Write one line of Python that swaps the values of variables ``x``
    and ``y`` without using a temporary variable.

#.  Given::

       data = (10, 20, 30, 40)

    Write an unpacking statement that assigns 10 to ``first``, 40 to
    ``last``, and ``[20, 30]`` to ``middle``.

#.  Why can a tuple be used as a dictionary key but a list cannot?

#.  What does ``zip([1, 2, 3], ["a", "b", "c"])`` produce?  Write a
    ``for`` loop that prints each pair on its own line.

#.  When would you choose a tuple over a list?  Give two concrete
    examples.

#.  What is the output of::

       a, b, c = (5, 10, 15)
       a, b = b, a
       print(a, b, c)
