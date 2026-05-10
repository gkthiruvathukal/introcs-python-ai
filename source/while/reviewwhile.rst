.. index:: review questions; while loops

.. _Review-While:

Chapter Review Questions
========================

#.  When should you prefer a ``while`` loop over a ``for`` loop?

#.  What is an *infinite loop*?

    a.  Give an example of code that produces one.
    b.  How do you stop an infinite loop that is running in a terminal?

#.  What is a *sentinel value* in a ``while`` loop?

    a.  Define the term.
    b.  Write a short loop that reads integers from the user until the
        user enters ``0``, then prints the sum.

#.  Consider this loop::

        n = 10
        while n > 0:
            print(n)
            n -= 3

    a.  What does it print?
    b.  Does it terminate?  Explain why.

#.  What does ``break`` do inside a ``while`` loop?

#.  What does ``continue`` do inside a ``while`` loop?
    How is it different from ``break``?

#.  Write a ``while`` loop that prints the powers of 2 (1, 2, 4, 8, …)
    that are less than 1000.

#.  Input validation.

    a.  Write a loop that repeatedly asks the user to enter a positive
        integer and keeps asking until they do.
    b.  Why is a ``while`` loop more appropriate than a ``for`` loop for
        this task?

#.  Trace the following code by hand and predict the output::

        i = 1
        total = 0
        while i <= 5:
            total += i
            i += 1
        print(total)

#.  What is the difference between a *pre-condition* loop (``while``
    condition at the top) and checking the exit condition inside the
    loop body with ``break``?
    Give one situation where the ``break`` form is cleaner.
