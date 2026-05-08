.. index:: class; Rational, operator overloading, dunder methods

.. _Rational-Class:

The Rational Class
==================

.. note::

   *Source:* Adapted from the C# edition (``classes/rational.rst``).
   Python's dunder (double-underscore) methods replace C#'s
   ``operator+``, ``operator*``, and ``CompareTo`` syntax.
   Python's ``math.gcd`` replaces the hand-coded GCD function.

A *rational number* is a ratio of two integers: 2/3, -5/4, 7.  We build
a ``Rational`` class that stores numerator and denominator in lowest
terms and supports arithmetic with natural Python operators.

Class Definition and Normalisation
------------------------------------

.. index:: Rational; __init__, gcd

.. code-block:: python

   import math

   class Rational:
       def __init__(self, numerator: int, denominator: int = 1):
           if denominator == 0:
               raise ValueError("Denominator cannot be zero")
           g = math.gcd(abs(numerator), abs(denominator))
           sign = -1 if denominator < 0 else 1
           self._num = sign * numerator // g
           self._denom = sign * denominator // g

       def numerator(self) -> int:
           return self._num

       def denominator(self) -> int:
           return self._denom

``math.gcd`` reduces the fraction to lowest terms.  We force the
denominator to always be positive so ``-3/5`` is stored as ``(-3, 5)``
rather than ``(3, -5)``.

String Representation
---------------------

.. index:: Rational; __str__, __repr__

.. code-block:: python

       def __str__(self) -> str:
           if self._denom == 1:
               return str(self._num)
           return f"{self._num}/{self._denom}"

       def __repr__(self) -> str:
           return f"Rational({self._num}, {self._denom})"

Arithmetic Operators
--------------------

.. index:: Rational; __add__, __mul__, __sub__, __truediv__

Python calls ``__add__`` when ``+`` is used between two ``Rational``
objects:

.. code-block:: python

       def __add__(self, other: "Rational") -> "Rational":
           return Rational(
               self._num * other._denom + other._num * self._denom,
               self._denom * other._denom
           )

       def __sub__(self, other: "Rational") -> "Rational":
           return Rational(
               self._num * other._denom - other._num * self._denom,
               self._denom * other._denom
           )

       def __mul__(self, other: "Rational") -> "Rational":
           return Rational(self._num * other._num,
                           self._denom * other._denom)

       def __truediv__(self, other: "Rational") -> "Rational":
           return Rational(self._num * other._denom,
                           self._denom * other._num)

Comparison Operators
--------------------

.. index:: Rational; __eq__, __lt__

.. code-block:: python

       def __eq__(self, other: object) -> bool:
           return self._num == other._num and self._denom == other._denom

       def __lt__(self, other: "Rational") -> bool:
           return self._num * other._denom < other._num * self._denom

       def __le__(self, other: "Rational") -> bool:
           return self == other or self < other

Conversion Methods
------------------

.. index:: Rational; float()

.. code-block:: python

       def __float__(self) -> float:
           return self._num / self._denom

Putting It Together
--------------------

.. code-block:: python

   f = Rational(6, -10)
   h = Rational(1, 2)

   print(f)              # -3/5  (normalised automatically)
   print(f + h)          # -1/10
   print(f * h)          # -3/10
   print(h > f)          # True
   print(float(f))       # -0.6

Output:

.. code-block:: none

   -3/5
   -1/10
   -3/10
   True
   -0.6

Python dispatches ``f + h`` to ``f.__add__(h)`` and ``h > f`` to
``h.__gt__(f)`` (derived automatically from ``__lt__`` and ``__eq__``
when Python can't find ``__gt__`` directly).

Static Parse Method
-------------------

.. index:: Rational; classmethod, @classmethod

A class method acts on the class itself rather than an instance —
Python's replacement for C#'s ``static Parse``:

.. code-block:: python

       @classmethod
       def parse(cls, s: str) -> "Rational":
           if "/" in s:
               num, denom = s.split("/")
               return cls(int(num), int(denom))
           if "." in s:
               digits_after = len(s.split(".")[1])
               value = int(s.replace(".", ""))
               return cls(value, 10 ** digits_after)
           return cls(int(s))

.. code-block:: python

   print(Rational.parse("-12/30"))   # -2/5
   print(Rational.parse("1.125"))    # 9/8
   print(Rational.parse("7"))        # 7
