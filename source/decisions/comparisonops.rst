.. index:: comparison operators, relational operators

More Conditional Expressions
=============================

We introduced the basic comparison operators in the previous section.
Here we look at a few more expressions that produce Boolean results.

.. index:: in operator, not in operator

Membership Testing
------------------

The ``in`` operator tests whether a value appears in a sequence (string,
list, tuple, etc.):

.. code-block:: none

   >>> "lo" in "hello"
   True
   >>> "xyz" in "hello"
   False
   >>> 3 in [1, 2, 3, 4]
   True

``not in`` is the negation:

.. code-block:: none

   >>> "xyz" not in "hello"
   True

.. index:: is operator, is not operator, None; testing

Identity: ``is`` and ``is not``
--------------------------------

The ``is`` operator tests whether two names refer to the *same object*, not
just equal values.  Its most common use is testing for ``None``:

.. code-block:: none

   >>> x = None
   >>> x is None
   True
   >>> x is not None
   False

Use ``is None`` rather than ``== None`` — it is more precise and Pythonic.

.. index:: string; comparison, lexicographic order, ASCII; ordering

Comparison with Strings
-----------------------

String comparison uses lexicographic (dictionary) order:

.. code-block:: none

   >>> "apple" < "banana"
   True
   >>> "Z" < "a"    # uppercase letters come before lowercase in ASCII
   True
   >>> "cat" == "cat"
   True

.. index:: chained comparison

Chained Comparisons Revisited
------------------------------

Python's chained comparisons work with all comparison operators:

.. code-block:: none

   >>> score = 85
   >>> 0 <= score <= 100
   True
   >>> 'a' <= 'c' <= 'z'
   True

Be cautious when mixing ``is`` in a chain — it is unusual and can be
confusing.  For numeric range checks, chaining is clear and idiomatic.
