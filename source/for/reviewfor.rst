.. index:: review questions; for loops

.. _Review-For:

Chapter Review Questions
========================

#.  Choosing the right loop.

    a.  When might you prefer a ``for`` loop over a ``while`` loop?
    b.  What do you gain by using ``for``?

#.  When might you prefer a ``while`` loop over a ``for`` loop?

#.  When you have nested ``for`` loops and reach the bottom of the *inner*
    loop body, where does execution go next?

#.  Write a ``range()`` expression that produces: ``0, 1, 2, 3, 4``.

#.  Write a ``range()`` expression that produces: ``3, 4, 5, 6, 7``.

#.  Write a ``range()`` expression that produces: ``0, 3, 6, 9, 12``.

#.  Write a ``range()`` expression that produces: ``10, 8, 6, 4, 2``.

#.  Rewrite the following without using ``+=``::

       total += score

#.  Rewrite the following using a compound assignment operator so that
    ``big_name`` appears only once::

       big_name = big_name * 2

#.  What does ``enumerate()`` give you that a plain ``for item in seq:``
    loop does not?

#.  What is printed?  Trace through by hand before running::

       for i in range(1, 4):
           for j in range(i):
               print(j, end=" ")
           print()

#.  What is printed?::

       s = "abcde"
       for i in range(0, len(s), 2):
           print(s[i])

#.  Write a list comprehension that produces the cubes of 1 through 5:
    ``[1, 8, 27, 64, 125]``.

#.  Write a list comprehension equivalent to::

       result = []
       for w in ["hello", "world", "python"]:
           if len(w) > 4:
               result.append(w.upper())

#.  Two similar expressions.

    a.  What is the type and value of ``[n * 2 for n in range(5)]``?
    b.  What is the type and value of ``(n * 2 for n in range(5))``?
    c.  When would you prefer the second form?
