.. index:: pytest, testing; pytest, test function
   ACM-IEEE CS2013; SDF4 Development Methods
   ACM-IEEE CS2023; SDF4 Development Methods
   ACM-IEEE CS2013; SE7 Verification and Validation
   ACM-IEEE CS2023; SE7 Verification and Validation

.. _Pytest-Intro:

Introduction to pytest
======================

Testing is the practice of running code with known inputs and checking
that the outputs match expectations.  A *test* that passes gives
confidence that a function works; a test that fails pinpoints exactly
what broke.

Installing pytest
-----------------

.. index:: pytest; install

.. code-block:: none

   pip install pytest

Running Tests
-------------

.. index:: pytest; running

Place test functions in files named ``test_*.py`` or ``*_test.py``.
Run all tests in the current directory:

.. code-block:: none

   pytest

Run a specific file:

.. code-block:: none

   pytest test_mymodule.py

pytest prints a dot for each passing test and ``F`` for each failure,
followed by a detailed report of what went wrong.

Writing a First Test
---------------------

.. index:: test function, assert

Suppose we have a function in ``mymath.py``:

.. code-block:: python

   def factorial(n: int) -> int:
       if n == 0:
           return 1
       return n * factorial(n - 1)

A test file ``test_mymath.py``:

.. code-block:: python

   from mymath import factorial

   def test_factorial_zero() -> None:
       assert factorial(0) == 1

   def test_factorial_positive() -> None:
       assert factorial(5) == 120

   def test_factorial_one() -> None:
       assert factorial(1) == 1

Running ``pytest`` produces:

.. code-block:: none

   ...
   3 passed in 0.01s

If a test fails — say we accidentally write ``factorial(5) == 119`` —
pytest shows exactly which assertion failed and what the actual values
were:

.. code-block:: none

   FAILED test_mymath.py::test_factorial_positive
   AssertionError: assert 120 == 119

.. index:: test discovery, naming convention; test files

How pytest Finds Tests
-----------------------

.. index:: pytest; test discovery

pytest discovers tests automatically:

- Files matching ``test_*.py`` or ``*_test.py``
- Functions inside those files starting with ``test_``
- Methods starting with ``test_`` inside classes starting with ``Test``

You do not need a ``main`` function or any special imports beyond the
module under test.

