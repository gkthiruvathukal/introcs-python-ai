.. index:: class; examples, Averager class, __repr__

.. _Class-Examples:

Class Instance Examples
=======================

.. note::

   *Source:* Adapted from the C# edition (``classes/classexamples.rst``).
   The ``Averager`` example is a direct Python translation.  C#'s
   ``Print()`` method is replaced by ``__str__``; ``__repr__`` is added
   as a Python-specific bonus for interactive use.

The Averager Class
------------------

.. index:: Averager class

An ``Averager`` accumulates numeric values one at a time and reports
their running average.  It illustrates a class whose instance variables
track *changing internal state* rather than simply storing data:

.. literalinclude:: ../../examples/introcs-python/classes/averager.py
   :language: python
   :start-after: # start: Averager
   :end-before: # end: Averager

.. code-block:: python

   avg = Averager()
   for value in [3.0, 7.5, 2.0, 6.5]:
       avg.add_datum(value)
   print(avg.get_count(), "values")
   print(f"Average: {avg.get_average():.2f}")
   print(avg)

Output:

.. code-block:: none

   4 values
   Average: 4.75
   Averager(4 values, avg=4.7500)

The ``_count`` and ``_total`` prefixes with ``_`` signal that these are
internal attributes not meant to be accessed from outside the class.

``__str__`` and ``__repr__``
-----------------------------

.. index:: __repr__

Python uses two methods for string representations:

- ``__str__`` is called by ``print()`` and ``str()`` — intended for
  human-readable output.
- ``__repr__`` is called in the interactive interpreter and by ``repr()``
  — intended for an unambiguous, developer-readable representation.

A useful rule: if possible, write ``__repr__`` so that ``eval(repr(obj))``
recreates the object.

.. code-block:: python

   class Point:
       def __init__(self, x: float, y: float):
           self.x = x
           self.y = y

       def __str__(self) -> str:
           return f"({self.x}, {self.y})"

       def __repr__(self) -> str:
           return f"Point({self.x!r}, {self.y!r})"

.. code-block:: python

   p = Point(3, 7)
   print(str(p))    # uses __str__
   print(repr(p))   # uses __repr__

Output:

.. code-block:: none

   (3, 7)
   Point(3, 7)

A Distance Method
-----------------

.. index:: class; method with same-type parameter

Methods can accept parameters of the same class.  Here ``distance_to``
receives another ``Point``:

.. code-block:: python

       def distance_to(self, other: "Point") -> float:
           import math
           return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

.. code-block:: python

   p1 = Point(0, 0)
   p2 = Point(3, 4)
   print(p1.distance_to(p2))

Output:

.. code-block:: none

   5.0

Inside ``distance_to``, ``self`` refers to the object the method was
called on (``p1``), and ``other`` refers to the argument (``p2``).
Both are ``Point`` objects, and both sets of instance variables are
accessible.
