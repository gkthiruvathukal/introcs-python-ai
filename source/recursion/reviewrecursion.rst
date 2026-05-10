.. index:: review questions; recursion

.. _Review-Recursion:

Chapter Review Questions
========================

#.  What are the two essential parts of every correct recursive function?

#.  Python's recursion limit.

    a.  What error does Python raise when the recursion limit is exceeded?
    b.  What is the default limit?

#.  Trace ``factorial(3)`` step by step, showing each recursive call and
    its return value.

#.  Naive recursive Fibonacci.

    a.  Why is the naive recursive Fibonacci slow for large ``n``?
    b.  What is the time complexity in terms of the number of calls made?

#.  Memoization with ``lru_cache``.

    a.  What does ``functools.lru_cache`` do?
    b.  How does it improve the performance of recursive Fibonacci?

#.  Write a recursive function ``sum_list(lst)`` that returns the sum
    of all integers in a list, without using ``sum()``.

#.  Recursive GCD.

    a.  In the recursive GCD algorithm, what is the base case?
    b.  Why does the algorithm always terminate?

#.  The call stack.

    a.  What is a *call stack*?
    b.  What happens to it as recursive calls are made?
    c.  What happens to it as those calls return?

#.  When is recursion a better choice than an iterative loop?
    Give one concrete example.

#.  The recursive binary search splits the problem in half at each step.
    What is the maximum recursion depth for a list of 1024 elements?
