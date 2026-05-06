.. index:: testing; effective, pytest.raises, edge cases

.. _Writing-Tests:

Writing Effective Tests
=======================

.. note::

   *Source:* Python-specific — no direct equivalent in the C# edition.
   Examples test the ``Rational`` class from :ref:`Rational-Class` and
   illustrate best practices applicable to any Python module.

Good tests are specific, independent, and cover edge cases.  Each test
function should check one thing and have a name that explains what
scenario it is testing.

Testing the Rational Class
---------------------------

.. index:: Rational; testing

Assuming ``Rational`` is defined in ``rational.py``:

.. code-block:: python

   from rational import Rational

   def test_normalisation():
       r = Rational(6, -10)
       assert str(r) == "-3/5"

   def test_addition():
       f = Rational(-3, 5)
       h = Rational(1, 2)
       assert str(f + h) == "-1/10"

   def test_multiplication():
       assert Rational(2, 3) * Rational(3, 4) == Rational(1, 2)

   def test_equality():
       assert Rational(2, 4) == Rational(1, 2)
       assert Rational(1, 3) != Rational(1, 4)

   def test_whole_number():
       assert str(Rational(6, 3)) == "2"

   def test_float_conversion():
       assert float(Rational(1, 4)) == 0.25

Testing for Exceptions
-----------------------

.. index:: pytest.raises

Use ``pytest.raises`` as a context manager to verify that an exception
is raised in the expected situation:

.. code-block:: python

   import pytest
   from rational import Rational

   def test_zero_denominator():
       with pytest.raises(ValueError):
           Rational(1, 0)

If the block inside ``with pytest.raises(ValueError):`` does *not* raise
``ValueError``, the test fails.

Edge Cases
----------

.. index:: testing; edge cases

Always test:

- **Zero**: ``factorial(0)``, ``Rational(0, 5)``
- **Negative inputs**: ``Rational(-1, 2)``, ``Rational(1, -2)``
- **Boundary values**: the smallest and largest valid inputs
- **Already-normalised values**: ``Rational(1, 2)`` should stay ``1/2``
- **Idempotent operations**: adding zero, multiplying by one

.. code-block:: python

   def test_add_zero():
       r = Rational(3, 4)
       assert r + Rational(0, 1) == r

   def test_multiply_by_one():
       r = Rational(3, 4)
       assert r * Rational(1) == r

   def test_negative_numerator_and_denominator():
       assert str(Rational(-2, -3)) == "2/3"

Organising Tests in a Class
-----------------------------

.. index:: test class

For a large module, group related tests in a class prefixed with
``Test``:

.. code-block:: python

   class TestRationalArithmetic:
       def test_add(self):
           assert Rational(1, 3) + Rational(1, 6) == Rational(1, 2)

       def test_sub(self):
           assert Rational(3, 4) - Rational(1, 4) == Rational(1, 2)

   class TestRationalComparison:
       def test_less_than(self):
           assert Rational(1, 3) < Rational(1, 2)

pytest discovers and runs these automatically with no extra configuration.

One Assert per Test (Guideline)
---------------------------------

.. index:: testing; one assert per test

When a test contains many assertions and fails, it can be hard to tell
*which* assertion caused the failure.  Prefer one logical check per test
function so failure messages are immediately actionable.
