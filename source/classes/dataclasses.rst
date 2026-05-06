.. index:: dataclass, @dataclass

.. _Dataclasses:

Python Dataclasses
==================

.. note::

   *Source:* Python-specific — no direct equivalent in the C# edition.
   ``@dataclass`` (introduced in Python 3.7) automatically generates
   ``__init__``, ``__repr__``, and ``__eq__`` for classes that primarily
   hold data, reducing boilerplate.

Writing a data-holding class by hand requires repeating each field name
three or four times — in ``__init__`` parameters, in ``self.x = x``
assignments, and in ``__repr__``.  The ``@dataclass`` decorator generates
all of this automatically from a simple field declaration.

Basic Dataclass
---------------

.. index:: @dataclass; basic

.. code-block:: python

   from dataclasses import dataclass

   @dataclass
   class Contact:
       name: str
       phone: str
       email: str

This single declaration is equivalent to:

.. code-block:: python

   class Contact:
       def __init__(self, name: str, phone: str, email: str):
           self.name = name
           self.phone = phone
           self.email = email

       def __repr__(self):
           return f"Contact(name={self.name!r}, phone={self.phone!r}, email={self.email!r})"

       def __eq__(self, other):
           return (self.name, self.phone, self.email) == (other.name, other.phone, other.email)

.. code-block:: python

   c = Contact("Marie Ortiz", "773-508-7890", "mortiz2@luc.edu")
   print(c)
   print(c == Contact("Marie Ortiz", "773-508-7890", "mortiz2@luc.edu"))

Output:

.. code-block:: none

   Contact(name='Marie Ortiz', phone='773-508-7890', email='mortiz2@luc.edu')
   True

Default Values
--------------

.. index:: @dataclass; defaults

Fields can have default values, just like function parameters:

.. code-block:: python

   @dataclass
   class Point:
       x: float = 0.0
       y: float = 0.0

   origin = Point()
   p = Point(3.0, 4.0)
   print(origin, p)

Output:

.. code-block:: none

   Point(x=0.0, y=0.0) Point(x=3.0, y=4.0)

Adding Methods
--------------

.. index:: @dataclass; methods

You can still add your own methods — ``@dataclass`` only generates the
boilerplate:

.. code-block:: python

   import math

   @dataclass
   class Point:
       x: float
       y: float

       def distance_to(self, other):
           return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

       def __str__(self):
           return f"({self.x}, {self.y})"

Immutable Dataclasses
----------------------

.. index:: @dataclass; frozen

Pass ``frozen=True`` to make instances immutable (and hashable, so they
can be used as dictionary keys):

.. code-block:: python

   @dataclass(frozen=True)
   class Point:
       x: float
       y: float

   p = Point(1.0, 2.0)
   # p.x = 5.0   # raises FrozenInstanceError

When to Use ``@dataclass``
---------------------------

Use ``@dataclass`` when a class is primarily a container for related
fields and you want automatic ``__init__`` and ``__repr__``.  Write a
class by hand when you need fine-grained control over initialisation,
validation, or private attributes.
