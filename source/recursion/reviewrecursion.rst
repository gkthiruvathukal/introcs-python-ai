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

#.  Inner helper pattern.

    a.  What is the advantage of putting the recursive ``helper`` function
        inside the outer ``binary_search`` function instead of using
        default parameters like ``lo=0`` and ``hi=None``?
    b.  Can the caller accidentally pass a wrong value for ``low`` or
        ``high`` when using the inner helper pattern?  Why or why not?

#.  Property-based testing with Hypothesis.

    a.  What does ``@given(st.lists(st.integers()), st.integers())`` tell
        Hypothesis to do?
    b.  Name two properties that the binary search test verifies for every
        generated input.
    c.  Why is property-based testing more thorough than writing a fixed
        set of example inputs by hand?

#.  Filesystem walker — observer pattern.

    a.  What four events does ``FileSystemEventWalker`` fire during a
        traversal?
    b.  What does returning ``False`` from ``enter_dir`` do?
    c.  Write a handler class that counts the total number of files
        visited, without printing anything.

#.  DFS vs BFS filesystem traversal.

    a.  In what order does depth-first traversal (DFS) visit entries
        compared to breadth-first traversal (BFS)?
    b.  DFS uses the call stack; BFS uses an explicit ``deque``.  What
        practical consequence does this have for very deep directory trees?
    c.  Give one scenario where BFS is the better choice over DFS.

#.  Recursive descent parser — grammar mapping.

    a.  In the arithmetic grammar, why does ``expr`` call ``term`` rather
        than handling multiplication itself?
    b.  Each grammar rule becomes one method in the ``Parser`` class.
        Which method handles parenthesised sub-expressions, and how does
        it re-enter the grammar?
    c.  What is *mutual recursion*, and where does it appear in the
        parser?

#.  Associativity in the recursive descent parser.

    a.  Why does ``expr`` use a ``while`` loop but ``power`` uses a
        single ``if`` with a recursive call?
    b.  Evaluate ``2 ^ 3 ^ 2`` by hand, showing how right-associativity
        groups the operands.
    c.  What would change in the output of ``calc("8 / 4 / 2")`` if
        division were accidentally made right-associative?

#.  Structural recursion in the evaluator.

    a.  What does it mean for recursion to be *structural*?
    b.  The ``eval_expr`` function uses Python ``match`` statements.
        What are the three cases it handles?
    c.  Trace the evaluation of ``BinOp(Number(2), '+', Number(3))``
        through ``eval_expr``, showing each recursive call and its
        return value.
