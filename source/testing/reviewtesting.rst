.. index:: review questions; testing

.. _Review-Testing:

Chapter Review Questions
========================

.. note::

   *Source:* Python-specific — no direct equivalent in the C# edition.
   Questions cover pytest conventions, assert usage, and testing strategy.

#.  What naming convention must a test file follow for pytest to discover
    it automatically?

#.  What naming convention must a test function follow?

#.  What happens when an ``assert`` statement fails inside a test function?

#.  Write a test function that verifies ``abs(-5) == 5``.

#.  ``pytest.raises``.

    a.  What does ``pytest.raises(ValueError)`` do?
    b.  When would you use it?

#.  What is the difference between a *unit test* and an *integration test*?

#.  Give three examples of edge cases you should always consider when
    writing tests for a numeric function.

#.  Why is it generally better to have one assertion per test function
    rather than many?

#.  How do you run only the tests in a file called ``test_strings.py``
    from the command line?

#.  C# vs. Python testing.

    a.  In the C# edition, what attribute marks a test method?
    b.  What is the Python pytest equivalent?
    c.  What replaces ``Assert.AreEqual`` in pytest?
