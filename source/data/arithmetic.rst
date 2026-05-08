.. index:: arithmetic

.. _arithmetic:

Arithmetic
==========

.. note::

   *Source:* Drawn from the SE4ML Python chapter (``chapter_python.rst``,
   lines 196–441) and the C# edition (``data/arithmetic.rst``).  Operator
   tables, integer vs. float distinction, and ``math`` module introduction
   closely follow the SE4ML presentation.

We start with integers and arithmetic — not because arithmetic is exciting, but
because the symbolism should be mostly familiar.

.. index:: Python; interactive shell
   REPL

Testing Expressions in the Shell
---------------------------------

Python's interactive shell is perfect for trying out arithmetic.  Start it
with ``python3`` and type expressions at the ``>>>`` prompt:

.. code-block:: none

   >>> 2 + 3
   5
   >>> 10 - 4
   6
   >>> 3 * 7
   21

The shell evaluates the expression and prints the result immediately.  This
is much faster than writing a whole program for small experiments.

.. index:: integer, float

Numeric Types
-------------

Python has two main numeric types for beginners:

``int``
   Whole numbers, positive or negative, with no fractional part:
   ``0``, ``42``, ``-17``, ``1000000``.

   Python integers have *unlimited precision* — they can be as large as
   your computer's memory allows.  There is no overflow.

``float``
   Approximate real numbers, written with a decimal point or an exponent:
   ``.2``, ``2.0``, ``20.``, ``2000e-1``, ``2E3``.

.. code-block:: none

   >>> type(42)
   <class 'int'>
   >>> type(3.14)
   <class 'float'>

.. index:: operator; arithmetic

Arithmetic Operators
--------------------

The arithmetic operators in Python are:

.. list-table::
   :header-rows: 1
   :widths: 15 20 40

   * - Operator
     - Meaning
     - Example
   * - ``+``
     - Addition
     - ``3 + 4`` → ``7``
   * - ``-``
     - Subtraction
     - ``10 - 3`` → ``7``
   * - ``*``
     - Multiplication
     - ``3 * 4`` → ``12``
   * - ``/``
     - Division (always float)
     - ``7 / 2`` → ``3.5``
   * - ``//``
     - Floor division (integer result)
     - ``7 // 2`` → ``3``
   * - ``%``
     - Remainder (modulus)
     - ``7 % 2`` → ``1``
   * - ``**``
     - Exponentiation
     - ``2 ** 10`` → ``1024``
   * - ``-x``
     - Negation (unary)
     - ``-5``

.. index:: operator; /; true division, operator; //; floor division, operator; %; modulus, operator; **; exponentiation

A key difference from many other languages: ``/`` *always* produces a
``float``, even if both operands are integers:

.. code-block:: none

   >>> 7 / 2
   3.5
   >>> 6 / 2
   3.0

Use ``//`` when you want a whole-number result:

.. code-block:: none

   >>> 7 // 2
   3
   >>> -7 // 2
   -4

.. index:: operator precedence

Operator Precedence
-------------------

Python follows the standard mathematical order of operations.  From highest
to lowest precedence:

1. ``**`` (exponentiation, right to left)
2. ``-x`` (unary negation)
3. ``*``, ``/``, ``//``, ``%`` (multiplication and division)
4. ``+``, ``-`` (addition and subtraction)

Use parentheses to override the default order:

.. code-block:: none

   >>> 2 + 3 * 4
   14
   >>> (2 + 3) * 4
   20

See the appendix for the complete precedence table.

.. index:: mixed arithmetic, type conversion

Mixed Arithmetic
----------------

When you mix ``int`` and ``float`` in an expression, Python converts the
``int`` to ``float`` automatically:

.. code-block:: none

   >>> 1 + 2.0
   3.0
   >>> type(1 + 2)
   <class 'int'>
   >>> type(1 + 2.0)
   <class 'float'>

.. index:: widening conversion, implicit type conversion

This *widening* conversion preserves the value.

.. index:: built-in functions; abs, round, divmod

Useful Built-in Functions
--------------------------

Python provides several useful arithmetic functions built in — no import
needed:

.. list-table::
   :header-rows: 1
   :widths: 20 50

   * - Function
     - Description
   * - ``abs(x)``
     - Absolute value of ``x``
   * - ``round(x)``
     - Round to nearest integer
   * - ``round(x, n)``
     - Round to ``n`` decimal places
   * - ``divmod(x, y)``
     - Returns ``(x // y, x % y)`` as a tuple
   * - ``pow(x, y)``
     - ``x ** y``  (also ``pow(x, y, z)`` for modular exponentiation)
   * - ``max(a, b, ...)``
     - Largest value
   * - ``min(a, b, ...)``
     - Smallest value

.. code-block:: none

   >>> abs(-7)
   7
   >>> round(3.14159, 2)
   3.14
   >>> divmod(17, 5)
   (3, 2)

.. index:: math module, math.sqrt(), math.floor(), math.ceil(), math.pi

The ``math`` module provides more functions.  Import it first:

.. code-block:: none

   >>> import math
   >>> math.sqrt(2)
   1.4142135623730951
   >>> math.pi
   3.141592653589793
   >>> math.floor(3.7)
   3
   >>> math.ceil(3.2)
   4
