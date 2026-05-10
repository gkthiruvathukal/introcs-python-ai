.. index:: tuple; examples, tuple; as dict key, zip(), namedtuple; preview

.. _Tuple-Examples:

Tuple Examples
==============

Tuples as Records
-----------------

.. index:: tuple; record

A tuple is a natural way to group a fixed number of related values when
you do not need a full class:

.. code-block:: python

   # 2-D point
   origin = (0, 0)
   point = (3.0, -1.5)

   # RGB colour
   red = (255, 0, 0)
   teal = (0, 128, 128)

   # (name, grade) record
   student = ("Alice", 91)

   name, grade = student
   print(f"{name} earned a {grade}")

Output:

.. code-block:: none

   Alice earned a 91

Tuples as Dictionary Keys
--------------------------

.. index:: tuple; dict key

Because tuples are immutable they can serve as dictionary keys — lists
cannot:

.. code-block:: python

   # Map grid coordinates to a label
   grid = {
       (0, 0): "origin",
       (1, 0): "east",
       (0, 1): "north",
   }

   print(grid[(1, 0)])

Output:

.. code-block:: none

   east

This is useful for representing two-dimensional data, graph edges, or
any pairing that should be looked up quickly.

Iterating Paired Data with ``zip()``
--------------------------------------

.. index:: zip(); paired iteration

``zip()`` pairs elements from multiple sequences into tuples, making it
easy to iterate over related data:

.. code-block:: python

   xs = [0, 1, 2, 3]
   ys = [0, 1, 4, 9]

   for x, y in zip(xs, ys):
       print(f"({x}, {y})")

Output:

.. code-block:: none

   (0, 0)
   (1, 1)
   (2, 4)
   (3, 9)

.. index:: tabular data; tuple list

Building a List of Tuples
--------------------------

.. index:: list; of tuples

A common pattern is building a list of tuples to represent tabular data:

.. code-block:: python

   import math

   table = [(n, n**2, math.sqrt(n)) for n in range(1, 6)]
   for n, sq, root in table:
       print(f"{n:2d}  {sq:4d}  {root:.4f}")

Output:

.. code-block:: none

    1     1  1.0000
    2     4  1.4142
    3     9  1.7321
    4    16  2.0000
    5    25  2.2361

Sorting a List of Tuples
-------------------------

.. index:: sorted(); key with tuple

``sorted()`` compares tuples lexicographically by default (first element
first, then second, etc.):

.. code-block:: python

   students = [("Carol", 85), ("Alice", 91), ("Bob", 78)]
   by_name = sorted(students)
   by_grade = sorted(students, key=lambda s: s[1], reverse=True)

   print(by_name)
   print(by_grade)

Output:

.. code-block:: none

   [('Alice', 91), ('Bob', 78), ('Carol', 85)]
   [('Alice', 91), ('Carol', 85), ('Bob', 78)]

A Preview: Named Tuples
------------------------

.. index:: namedtuple; preview

Plain tuples work well for small, obvious structures, but positional
access can become unclear as tuples grow.  What does ``record[2]`` mean?
Python's ``collections.namedtuple`` solves this by letting you give each
position a name:

.. code-block:: python

   from collections import namedtuple

   Student = namedtuple('Student', ['name', 'grade'])
   s = Student("Alice", 91)
   print(s.name, s.grade)   # clear
   print(s[0], s[1])        # positional access still works

Output:

.. code-block:: none

   Alice 91
   Alice 91

A named tuple is still a tuple — immutable, unpackable, usable as a
dictionary key — but fields are readable by name.  We return to named
tuples in the :ref:`Dataclasses` section, where they are compared with
``@dataclass`` and full classes.

Sorting a List of Named Tuples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: namedtuple; sorting

Named field access makes sort keys easier to read.  Compare the plain-
tuple version from above with the named-tuple version:

.. code-block:: python

   from collections import namedtuple

   Student = namedtuple('Student', ['name', 'grade'])

   students = [Student("Carol", 85), Student("Alice", 91), Student("Bob", 78)]
   by_name  = sorted(students)
   by_grade = sorted(students, key=lambda s: s.grade, reverse=True)

   print(by_name)
   print(by_grade)

Output:

.. code-block:: none

   [Student(name='Alice', grade=91), Student(name='Bob', grade=78), Student(name='Carol', grade=85)]
   [Student(name='Alice', grade=91), Student(name='Carol', grade=85), Student(name='Bob', grade=78)]

.. index:: lambda; sort key

``lambda s: s.grade`` is clearer than ``lambda s: s[1]`` — the intent
is self-documenting.  Default (lexicographic) sorting still works
because named tuples compare like ordinary tuples.
