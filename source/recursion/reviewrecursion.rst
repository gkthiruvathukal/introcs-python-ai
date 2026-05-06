.. index:: review questions; recursion

.. _Review-Recursion:

Chapter Review Questions
========================

.. note::

   *Source:* Adapted from the C# edition (``recursion/recursion.rst``).
   The C# chapter is a brief placeholder; these questions cover the full
   Python recursion content presented in this chapter.

#.  What are the two essential parts of every correct recursive function?

#.  What error does Python raise when the recursion limit is exceeded?
    What is the default limit?

#.  Trace ``factorial(3)`` step by step, showing each recursive call and
    its return value.

#.  Why is the naive recursive Fibonacci slow for large ``n``?  What is
    the time complexity in terms of the number of calls made?

#.  What does ``functools.lru_cache`` do, and how does it improve the
    performance of recursive Fibonacci?

#.  Write a recursive function ``sum_list(lst)`` that returns the sum
    of all integers in a list, without using ``sum()``.

#.  In the recursive GCD algorithm, what is the base case?  Why does the
    algorithm always terminate?

#.  What is a *call stack*?  What happens to it as recursive calls
    are made and as they return?

#.  When is recursion a better choice than an iterative loop?
    Give one concrete example.

#.  The recursive binary search splits the problem in half at each step.
    What is the maximum recursion depth for a list of 1024 elements?
